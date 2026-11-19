
from input_handler import validar_alfabeto_inicial
from validator_ip import validar_ip
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

            if validar_alfabeto_inicial(entrada):
                if validar_ip(entrada):
                    print("ACEITA")
                else:
                    print("REJEITA")
            else:
                print("REJEITA")

        elif opcao == "2":
            entrada = input("Digite a URL: ")

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
