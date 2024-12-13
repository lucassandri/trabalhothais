from daos.dao import DAO
from entidades.financas import Financas

class FinancasDAO(DAO):
    def __init__(self):
        super().__init__('financas.pkl')

    def add(self, financas):
        if(financas is not None) and isinstance(financas, Financas):
            super().add(financas.id, financas)

    def update(self, financas):
        if(financas is not None) and isinstance(financas, Financas):
            super().update(financas.id, financas)

    def get(self, key:int):
        return super().get(key)

    def remove(self, key:int):
        return super().remove(key)
