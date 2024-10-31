class TelaAluno():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- ALUNOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Aluno")
    print("2 - Alterar Aluno")
    print("3 - Listar Alunos")
    print("4 - Excluir Aluno")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_aluno(self):
    print("-------- DADOS ALUNO ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    nome_pais = input("Nome dos pais: ")

    return {"nome": nome, "telefone": telefone, "Nome dos pais": nome_pais}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_aluno(self, dados_aluno):
    print("NOME DO ALUNO: ", dados_aluno["nome"])
    print("FONE DO ALUNO: ", dados_aluno["telefone"])
    print("PAIS DO ALUNO: ", dados_aluno["nome_pais"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_aluno(self):
    matricula = input("Matrícula do aluno que deseja selecionar ")
    return matricula

  def mostra_mensagem(self, msg):
    print(msg)