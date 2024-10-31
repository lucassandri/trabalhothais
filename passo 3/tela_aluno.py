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
    nome = str(input("Nome: "))
    matricula = int(input("Matrícula: "))
    pais = str(input("Pais do aluno: "))
    serie = str(input("Série do aluno: "))
    mensalidade = float(input("Mensalidade do aluno "))
    bolsa = input("Aluno bolsista? (True ou False) ")

    if isinstance(bolsa, bool):
      return {"nome": nome, "matricula": matricula, "pais": pais, "serie": serie, "mensalidade": mensalidade, "bolsa": bolsa}

  def pega_dados_boletim(self):
    print("-------- DADOS BOLETIM ----------")
    notas = [float(x) for x in input().split()]
    frequencia_suficiente = input("Frequencia Suficiente? (True ou False)")

    return {"notas": notas, "frequencia_suficiente": frequencia_suficiente}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_aluno(self, dados_aluno):
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