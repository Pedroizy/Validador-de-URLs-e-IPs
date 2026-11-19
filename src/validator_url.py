# Autômato Finito Determinístico para validação sintática de URLs.
# Formato aceito: [http://|https://]dominio.ext
#   dominio = letras/dígitos; ext = letras (ex.: com, br)

LETRAS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITOS = set("0123456789")

ESTADO_INICIAL = "q0"
ESTADOS_FINAIS = {"qF"}


def classificar(c: str) -> str:
    """Mapeia um caractere para sua classe no alfabeto Sigma."""
    if c in LETRAS:
        return "L"
    if c in DIGITOS:
        return "D"
    return c  # '.', ':', '/' ou símbolo inválido


def delta(estado: str, c: str):
    """Função de transição. Retorna o próximo estado ou None (rejeita)."""
    cl = classificar(c)
    # ... a tabela de transições:
    return None


def validar_url(cadeia: str) -> bool:
    estado = ESTADO_INICIAL
    for c in cadeia:
        estado = delta(estado, c)
        if estado is None:
            return False
    return estado in ESTADOS_FINAIS