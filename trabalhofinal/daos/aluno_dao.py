from daos.dao import DAO
from entidades.aluno import Aluno

class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, aluno):
        if(aluno is not None) and isinstance(aluno, Aluno):
            super().add(aluno.matricula, aluno)

    def update(self, aluno):
        if(aluno is not None) and isinstance(aluno, Aluno):
            super().update(aluno.matricula, aluno)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
