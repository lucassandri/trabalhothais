from abc import ABC, abstractmethod

from aluno import Aluno
from funcionario import Funcionario
from professor import Professor

lista_alunos = []
lista_funcionarios = []
lista_professores = []
lista_boletins = []
lista_alunos_com_boletins = {}
class Sistema(ABC):
    @abstractmethod
    def __init__(self, aluno: 'Aluno', funcionario: 'Funcionario', professor: 'Professor'):
        self.__aluno = aluno
        self.__funcionario = funcionario
        self.__professor = professor
        

    @staticmethod
    def cadastrar_professor(professor: Professor):
        if isinstance(professor, Professor) and professor not in lista_professores:
            lista_professores.append(professor)

    


    @staticmethod
    def excluir_professor(professor: Professor):
        if isinstance(professor, Professor) and professor in lista_professores:
            lista_professores.remove(professor)
            del professor

    @staticmethod
    def cadastrar_funcionario(funcionario: Funcionario):
        if isinstance(funcionario, Funcionario) and funcionario not in lista_funcionarios:
            lista_funcionarios.append(funcionario)

    @staticmethod
    def excluir_funcionario(funcionario: Funcionario):
        if isinstance(funcionario, Funcionario) and funcionario in lista_funcionarios:
            lista_funcionarios.remove(funcionario)
            del funcionario

    @staticmethod
    def media_serie(serie):
        notas = 0
        contador = 0
        for aluno in lista_alunos:
            if aluno.serie == serie:
                notas += aluno.boletim.media_final()
                contador += 1
        if contador > 0:
            media = notas / contador
            return media
        return 0

    @staticmethod
    def alunos_serie(serie):
        contador = 0
        for aluno in lista_alunos:
            if aluno.serie == serie:
                contador += 1
        return contador

    @staticmethod
    def lista_professores_por_materia(materia):
        professor_por_materia = []
        for professor in lista_professores:
            if professor.leciona == materia:
                professor_por_materia.append(professor)
        return professor_por_materia

    @staticmethod
    def porcentagem_alunos_aprovados():
        contador_aprovados = 0
        total_alunos = len(lista_alunos)
        for aluno in lista_alunos:
            if aluno.boletim.aprovado():
                contador_aprovados += 1
        if total_alunos > 0:
            return contador_aprovados / total_alunos * 100
        return 0



    @staticmethod
    def porcentagem_alunos_reprovados():
        contador_reprovados = 0
        total_alunos = len(lista_alunos)
        for aluno in lista_alunos:
            if not aluno.boletim.aprovado():
                contador_reprovados += 1
        if total_alunos > 0:
            return contador_reprovados / total_alunos * 100
        return 0

    @staticmethod
    def relacao_salario_funcionario():
        soma_salarios = 0
        numero_funcionarios = 0
        for professor in lista_professores:
            soma_salarios += professor.salario
            numero_funcionarios += 1
        for funcionario in lista_funcionarios:
            soma_salarios += funcionario.salario
            numero_funcionarios += 1
        if numero_funcionarios > 0:
            return soma_salarios / numero_funcionarios
        return 0

    @staticmethod
    def porcentagem_alunos_bolsistas():
        contador_bolsistas = 0
        total_alunos = len(lista_alunos)
        for aluno in lista_alunos:
            if aluno.bolsa:
                contador_bolsistas += 1
        if total_alunos > 0:
            return contador_bolsistas / total_alunos * 100
        return 0

    @staticmethod
    def porcentagem_alunos_nao_bolsistas():
        contador_nao_bolsistas = 0
        total_alunos = len(lista_alunos)
        for aluno in lista_alunos:
            if not aluno.bolsa:
                contador_nao_bolsistas += 1
        if total_alunos > 0:
            return contador_nao_bolsistas / total_alunos * 100
        return 0