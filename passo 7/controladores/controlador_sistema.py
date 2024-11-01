import controlador_aluno
import controlador_funcionario
import controlador_professor
from telas.tela_sistema import TelaSistema
from entidades.sistema import Sistema
from controlador_abstrato import ControladorAbstrato
from controlador_aluno import ControladorAluno
from controlador_financas import ControladorFinancas
from controlador_funcionario import ControladorFuncionario
from controlador_professor import ControladorProfessor

class ControladorSistema(ControladorAbstrato):

    def __init__(self):
        self.__sistema = Sistema()
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_professor = ControladorProfessor(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_financas = ControladorFinancas(self, controlador_aluno, controlador_professor, controlador_funcionario)
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
        print('Encerrada a execução do sistema!')
        exit()

    def abre_tela(self):
        lista_opcoes = {1: self.alunos, 2: self.financas, 3: self.funcionarios, 4: self.professores, 0: self.encerra_sistema}
        continua = True
        while continua:
            lista_opcoes[self.__tela_sistema.tela_opcoes()]()
