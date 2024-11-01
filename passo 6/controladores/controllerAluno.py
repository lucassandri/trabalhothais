from entidades.aluno import Aluno
from entidades.boletim import Boletim
from entidades.sistema import *

class AlunoController:
    
    def cadastrar_aluno(aluno: Aluno):
        if isinstance(aluno, Aluno) and aluno not in lista_alunos:
            lista_alunos.append(aluno)
            lista_alunos_com_boletins[aluno] = []
        

    def cadastrar_boletim(aluno: Aluno, notas: list, frequencia_suficiente: bool):
        boletim = Boletim(notas, frequencia_suficiente)
        lista_alunos_com_boletins[aluno].append(boletim)


    def excluir_aluno(aluno: Aluno):
        if isinstance(aluno, Aluno) and aluno in lista_alunos:
            lista_alunos.remove(aluno)
            del aluno