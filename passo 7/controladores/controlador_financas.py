from telas.tela_financas import TelaFinancas
from entidades.financas import Financas
from controlador_abstrato import ControladorAbstrato


class ControladorFinancas(ControladorAbstrato):
    
    def __init__(self, controlador_sistema, controlador_aluno, controlador_professor, controlador_funcionario):
        super().__init__(controlador_sistema)
        self.__controlador_aluno = controlador_aluno
        self.__controlador_professor = controlador_professor
        self.__controlador_funcionario = controlador_funcionario
        self.__tela_financas = TelaFinancas()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_funcionario, 2: self.alterar_funcionario, 3: self.excluir_funcionario, 4: self.lista_funcionarios, 5: self.achar_funcionario, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_financas.tela_opcoes()]()