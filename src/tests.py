
from input_handler import limpar_entrada, validar_alfabeto_inicial
from validator_ip import processar_ip
from validator_url import validar_url


def executar_testes():

    testes_handler = [
        ("  192.168.0.1  ", "192.168.0.1", "limpeza"),
        ("  https://google.com  ", "https://google.com", "limpeza"),
        ("192.168.0.1", True, "ip"),
        ("192.168.0.a", False, "ip"),
        ("https://google.com", True, "url"),
        ("https://google.com?x=1", False, "url"),
    ]

    testes_ip = [
        ("192.168.0.1", True),
        ("10.0.0.255", True),
        ("127.0.0.1", True),
        ("172.16.254.1", True),
        ("0.0.0.0", True),
        ("256.100.0.1", False),
        ("192.168..1", False),
        ("192.168.0.01", False),
        ("192.168.0", False),
        ("abc.def.ghi.jkl", False),
        ("", False),
    ]

    testes_url = [
        ("google.com", True),
        ("http://google.com", True),
        ("https://ufal.br", True),
        ("https://github.com", True),
        ("http://example.br", True),
        ("google.org", False),
        ("http://.com", False),
        ("https://", False),
        ("HTTP://google.com", False),
        ("google", False),
        ("", False),
    ]

    aprovados = 0
    total = 0

    def registrar_teste(descricao, esperado, obtido):
        nonlocal aprovados, total

        passou = esperado == obtido
        total += 1

        if passou:
            aprovados += 1

        print(f"\nTeste: {descricao}")
        print(f"Esperado: {esperado}")
        print(f"Obtido: {obtido}")
        print(f"Resultado: {'PASSOU' if passou else 'FALHOU'}")

    print("\n========== TESTES DO INPUT HANDLER ==========")

    for entrada, esperado, tipo in testes_handler:

        if tipo == "limpeza":
            obtido = limpar_entrada(entrada)

        else:
            obtido = validar_alfabeto_inicial(entrada, tipo)

        registrar_teste(
            f"Handler - {entrada!r}",
            esperado,
            obtido
        )

    print("\n========== TESTES DO VALIDADOR DE IP ==========")

    for entrada, esperado in testes_ip:
        obtido = processar_ip(entrada)

        registrar_teste(
            f"IP - {entrada!r}",
            esperado,
            obtido
        )

    print("\n========== TESTES DO VALIDADOR DE URL ==========")

    for entrada, esperado in testes_url:
        obtido = validar_url(entrada)

        registrar_teste(
            f"URL - {entrada!r}",
            esperado,
            obtido
        )

    reprovados = total - aprovados

    print("\n========== RESUMO FINAL ==========")
    print(f"Total de testes: {total}")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {reprovados}")

    if reprovados == 0:
        print("\nTODOS OS TESTES FORAM APROVADOS!")
    else:
        print("\nEXISTEM TESTES QUE PRECISAM SER REVISADOS.")


if __name__ == "__main__":
    executar_testes()
