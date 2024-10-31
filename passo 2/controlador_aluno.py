from tela_aluno import TelaAluno

class ControladorAlunos():

  def __init__(self, controlador_sistema):
    self.__alunos = []
    self.__tela_aluno = TelaAluno()
    self.__controlador_sistema = controlador_sistema

  def pega_aluno_por_matricula(self, matricula: int):
    for aluno in self.__alunos:
      if(aluno.matricula == matricula):
        return aluno
    return None

  def incluir_aluno(self):
    dados_aluno = self.__tela_aluno.pega_dados_aluno()
    aluno = Aluno(dados_aluno["nome"], dados_aluno["telefone"], dados_aluno["cpf"])
    self.__alunos.append(aluno)

  def alterar_aluno(self):
    self.lista_alunos()
    matricula_aluno = self.__tela_amigo.seleciona_aluno()
    aluno = self.pega_aluno_por_matricula(matricula_aluno)

    if(aluno is not None):
      novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
      aluno.nome = novos_dados_aluno["nome"]
      aluno.telefone = novos_dados_aluno["telefone"]
      aluno.matricula = novos_dados_aluno["matricula"]
      self.lista_alunos()
    else:
      self.__tela_aluno.mostra_mensagem("ATENCAO: Aluno não existente")


  def lista_alunos(self):
    for aluno in self.__alunos:
      self.__tela_aluno.mostra_aluno({"nome": aluno.nome, "telefone": aluno.telefone, "matricula": aluno.matricula})

  def excluir_aluno(self):
    self.lista_alunos()
    matricula_aluno = self.__tela_aluno.seleciona_aluno()
    aluno = self.pega_aluno_por_matricula(matricula_aluno)

    if(aluno is not None):
      self.__alunos.remove(aluno)
      self.lista_alunos()
    else:
      self.__tela_aluno.mostra_mensagem("ATENCAO: Aluno não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.lista_alunos, 4: self.excluir_aluno, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_aluno.tela_opcoes()]()