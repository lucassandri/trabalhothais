from entidades.aluno import Aluno
from view.tela_aluno import TelaAluno

class ControladorAlunos():

  def __init__(self, controlador_sistema):
    self.__alunos = []
    self.__tela_aluno = TelaAluno()
    self.__controlador_sistema = controlador_sistema

  def cadastrar_notas_periodo(self):
    matricula_aluno = self.__tela_aluno.seleciona_aluno()
    aluno = self.pega_aluno_por_matricula(matricula_aluno)
    notas = self.__tela_aluno.pega_dados_boletim()
    aluno.boletim.append(notas)

  def mostra_aluno_por_matricula(self):
    matricula_aluno = self.__tela_aluno.seleciona_aluno()
    aluno = self.pega_aluno_por_matricula(matricula_aluno)
    self.__tela_aluno.mostra_aluno({"nome": aluno.nome, "matricula": aluno.matricula, "pais": aluno.pais, "serie": aluno.serie, "mensalidade": aluno.mensalidade, "bolsa": aluno.bolsa, "media_ultimo_boletim": aluno.media_ultimo_boletim()})

  def incluir_aluno(self):
    dados_aluno = self.__tela_aluno.pega_dados_aluno()
    aluno = Aluno(dados_aluno["nome"], dados_aluno["matricula"], dados_aluno["pais"], dados_aluno["serie"], dados_aluno["bolsa"], dados_aluno["mensalidade"])
    self.__alunos.append(aluno)

  def pega_aluno_por_matricula(self, matricula_aluno):
    for aluno in self.__alunos:
      if matricula_aluno == aluno.matricula:
        return aluno
      else:
        return None

  def alterar_aluno(self):
    matricula_aluno = self.__tela_aluno.seleciona_aluno()
    aluno = self.pega_aluno_por_matricula(matricula_aluno)

    if (aluno is not None):
      novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
      aluno.nome = novos_dados_aluno["nome"]
      aluno.matricula = novos_dados_aluno["matricula"]
      aluno.pais = novos_dados_aluno["pais"]
      aluno.serie = novos_dados_aluno["serie"]
      aluno.bolsa = novos_dados_aluno["bolsa"]
      aluno.mensalidade = novos_dados_aluno["mensalidade"]
    else:
      self.__tela_aluno.mostra_mensagem("ATENCAO: Aluno não existente")


  def lista_alunos(self):
    for aluno in self.__alunos:
      self.__tela_aluno.mostra_aluno({"nome": aluno.nome, "matricula": aluno.matricula, "pais": aluno.pais, "serie": aluno.serie, "mensalidade": aluno.mensalidade, "bolsa": aluno.bolsa, "media_ultimo_boletim": aluno.media_ultimo_boletim()})

  def excluir_aluno(self):
    matricula_aluno = self.__tela_aluno.seleciona_aluno()
    aluno = self.pega_aluno_por_matricula(matricula_aluno)

    if(aluno is not None):
      self.__alunos.remove(aluno)
    else:
      self.__tela_aluno.mostra_mensagem("ATENCAO: Aluno não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.lista_alunos, 4: self.excluir_aluno, 5: self.cadastrar_notas_periodo, 6: self.mostra_aluno_por_matricula, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_aluno.tela_opcoes()]()