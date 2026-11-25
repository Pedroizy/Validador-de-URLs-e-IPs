
from input_handler import limpar_entrada
from validator_ip import processar_ip
from validator_url import validar_url
from input_handler import limpar_entrada, validar_alfabeto_inicial 

def main():
    while True:
        print("\n========== VALIDADOR DE IP E URL ==========")
        print("1 - Validar IP")
        print("2 - Validar URL")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            entrada = limpar_entrada(input("Digite o endereço IP: "))
            if  validar_alfabeto_inicial(entrada, "ip"):
                
                if processar_ip(entrada):
                    print("ACEITA")
                else:
                    print("REJEITA")
            else:
                print("ERRO: Foram inseridos caracteres não permitidos em um IP.")

        elif opcao == "2":
            entrada = limpar_entrada(input("Digite a URL: "))
            if validar_alfabeto_inicial(entrada, "url"):

                if validar_url(entrada):
                    print("ACEITA")
                else:
                    print("REJEITA")
            else:
                print("ERRO: Foram inseridos caracteres não permitidos em uma URL.")        

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Escolha 1, 2 ou 0.")


if __name__ == "__main__":
    main()
