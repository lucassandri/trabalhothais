from controladores.controlador_aluno import ControladorAlunos
from controladores.controllerProfessor import ControladorProfessor
from controladores.controllerFuncionario import ControladorFuncionarios
class Financas:
    def faturamento_escola():
        faturamento = 0
        for aluno in ControladorAlunos.alunos():
            faturamento += aluno.mensalidade
        return faturamento
    
    def despesa_escola():
        despesa = 0
        for professor in ControladorProfessor.professores():
            despesa += professor.salario
        for funcionario in ControladorFuncionarios.lista_funcionarios:
            despesa += funcionario.salario
        return despesa

    
    def lucro_escola(self):
        lucro = self.faturamento_escola() - self.despesa_escola()
        return lucro