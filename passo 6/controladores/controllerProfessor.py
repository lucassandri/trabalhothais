from entidades.professor import Professor
from view.tela_professor import TelaProfessor

class ControladorProfessor():

  def __init__(self, controlador_sistema):
    self.__professores = []
    self.__tela_professor = TelaProfessor()
    self.__controlador_sistema = controlador_sistema

  @property
  def professores(self):
    return self.__professores

  def pega_professor_por_nome(self, nome: str):
    for professor in self.__professores:
      if(professor.nome == nome):
        return professor
    return None

  def incluir_professor(self):
    dados_professor = self.__tela_professor.pega_dados_professor()
    professor = Professor(dados_professor["nome"], dados_professor["salario"], dados_professor["leciona"], dados_professor["email"])
    self.__professores.append(professor)

  def alterar_professor(self):
    nome_professor = self.__tela_professor.seleciona_professor()
    professor = self.pega_professor_por_nome(nome_professor)

    if (professor is not None):
      novos_dados_professor = self.__tela_professor.pega_dados_professor()
      professor.nome = novos_dados_professor["nome"]
      professor.salario = novos_dados_professor["telefone"]
      professor.leciona = novos_dados_professor["leciona"]
      professor.email = novos_dados_professor["email"]
    else:
      self.__tela_professor.mostra_mensagem("ATENCAO: Professor não existente")


  def lista_professores(self):
    for professor in self.__professores:
      self.__tela_professor.mostra_professor({"nome": professor.nome, "telefone": professor.telefone, "leciona": professor.leciona, "email": professor.email})

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
    lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.lista_alunos, 4: self.excluir_aluno, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_aluno.tela_opcoes()]()