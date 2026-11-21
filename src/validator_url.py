# Automato Finito Deterministico (AFD) para validacao sintatica de URLs.
#
# Linguagem reconhecida:
#     [http:// | https://]  rotulo . rotulo . ... . extensao
#   - rotulo:   comeca com letra ou digito; depois aceita letras, digitos e '-'
#               (ex.: www, google, meu-site, ufal)
#   - extensao: apenas letras, com pelo menos 2 (ex.: com, br, org, edu)
#   - pelo menos um ponto; aceita subdominios (www.google.com) e extensoes
#     de varios niveis (google.com.br)
#   - protocolo em letras minusculas
#
# M = (Q, Sigma, delta, q0, F)   com   F = {q12}
# Estado de erro (armadilha): qe. Toda transicao nao listada leva a qe.

LETRAS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITOS = set("0123456789")
ALFANUMERICOS = LETRAS | DIGITOS
SIGMA = ALFANUMERICOS | {".", ":", "/", "-"}

ESTADO_INICIAL = "q0"
ESTADOS_FINAIS = {"q12"}
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
}

# Apos um ponto, a extensao precisa ter so letras (>= 2):
# q10 (apos o ponto) --letra--> q11 (1 letra) --letra--> q12 (2+ letras)
APOS_LETRA = {"q10": "q11", "q11": "q12", "q12": "q12"}

# Estados em que letra/digito (nao tratado acima) leva a q9 (rotulo em andamento)
ESTADOS_ROTULO = {"q0", "q1", "q2", "q3", "q4", "q5", "q8", "q9"}

# Estados em que o '-' leva a q9 (hifen so dentro do rotulo, nunca no inicio)
ESTADOS_HIFEN = {"q1", "q2", "q3", "q4", "q5", "q9", "q11", "q12"}

# Estados em que o '.' leva a q10 (inicio de um novo rotulo)
ESTADOS_PONTO = {"q1", "q2", "q3", "q4", "q5", "q9", "q11", "q12"}


def delta(estado: str, simbolo: str) -> str:
    """Funcao de transicao delta: Q x Sigma -> Q (total, com estado de erro)."""
    if estado == ESTADO_ERRO:
        return ESTADO_ERRO
    if (estado, simbolo) in TRANSICOES:
        return TRANSICOES[(estado, simbolo)]
    if estado in APOS_LETRA:                       # q10, q11, q12
        if simbolo in LETRAS:
            return APOS_LETRA[estado]
        if simbolo in DIGITOS:
            return "q9"
    if simbolo in ALFANUMERICOS and estado in ESTADOS_ROTULO:
        return "q9"
    if simbolo == "-" and estado in ESTADOS_HIFEN:
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
        "www.google.com",
        "https://www.ufal.edu.br",
        "http://meu-site.com.br",
        "google",
        "http://.com",
    ]
    for url in exemplos:
        resultado = "VALIDA" if validar_url(url, verbose=True) else "INVALIDA"
        print(f"  {url!r}: {resultado}\n")