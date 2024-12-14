from telas.tela_sistema import TelaSistema
from entidades.sistema import Sistema
from controladores.controlador_abstrato import ControladorAbstrato
from controladores.controlador_aluno import ControladorAluno
from controladores.controlador_financas import ControladorFinancas
from controladores.controlador_funcionario import ControladorFuncionario
from controladores.controlador_professor import ControladorProfessor
from controladores.controlador_turma import ControladorTurma

class ControladorSistema(ControladorAbstrato):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__sistema = Sistema()
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_professor = ControladorProfessor(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_financas = ControladorFinancas(self)
        self.__controlador_turma = ControladorTurma(self)
        self.__tela_sistema = TelaSistema()
    
    @property
    def sistema(self):
        return self.__sistema
    
    @property
    def controlador_financas(self):
        return self.__controlador_financas
    
    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario
    
    @property
    def controlador_aluno(self):
        return self.__controlador_aluno

    @property
    def controlador_professor(self):
        return self.__controlador_professor
    
    @property
    def controlador_turma(self):
        return self.__controlador_turma

    def inicializa_sistema(self):
        self.abre_tela()

    def alunos(self):
        self.__controlador_aluno.abre_tela()

    def funcionarios(self):
        self.__controlador_funcionario.abre_tela()

    def professores(self):
        self.__controlador_professor.abre_tela()

    def financas(self):
        self.__controlador_financas.abre_tela()

    def encerra_sistema(self):
        self.__tela_sistema.mostra_mensagem('Encerrada a execução do sistema!')
        exit()

    def abre_tela(self):
        lista_opcoes = {1: self.alunos, 2: self.financas, 3: self.funcionarios, 4: self.professores, 0: self.encerra_sistema}
        continua = True
        while continua:
            lista_opcoes[self.__tela_sistema.tela_opcoes()]()
