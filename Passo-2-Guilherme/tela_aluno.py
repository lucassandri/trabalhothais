from tela_abstrata import TelaAbstrata

class TelaAluno(TelaAbstrata):

  def __init__(self):
    pass
    
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- ALUNOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Aluno")
    print("2 - Alterar Aluno")
    print("3 - Listar Alunos")
    print("4 - Excluir Aluno")
    print("5 - Cadastrar Notas de um Período")
    print("6 - Mostrar aluno por matricula")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_aluno(self):
    print("-------- DADOS ALUNO ----------")
    nome = str(input("Nome: "))
    matricula = int(input("Matrícula: "))
    pais = str(input("Pais do aluno: "))
    serie = str(input("Série do aluno: "))
    mensalidade = float(input("Mensalidade do aluno "))
    bolsa = input("Aluno bolsista? (True ou False) ")
  
    if isinstance(bolsa, bool):
      return {"nome": nome, "matricula": matricula, "pais": pais, "serie": serie, "mensalidade": mensalidade, "bolsa": bolsa}

  def pega_matricula_aluno(self):
    print("-------- DADOS ALUNO ----------")
    nome = str(input("Nome: "))
    matricula = int(input("Matrícula: "))

  def pega_dados_boletim(self):
    print("-------- DADOS BOLETIM ----------")
    notas = [float(x) for x in input("Notas(separadas por espaço): ").split()]
    frequencia_suficiente = input("Frequencia Suficiente? (True ou False)")

    return {"notas": notas, "frequencia_suficiente": frequencia_suficiente}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  
  def mostra_aluno(self, dados_aluno):
    chaves_necessarias = ["nome", "matricula", "pais", "serie", "mensalidade", "bolsa", "media_ultimo_boletim"]
    for chave in chaves_necessarias:
        if chave not in dados_aluno:
            print(f"Erro: Falta informação para a chave '{chave}'")
            return
        
    print("NOME DO ALUNO: ", dados_aluno["nome"])
    print("MATRICULA DO ALUNO: ", dados_aluno["matricula"])
    print("PAIS DO ALUNO: ", dados_aluno["pais"])
    print("SERIE: ", dados_aluno["serie"])
    print("MENSALIDADE: ", dados_aluno["mensalidade"])
    print("BOLSA ", dados_aluno["bolsa"])
    print("ULTIMO BOLETIM ", dados_aluno["media_ultimo_boletim"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_aluno(self):
    matricula = input("Matrícula do aluno que deseja selecionar ")
    return matricula

  def mostra_mensagem(self, msg):
    print(msg)