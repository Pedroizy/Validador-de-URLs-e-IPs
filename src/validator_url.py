# Automato Finito Deterministico (AFD) para validacao sintatica de URLs.
#
# Linguagem reconhecida:   [http:// | https://]  dominio . (com | br)
#   - dominio: uma ou mais letras (a-z, A-Z) ou digitos (0-9)
#   - protocolo e extensao devem estar em letras minusculas
#
# M = (Q, Sigma, delta, q0, F)   com   F = {q14}
# Estado de erro (armadilha): qe. Toda transicao nao listada leva a qe.

LETRAS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITOS = set("0123456789")
ALFANUMERICOS = LETRAS | DIGITOS
SIGMA = ALFANUMERICOS | {".", ":", "/"}

ESTADO_INICIAL = "q0"
ESTADOS_FINAIS = {"q14"}
ESTADO_ERRO = "qe"

# Transicoes por simbolo especifico: (estado, simbolo) -> proximo estado
TRANSICOES = {
    # reconhecimento do prefixo "http" / "https"
    ("q0", "h"): "q1",
    ("q1", "t"): "q2",
    ("q2", "t"): "q3",
    ("q3", "p"): "q4",
    ("q4", "s"): "q5",
    # separador "://"
    ("q4", ":"): "q6",
    ("q5", ":"): "q6",
    ("q6", "/"): "q7",
    ("q7", "/"): "q8",
    # extensao ".com" ou ".br"
    ("q10", "c"): "q11",
    ("q11", "o"): "q12",
    ("q12", "m"): "q14",
    ("q10", "b"): "q13",
    ("q13", "r"): "q14",
}

# Estados em que qualquer alfanumerico (nao tratado acima) leva ao dominio q9
ESTADOS_DOMINIO = {"q0", "q1", "q2", "q3", "q4", "q5", "q8", "q9"}

# Estados em que o '.' (apos >= 1 caractere de dominio) leva a q10
ESTADOS_PONTO = {"q1", "q2", "q3", "q4", "q5", "q9"}


def delta(estado: str, simbolo: str) -> str:
    """Funcao de transicao delta: Q x Sigma -> Q (total, com estado de erro)."""
    if estado == ESTADO_ERRO:
        return ESTADO_ERRO
    if (estado, simbolo) in TRANSICOES:
        return TRANSICOES[(estado, simbolo)]
    if simbolo in ALFANUMERICOS and estado in ESTADOS_DOMINIO:
        return "q9"
    if simbolo == "." and estado in ESTADOS_PONTO:
        return "q10"
    return ESTADO_ERRO


def validar_url(cadeia: str, verbose: bool = False) -> bool:
    """Retorna True se a cadeia pertence a linguagem do automato."""
    estado = ESTADO_INICIAL
    if verbose:
        print(f"{estado}", end="")
    for simbolo in cadeia:
        estado = delta(estado, simbolo)
        if verbose:
            print(f" --{simbolo}--> {estado}", end="")
        if estado == ESTADO_ERRO:
            break
    if verbose:
        print()
    return estado in ESTADOS_FINAIS


if __name__ == "__main__":
    exemplos = [
        "google.com",
        "http://google.com",
        "https://ufal.br",
        "http://.com",
        "google.org",
    ]
    for url in exemplos:
        resultado = "VALIDA" if validar_url(url, verbose=True) else "INVALIDA"
        print(f"  {url!r}: {resultado}\n")