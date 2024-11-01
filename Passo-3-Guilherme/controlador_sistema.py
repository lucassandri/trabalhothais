from tela_sistema import TelaSistema
from controlador_abstrato import ControladorAbstrato
from controlador_aluno import ControladorAluno
from controlador_financas import ControladorFinancas
from controlador_funcionario import ControladorFuncionario
from controlador_professor import ControladorProfessor

class ControladorSistema(ControladorAbstrato):

    def __init__(self):
        self.__controlador_aluno = ControladorAluno()
        self.__controlador_financas = ControladorFinancas()
        self.__controlador_funcionario = ControladorFuncionario()
        self.__controlador_professor = ControladorProfessor()
        self.__tela_sistema = TelaSistema()

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

    def cadastra_alunos(self):
        # Chama o controlador de Alunos
        self.__controlador_aluno.abre_tela()

    def cadastra_funcionarios(self):
        # Chama o controlador de Amigos
        self.__controlador_funcionario.abre_tela()

    def cadastra_professores(self):
        # Chama o controlador de Emprestimos
        self.__controlador_professor.abre_tela()

    def controla_financas(self):
        # Chama o controlador de Amigos
        self.__controlador_financas.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_alunos, 2: self.controla_financas, 3: self.cadastra_funcionarios, 4: self.cadastra_professores, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
