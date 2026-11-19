
from validator_ip import validar_ip
from validator_url import validar_url



def testar_ips():
    print("\n========== TESTES DE IP ==========")

    casos = [
        ("192.168.0.1", True),
        ("8.8.8.8", True),
        ("10.0.0.1", True),
        ("172.16.0.1", True),
        ("256.1.1.1", False),
        ("192.168.0", False),
        ("abc.def.ghi.jkl", False),
        ("192.168.1.999", False),
        ("192.168.1.1.1", False),
    ]

    for ip, esperado in casos:
        print(f"IP: {ip} | Resultado esperado: {'ACEITA' if esperado else 'REJEITA'}")


def testar_urls():
    print("\n========== TESTES DE URL ==========")

    casos = [
        ("https://www.google.com", True),
        ("http://example.com", True),
        ("https://github.com", True),
        ("google", False),
        ("htp://site.com", False),
        ("www.google.com", False),
        ("https://", False),
    ]

    for url, esperado in casos:
        print(f"URL: {url} | Resultado esperado: {'ACEITA' if esperado else 'REJEITA'}")


def executar_testes():
    testar_ips()
    testar_urls()


if __name__ == "__main__":
    executar_testes()
