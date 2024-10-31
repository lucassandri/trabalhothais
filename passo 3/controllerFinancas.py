from sistema import *
class ControllerFinancas:
    
    def faturamento_escola():
        faturamento = 0
        for aluno in Sistema.lista_alunos:
            faturamento += aluno.mensalidade
        return faturamento
    
    def despesa_escola():
        despesa = 0
        for professor in Sistema.lista_professores:
            despesa += professor.salario
        for funcionario in Sistema.lista_funcionarios:
            despesa += funcionario.salario
        return despesa

    
    def lucro_escola(self):
        lucro = self.faturamento_escola() - self.despesa_escola()
        return lucro