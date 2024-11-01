from entidades.sistema import *
from controladores.controllerProfessor import ControladorProfessor
class ControllerFinancas:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_professor = ControladorProfessor()
        pass
    
    def faturamento_escola():
        faturamento = 0
        for aluno in Sistema.lista_alunos:
            faturamento += aluno.mensalidade
        return faturamento
    
    def despesa_escola(self):
        despesa = 0
        for professor in self.__controlador_professor.professores:
            despesa += professor.salario
        for funcionario in Sistema.lista_funcionarios:
            despesa += funcionario.salario
        return despesa

    
    def lucro_escola(self):
        lucro = self.faturamento_escola() - self.despesa_escola()
        return lucro
    

    def retornar(self):
        self.__controlador_sistema.abre_tela()
        
    def abre_tela(self):
        lista_opcoes = {1: self.ver_faturamento, 2: self.ver_despesas, 3: self.ver_lucro, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()