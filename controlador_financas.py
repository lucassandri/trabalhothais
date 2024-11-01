from tela_financas import TelaFinancas
from controlador_abstrato import ControladorAbstrato


class ControladorFinancas(ControladorAbstrato):
    
    def __init__(self, controlador_sistema, controlador_aluno, controlador_professor, controlador_funcionario):
        super().__init__(controlador_sistema)
        self.__controlador_aluno = controlador_aluno
        self.__controlador_professor = controlador_professor
        self.__controlador_funcionario = controlador_funcionario
        self.__tela_financas = TelaFinancas()
    
    def cadastrar_basicas(self):
        return 0
    
    def alterar_basicas(self):
        return 0
    
    def excluir_basicas(self):
        return 0
    
    def mostrar_trabalhadores(self):
        return 0
    
    def mostrar_basicas(self):
        return 0
    
    def mostrar_todas_despesas(self):
        return 0
    
    def mostrar_lucro(self):
        return 0
    
    def mostrar_faturamento(self):
        return 0
    
    def alunos_bolsistas(self):
        return 0

    def abre_tela(self):
            lista_opcoes = {1: self.cadastrar_basicas, 2: self.alterar_basicas, 3: self.excluir_basicas, 4: self.mostrar_trabalhadores, 5: self.mostrar_basicas, 6: self.mostrar_todas_despesas, 7: self.mostrar_lucro, 8: self.mostrar_faturamento, 9: self.alunos_bolsistas, 0: self.retornar}
            continua = True
            while continua:
                lista_opcoes[self.__tela_financas.tela_opcoes()]()
