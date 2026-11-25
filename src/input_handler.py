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
