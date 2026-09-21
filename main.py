# Importa a biblioteca JSON para salvar e carregar os dados em arquivo.
import json

# Lista principal que armazenará todos os alunos cadastrados.
# Cada aluno será um dicionário no formato: {"nome": "Maria", "nota": 9.5}
alunos = []

# Função para buscar um aluno na lista pelo nome.
def buscar_alunos():
    # Pede o nome do aluno e converte para minúsculas para comparar sem diferenciar maiúsculas/minúsculas.
    aluno = input("Nome do aluno?").strip().lower()

    # Variável para controlar se o aluno foi encontrado.
    encontrado = False

    # Percorre todos os alunos cadastrados.
    for item in alunos:
        nome = item["nome"]
        nota = item["nota"]

        # Se o nome digitado for igual ao nome do aluno atual, mostra a nota.
        if aluno == nome.lower():
            print(f"{nome} está na lista, sua nota é {nota}")
            encontrado = True
            break

    # Se o aluno não foi encontrado após percorrer a lista inteira, mostra a mensagem.
    if not encontrado:
        print("Esse aluno não está na lista")

# Função responsável por salvar a lista de alunos no arquivo "alunos.json".
def salvar_alunos():
    # Abre o arquivo em modo de escrita para sobrescrever os dados antigos.
    # O bloco with garante que o arquivo será fechado automaticamente ao final.
    with open("alunos.json", "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, indent=4)

# Função para cadastrar um novo aluno.
def cadastro_aluno():
    # Solicita o nome do aluno ao usuário.
    nome = input("Qual o nome do aluno? ")

    # Solicita a nota e converte para número decimal.
    nota = float(input("Qual a nota do aluno? "))

    # Cria um dicionário com os dados do aluno.
    aluno = {
        "nome": nome,
        "nota": nota,
    }

    # Adiciona o aluno à lista principal.
    alunos.append(aluno)

    # Salva os dados no arquivo após o cadastro.
    salvar_alunos()

    # Mensagem de confirmação para o usuário.
    print(f"Aluno '{nome}' cadastrado com sucesso!")

# Função para carregar os alunos já salvos no arquivo ao iniciar o programa.
def abrir_lista():
    # Tenta abrir o arquivo de dados.
    # Se o arquivo não existir, ignora o erro e continua o programa.
    try:
        with open("alunos.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            # Só aceita a leitura se o conteúdo for uma lista.
            if isinstance(dados, list):
                alunos.extend(dados)
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existir ou estiver vazio/inválido, o programa continua sem quebrar.
        pass

# Função para calcular a média das notas dos alunos cadastrados.
def calcular_media():
    soma = 0
    total = len(alunos)

    if total != 0:
        # Soma todas as notas da lista.
        for item in alunos:
            soma += item["nota"]

        media = soma / total
        print(f"A média dos alunos é {media}")
    else:
        print("Estamos sem notas cadastradas!")

# Função para listar todos os alunos e suas notas.
def listar_alunos():
    for item in alunos:
        nome = item["nome"]
        nota = item["nota"]
        print(f"Aluno {nome}, Nota: {nota}\n")

# Exibe o menu principal do sistema.
def exibir_menu():
    print("\nMenu:")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Calcular média")
    print("4 - Buscar aluno")
    print("5 - Sair")

# Função principal que mantém o programa em execução.
def main():
    # Carrega os dados salvos quando o programa inicia.
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
            buscar_alunos()
        elif opcao == "5":
            print("Saindo do sistema")
            break
        else:
            print("Opção inválida! Tente novamente")

# Garante que o programa só execute a função main quando o arquivo for executado diretamente.
if __name__ == "__main__":
    main()