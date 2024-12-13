from daos.dao import DAO
from entidades.professor import Professor

class ProfessorDAO(DAO):
    def __init__(self):
        super().__init__('professores.pkl')

    def add(self, professor):
        if(professor is not None) and isinstance(professor, Professor):
            super().add(professor.email, professor)

    def update(self, professor):
        if(professor is not None) and isinstance(professor, Professor):
            super().update(professor.email, professor)

    def get(self, key):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key):
        if(isinstance(key, str)):
            return super().remove(key)
