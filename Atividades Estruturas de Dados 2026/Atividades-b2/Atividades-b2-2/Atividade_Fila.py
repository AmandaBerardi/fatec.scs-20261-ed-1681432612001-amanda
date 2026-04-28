from collections import deque

class Arquivo:
    def __init__(self, nome, paginas):
        self.nome = nome
        self.paginas = paginas

    def __repr__(self):
        return f"{self.nome} ({self.paginas} págs)"


fila_adm = deque()
fila_alunos = deque()
fila_processamento = deque()


def adicionar_arquivo():
    tipo = input("Escolha a fila (1 - ADM | 2 - Aluno): ")

    nome = input("Nome do arquivo: ")
    paginas = int(input("Número de páginas: "))

    if tipo == "1":
        fila_adm.append(Arquivo(nome, paginas))
        print("Arquivo adicionado na fila ADM.\n")
    elif tipo == "2":
        fila_alunos.append(Arquivo(nome, paginas))
        print("Arquivo adicionado na fila de Alunos.\n")
    else:
        print("Opção inválida.\n")


def reorganizar_filas():
    if fila_processamento:
        print("Fila de processamento não está vazia.\n")
        return

    while fila_adm:
        fila_processamento.append(fila_adm.popleft())

    while fila_alunos:
        fila_processamento.append(fila_alunos.popleft())

    print("Filas reorganizadas com sucesso.\n")


def listar_fila():
    print("\nFila de Processamento:")
    print(list(fila_processamento))
    print()


def consumir_fila():
    if not fila_processamento:
        print("Nenhum arquivo para imprimir.\n")
        return

    arquivo = fila_processamento.popleft()
    print(f"Para impressão: {arquivo}\n")


while True:
    print("1 - Adicionar arquivo")
    print("2 - Reorganizar filas")
    print("3 - Listar fila de processamento")
    print("4 - Consumir (imprimir)")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_arquivo()
    elif opcao == "2":
        reorganizar_filas()
    elif opcao == "3":
        listar_fila()
    elif opcao == "4":
        consumir_fila()
    elif opcao == "5":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida.\n")