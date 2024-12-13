from controladores.controlador_abstrato import ControladorAbstrato
from entidades.turma import Turma
from daos.turma_dao import TurmaDAO

class ControladorTurma(ControladorAbstrato):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__turma_DAO = TurmaDAO()
        
        for i in range(1, 10):
                nome_turma = f"{i}° Ano"
                turma = Turma(nome_turma)
                self.__turma_DAO.add(turma)
        
    @property
    def turma_DAO(self):
        return self.__turma_DAO
    