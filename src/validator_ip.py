# Módulo 1: Validação de Alfabeto e Estado Inicial (Responsabilidade do Pedro)

ALFABETO_PERMITIDO = set("0123456789.")

def validar_alfabeto_inicial(cadeia: str) -> bool:
    """
    Verifica se a cadeia contém apenas símbolos válidos do alfabeto (Sigma)
    e inicializa o processo do autômato.
    """
    if not cadeia:
        return False
        
    # Garante que todos os caracteres da string pertencem ao alfabeto Σ
    for char in cadeia:
        if char not in ALFABETO_PERMITIDO:
            print(f"Erro: Caractere inválido encontrado -> '{char}'")
            return False
            
    print(string_inicializacao(cadeia))
    return True

def string_inicializacao(cadeia: str) -> str:
    return f"Iniciando processamento do autômato para a cadeia: '{cadeia}' a partir de q0."

if __name__ == "__main__":
    # Teste rápido do seu módulo isolado
    teste = "192.168"
    if validar_alfabeto_inicial(teste):
        print("Alfabeto validado com sucesso! Pronto para passar para o próximo estado.")