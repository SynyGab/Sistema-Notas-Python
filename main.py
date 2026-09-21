# Lista principal que guarda os alunos cadastrados.
# Cada aluno é armazenado como um dicionário dentro da lista.
alunos = []

# Salva os alunos em um arquivo de texto, usando o formato nome,nota.
# O código atual grava os dados em "alunos.json".
def salvar_alunos():
    # Abre o arquivo em modo de escrita para sobrescrever os dados antigos.
    # O bloco with garante que o arquivo será fechado ao final.
    with open("alunos.json", "w") as arquivo:
        json.dump(alunos,arquivo,indent=4)

# Solicita os dados do aluno e adiciona à lista.
def cadastro_aluno():
    # Pede o nome do aluno ao usuário.
    nome = input("Qual o nome do aluno?")
    # Pede a nota e converte o valor para número decimal.
    nota = float(input("Qual a nota do aluno?"))

    # Cria um dicionário com nome e nota.
    aluno = {
        "nome": nome,
        "nota": nota,
    }

    # Adiciona o aluno à lista principal.
    alunos.append(aluno)

    # Salva a lista no arquivo após o cadastro.
    salvar_alunos()

    # Exibe uma mensagem de confirmação.
    print(f"Aluno '{nome}' cadastrado com sucesso!")

# Tenta carregar os alunos já salvos no arquivo ao iniciar o programa.
# A leitura é feita usando o arquivo "alunos.json" e o formato nome,nota.
def abrir_lista():
    # Tenta abrir o arquivo para leitura.
    # Se ele não existir, o programa ignora o erro sem encerrar.
    try:
        with open("alunos.json","r") as arquivo:
            # Lê linha por linha do arquivo.
            for linha in arquivo:
                # Divide cada linha em nome e nota usando a vírgula como separador.
                dados = linha.split(",")
                # Pega o nome e remove espaços extras.
                nome = dados[0].strip()
                # Pega a nota e converte para float.
                nota = float(dados[1].strip())

                # Cria um dicionário com os dados lidos.
                aluno = {
                    "nome": nome,
                    "nota": nota,
                }

                # Adiciona o aluno à lista principal.
                alunos.append(aluno)
    except FileNotFoundError:
        pass


# Calcula a média das notas dos alunos cadastrados.
def calcular_media():
    soma = 0
    total = len(alunos)
    if total != 0:
        for item in alunos:
            nota = item["nota"]
            soma += nota
        media = soma / total
        print(f"A média dos alunos é {media}")
    else:
        print("Estamos sem notas cadastradas!")

# Lista todos os alunos e suas notas.
def listar_alunos():
    for item in alunos:
        nome = item["nome"]
        nota = item["nota"]
        print(f"Aluno {nome}, Nota: {nota}\n")

# Exibe as opções do menu principal do programa.
def exibir_menu():
    print("\nMenu:")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Calcular média")
    print("4 - Sair")

# Função principal. Inicia o programa e mantém o menu em execução.
def main():
    # Carrega os alunos salvos antes de abrir o menu principal.
    abrir_lista()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            calcular_media()
        elif opcao == "4":
            print("Saindo do sistema")
            exit()
        else:
            print("Opção inválida! Tente novamente")

if __name__ == "__main__":
    main()