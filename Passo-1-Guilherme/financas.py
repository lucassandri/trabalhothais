from controlador_aluno import ControladorAluno
from controlador_professor import ControladorProfessor
from controlador_funcionario import ControladorFuncionario

class Financas():

    def __init__(self):
        pass

    def faturamento_escola(self):
        faturamento = 0
        for aluno in ControladorAluno.alunos():
            faturamento += aluno.mensalidade
        return faturamento
    
    def despesa_escola(self):
        despesa = 0
        for professor in ControladorProfessor.professores():
            despesa += professor.salario
        for funcionario in ControladorFuncionario.lista_funcionarios:
            despesa += funcionario.salario
        return despesa

    
    def lucro_escola(self):
        lucro = self.faturamento_escola() - self.despesa_escola()
        return lucro