from collections import deque




def criar_no(valor):
    return {"valor": valor, "esq": None, "dir": None}


def criar_arvore():
    return {"raiz": None}



def inserir(arvore, valor):
    if arvore["raiz"] is None:
        arvore["raiz"] = criar_no(valor)
    else:
        _inserir_rec(arvore["raiz"], valor)


def _inserir_rec(no, valor):
    if valor < no["valor"]:
        if no["esq"] is None:
            no["esq"] = criar_no(valor)
        else:
            _inserir_rec(no["esq"], valor)
    elif valor > no["valor"]:
        if no["dir"] is None:
            no["dir"] = criar_no(valor)
        else:
            _inserir_rec(no["dir"], valor)



def buscar(no, valor):
    if no is None:
        return None
    if no["valor"] == valor:
        return no
    if valor < no["valor"]:
        return buscar(no["esq"], valor)
    return buscar(no["dir"], valor)




def imprimir_nos_internos(arvore):
    internos = []
    _coletar_internos(arvore["raiz"], internos)
    print("Nós Internos:", internos)
    return internos


def _coletar_internos(no, lista):
    if no is None:
        return
    if no["esq"] is not None or no["dir"] is not None:
        lista.append(no["valor"])
    _coletar_internos(no["esq"], lista)
    _coletar_internos(no["dir"], lista)


def imprimir_folhas(arvore):
    folhas = []
    _coletar_folhas(arvore["raiz"], folhas)
    print("Nós Folhas (externos):", folhas)
    return folhas


def _coletar_folhas(no, lista):
    if no is None:
        return
    if no["esq"] is None and no["dir"] is None:
        lista.append(no["valor"])
    _coletar_folhas(no["esq"], lista)
    _coletar_folhas(no["dir"], lista)




def imprimir_niveis(arvore):
    if arvore["raiz"] is None:
        print("Árvore vazia.")
        return {}
    niveis = {}
    fila = deque([(arvore["raiz"], 0)])
    while fila:
        no, nivel = fila.popleft()
        niveis.setdefault(nivel, []).append(no["valor"])
        if no["esq"]:
            fila.append((no["esq"], nivel + 1))
        if no["dir"]:
            fila.append((no["dir"], nivel + 1))
    for nivel, nos in niveis.items():
        print(f"  Nível {nivel}: {nos}")
    return niveis




def calcular_altura(no):
    if no is None:
        return -1
    return 1 + max(calcular_altura(no["esq"]), calcular_altura(no["dir"]))


def calcular_profundidade(arvore, valor):
    return _profundidade_rec(arvore["raiz"], valor, 0)


def _profundidade_rec(no, valor, prof):
    if no is None:
        return -1
    if no["valor"] == valor:
        return prof
    if valor < no["valor"]:
        return _profundidade_rec(no["esq"], valor, prof + 1)
    return _profundidade_rec(no["dir"], valor, prof + 1)




def imprimir_ancestrais(arvore, valor):
    ancestrais = []
    _coletar_ancestrais(arvore["raiz"], valor, ancestrais)
    if ancestrais:
        print(f"Ancestrais de {valor}: {ancestrais}")
    else:
        print(f"Nó {valor} é a raiz ou não foi encontrado.")
    return ancestrais


def _coletar_ancestrais(no, valor, lista):
    if no is None:
        return False
    if no["valor"] == valor:
        return True
    lista.append(no["valor"])
    if (_coletar_ancestrais(no["esq"], valor, lista) or
            _coletar_ancestrais(no["dir"], valor, lista)):
        return True
    lista.pop()
    return False



def imprimir_descendentes(arvore, valor):
    alvo = buscar(arvore["raiz"], valor)
    if alvo is None:
        print(f"Nó {valor} não encontrado.")
        return []
    desc = []
    _coletar_descendentes(alvo["esq"], desc)
    _coletar_descendentes(alvo["dir"], desc)
    print(f"Descendentes de {valor}: {desc}")
    return desc


def _coletar_descendentes(no, lista):
    if no is None:
        return
    lista.append(no["valor"])
    _coletar_descendentes(no["esq"], lista)
    _coletar_descendentes(no["dir"], lista)



def grau_no(no):
    if no is None:
        return -1
    return (1 if no["esq"] else 0) + (1 if no["dir"] else 0)




def analisar_arvore(arvore, valor_busca):
    sep = "=" * 55

    print(sep)
    print("          DIAGNÓSTICO GERAL DA ÁRVORE BST")
    print(sep)

    raiz = arvore["raiz"]
    if raiz is None:
        print("\nÁrvore vazia!")
        return

    print(f"\n[Raiz] → valor: {raiz['valor']}  |  id: {id(raiz)}")

    print("\n[Nós Internos]")
    imprimir_nos_internos(arvore)

    print("\n[Nós Folhas / Externos]")
    imprimir_folhas(arvore)

    print("\n[Exibição por Níveis]")
    imprimir_niveis(arvore)

    print()
    print(sep)
    print(f"     DIAGNÓSTICO ESPECÍFICO — Nó buscado: {valor_busca}")
    print(sep)

    alvo = buscar(raiz, valor_busca)
    if alvo is None:
        print(f"\n  Nó com valor {valor_busca} não encontrado na árvore.")
        return

    print(f"\n[Grau do Nó {valor_busca}] → {grau_no(alvo)} filho(s)")

    print(f"\n[Ancestrais do Nó {valor_busca}]")
    imprimir_ancestrais(arvore, valor_busca)

    print(f"\n[Descendentes do Nó {valor_busca}]")
    imprimir_descendentes(arvore, valor_busca)

    altura = calcular_altura(alvo)
    prof   = calcular_profundidade(arvore, valor_busca)
    print(f"\n[Altura do Nó {valor_busca}]      → {altura}")
    print(f"[Profundidade do Nó {valor_busca}] → {prof}")
    print()



if __name__ == "__main__":
    arvore = criar_arvore()
    for v in [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]:
        inserir(arvore, v)

    analisar_arvore(arvore, valor_busca=30)
