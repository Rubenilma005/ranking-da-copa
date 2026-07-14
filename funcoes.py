# Importação necessária para criar tabelas 
from terminaltables import AsciiTable
# Irá importar o arquivo dados do dicionário das selecoes
from dados import selecoes
# Importa a função sleep que atua como temporizador
from time import sleep

# Pesos utilizados no cálculo da pontuação para gerar o ranking
peso_gols = 0.5
peso_assistencias = 0.3
peso_premios = 0.5

# Função que mostra todos os dados das seleções na tabela
def mostrar():
    tabela = [
        ["Seleção", "Jogador", "Partidas", "Gols", "Assistências", "Prêmios"]
    ]
    # Percorre todas as seleções cadastradas
    for selecao, dados in selecoes.items():
        tabela.append([
            selecao,
            dados["jogador"],
            dados["partidas"],
            dados["gols"],
            dados["assistencias"],
            dados["premios_individuais"]
     
       ])
        
    # Exibe os dados organizaos dentro da tabela
    table = AsciiTable(tabela)
    print(table.table)

# Edita todos os dados de uma seleção
def editar():
    selecao = input("Informe a seleção que deseja editar: ").title()
    # Solicita a seleção que será editada
    if selecao in selecoes:
# Verifica se a seleção existe para realizar edição dos dados ou manter, por fim atualiza os dados
        while True:
            novo_jogador = input(f"Novo jogador ou Enter para manter '{selecoes[selecao]['jogador']}': ")

            if novo_jogador == "":
                break

            if novo_jogador.replace(" ", "").isalpha():
                selecoes[selecao]["jogador"] = novo_jogador.upper()
                break

            print("Valor inválido! Digite apenas letras.")

        while True:
            nova_partida = input(f"Nova quantidade de partidas ou Enter para manter '{selecoes[selecao]['partidas']}': ")

            if nova_partida == "":
                break

            if nova_partida.isdigit() and int(nova_partida) > 0:
                selecoes[selecao]["partidas"] = int(nova_partida)
                break

            print("Valor inválido! Digite um número inteiro maior que zero.")

        while True:
            novo_gol = input(f"Nova quantidade de gols ou Enter para manter '{selecoes[selecao]['gols']}': ")

            if novo_gol == "":
                break

            if novo_gol.isdigit():
                selecoes[selecao]["gols"] = int(novo_gol)
                break

            print("Valor inválido! Digite um número inteiro.")

        while True:
            nova_assistencia = input(f"Nova quantidade de assistências ou Enter para manter '{selecoes[selecao]['assistencias']}': ")

            if nova_assistencia == "":
                break

            if nova_assistencia.isdigit():
                selecoes[selecao]["assistencias"] = int(nova_assistencia)
                break

            print("Valor inválido! Digite um número inteiro.")

        while True:
            novo_premio = input(f"Novos Prêmios Individuais ou Enter para manter '{selecoes[selecao]['premios_individuais']}': ")

            if novo_premio == "":
                break

            if novo_premio.isdigit():
                selecoes[selecao]["premios_individuais"] = int(novo_premio)
                break

            print("Valor inválido! Digite um número inteiro.")
        # Confirma a atualização
        print("Aguarde a atualização...")
        sleep(2)
        print("Atualização concluída!✅")
# Se a seleção não existe, mostra a mensagem de que a seleçao não encontrada, e retorna ao menu
    else:
        print("Aguarde...")
        sleep(2)
        print("Seleção não encontrada!❌")

# Função que calcula o ranking dos três melhores jogadores
def ranking():
# Armazena a pontuação dos jogadores 
    ranking = []
# Percorre todas as seleções para calcular a pontuação
    for selecao, dados in selecoes.items():
       # Calcula a pontuação do jogador com base nos dados e com o uso da fórmula que pega os dados e multiplica pelo peso, diividindo cada dados pela quantidade e partidas a fim de não favorecer ninguém. Por fim, soma cada dados(gol, assistência e premios) para obter o resultado final
        pontuacao = (
            (dados["gols"] / dados["partidas"]) * peso_gols +
            (dados["assistencias"] / dados["partidas"]) * peso_assistencias +
            (dados["premios_individuais"] / dados["partidas"]) * peso_premios
        )
        # Armazena a pontuação, seleção e jogador
        ranking.append([pontuacao, selecao, dados["jogador"]])
    # Ordena a lista da maior para a menor pontuação
    ranking.sort(reverse=True)

    print("\n===== 🎺🎊 RANKING DOS TRÊS MELHORES JOGADORES DA COPA DO MUNDO DE 2026 🎊🎺 =====")
    print()
    print("AGUARDE...Estamos solicitando memória RAM extra para suportar o peso desse trio.")
    sleep(5)
    # Cria a tabela do ranking
    tabela = [
        ["Posição", "Seleção", "Jogador", "Pontuação"]
    ]

    tabela.append(["🥇", ranking[0][1], ranking[0][2], f"{ranking[0][0]:.1f}"])
    tabela.append(["🥈", ranking[1][1], ranking[1][2], f"{ranking[1][0]:.1f}"])
    tabela.append(["🥉", ranking[2][1], ranking[2][2], f"{ranking[2][0]:.1f}"])

    table = AsciiTable(tabela)
    print(table.table)
