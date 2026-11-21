def limpar_entrada(texto):
   
    # remove espaços em branco do inicio e fim, da entrada
    
    return texto.strip()

def validar_alfabeto_inicial(texto, tipo):
    #carateres permitidos
    caracteres_ip = "0123456789."
    caracteres_url = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "01234567089:/.-"
    )  # Escolhe o negocio correto

    if tipo == "ip":
        permitidos = caracteres_ip

    elif tipo == "url":
        permitidos = caracteres_url

    else:

        return False



    for caractere in texto:
        if caractere not in permitidos:
        
            return False
    
    return True    

if __name__ == "__main__":
    entrada = input("digite um IP ou URL:")
    resultado = limpar_entrada (entrada)
   
    print(resultado)


    print(validar_alfabeto_inicial("192.168.0.a", "ip"))
    print(validar_alfabeto_inicial("https://exemplo.com", "url"))
    print(validar_alfabeto_inicial("192.168.0.1", "tipo_invalido"))
