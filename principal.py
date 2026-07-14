# Importa as funções do programa
from funcoes import mostrar, editar, ranking
# Importa a função sleep
from time import sleep

# Laço principal do programa 
while True:
    # Exibe o menu de opções
    print("=" * 50)
    print("                      MENU")
    print("=" * 50)
    print("[1] Mostrar")
    print("[2] Editar")
    print("[3] Ranking")
    print("[4] Sair")
    # Pede que o usuário digite sua opção
    opcao = int(input("Escolha uma opção: "))
    sleep(1.5)
    # Mostra todas as seleções
    if opcao == 1:
        mostrar()
    # Edita os dados de uma seleção
    elif opcao == 2:
        editar()
    # Exibe o ranking dos três melhores jogadores
    elif opcao == 3:
        ranking()
    # Encerra o programa
    elif opcao == 4:
        print("Aguarde, estamos finalizando o programa...")
        sleep(2)
        print("Programa encerrado!")
        break
    # Se a opção escolhida não for nenhuma das listadas acima, ele mostra opção inválida e mostra novamente o menu    
    else:
        print("Opção inválida!")