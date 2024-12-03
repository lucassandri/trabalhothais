from daos.dao import DAO
from entidades.funcionario import Funcionario

class FuncionarioDAO(DAO):
    def __init__(self):
        super().__init__('funcionarios.pkl')

    def add(self, funcionario):
        if(funcionario is not None) and isinstance(funcionario, Funcionario):
            super().add(funcionario.email, funcionario)

    def update(self, funcionario):
        if(funcionario is not None) and isinstance(funcionario, Funcionario):
            super().update(funcionario.email, funcionario)

    def get(self, key):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key):
        if(isinstance(key, str)):
            return super().remove(key)
