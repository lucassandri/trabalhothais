from view.tela_sistema import TelaSistema
from controladores.controlador_aluno import ControladorAlunos
from controladores.controllerFinancas import ControllerFinancas
from controladores.controllerFuncionario import ControladorFuncionarios
from controladores.controllerProfessor import ControladorProfessor

class ControladorSistema:

    def __init__(self):
        self.__controlador_aluno = ControladorAlunos(self)
        self.__controlador_financas = ControllerFinancas(self)
        self.__controlador_funcionario = ControladorFuncionarios(self)
        self.__controlador_professor = ControladorProfessor(self)
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
