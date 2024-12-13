from daos.dao import DAO
from entidades.turma import Turma

class TurmaDAO(DAO):
    def __init__(self):
        super().__init__('turmas.pkl')

    def add(self, turma):
        if(turma is not None) and isinstance(turma, Turma):
            super().add(turma.nome, turma)

    def update(self, turma):
        if(turma is not None) and isinstance(turma, Turma):
            super().update(turma.nome, turma)

    def get(self, key):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key):
        if(isinstance(key, str)):
            return super().remove(key)