
from input_handler import limpar_entrada
from validator_ip import processar_ip
from validator_url import validar_url


def main():
    while True:
        print("\n========== VALIDADOR DE IP E URL ==========")
        print("1 - Validar IP")
        print("2 - Validar URL")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            entrada = input("Digite o endereço IP: ")
            entrada = limpar_entrada(entrada)

            if processar_ip(entrada):
                print("ACEITA")
            else:
                print("REJEITA")

        elif opcao == "2":
            entrada = input("Digite a URL: ")
            entrada = limpar_entrada(entrada)

            if validar_url(entrada):
                print("ACEITA")
            else:
                print("REJEITA")

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Escolha 1, 2 ou 0.")


if __name__ == "__main__":
    main()
