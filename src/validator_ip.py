def validar_bloco(bloco: str) -> bool:
    """
    Regra interna para validar se um bloco numérico do IP é válido:
    - Não pode estar vazio.
    - Deve conter apenas dígitos.
    - Não pode ter zeros à esquerda desnecessários (ex: '01' é inválido, mas '0' é válido).
    - O valor numérico deve estar entre 0 e 255.
    """
    if not bloco:
        return False
    
    # Se tem mais de um caractere e começa com '0', é inválido (ex: '01', '00')
    if len(bloco) > 1 and bloco[0] == '0':
        return False
        
    # Garante que todos os caracteres são dígitos numéricos
    if not bloco.isdigit():
        return False
        
    valor = int(bloco)
    return 0 <= valor <= 255


def processar_ip(cadeia: str) -> bool:
    """
    Núcleo de transição do autômato para validar a estrutura sintática de um IPv4.
    Espera uma string contendo dígitos e pontos (ex: '192.168.0.1').
    """
    if not cadeia:
        print("[REJEITA] A cadeia de IP está vazia.")
        return False

    # Separa a string utilizando o ponto (.) como delimitador
    blocos = cadeia.split('.')

    # Um IPv4 válido deve ter obrigatoriamente 4 blocos numéricos
    if len(blocos) != 4:
        print(f"[REJEITA] Estrutura inválida: o IP deve conter exatamente 4 blocos separados por pontos. (Encontrados: {len(blocos)})")
        return False

    # Valida cada bloco individualmente de acordo com as regras de autômato/redes
    for i, bloco in enumerate(blocos):
        if not validar_bloco(bloco):
            print(f"[REJEITA] Bloco {i+1} ('{bloco}') é inválido. Deve estar entre 0 e 255 sem zeros à esquerda inválidos.")
            return False

    print(f"[ACEITA] O endereço IPv4 '{cadeia}' é sintaticamente VÁLIDO.")
    return True


if __name__ == "__main__":
    # Teste rápido executando o arquivo de forma isolada
    print("--- TESTE DO MÓDULO VALIDADOR DE IPV4 ---")
    
    testes_exemplo = [
        "192.168.0.1",   # Deve aceitar
        "10.0.0.255",    # Deve aceitar
        "256.100.0.1",   # Deve rejeitar (estouro de valor > 255)
        "192.168..1",    # Deve rejeitar (bloco vazio)
        "192.168.0.01",   # Deve rejeitar (zero à esquerda inválido)
        "10.100.0.86"
    ]
    
    for ip in testes_exemplo:
        print(f"\nTestando: '{ip}'")
        processar_ip(ip)