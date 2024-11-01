from tela_financas import TelaFinancas
from controlador_abstrato import ControladorAbstrato


class ControladorFinancas(ControladorAbstrato):
    
    def __init__(self, controlador_sistema, controlador_aluno, controlador_professor, controlador_funcionario):
        super().__init__(controlador_sistema)
        self.__controlador_aluno = controlador_aluno
        self.__controlador_professor = controlador_professor
        self.__controlador_funcionario = controlador_funcionario
        self.__tela_financas = TelaFinancas()