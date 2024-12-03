from entidades.professor import Professor
from telas.tela_professor import TelaProfessor
from controladores.controlador_abstrato import ControladorAbstrato
from daos.professor_dao import ProfessorDAO

class ControladorProfessor(ControladorAbstrato):
    
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__professor_DAO = ProfessorDAO()
        self.__tela_professor = TelaProfessor()
    
    @property
    def professores(self):
        return self.__professores

    def incluir_professor(self):
        dados_professor = self.__tela_professor.pega_dados_professor()
        professor = Professor(dados_professor["nome"], dados_professor["salario"], dados_professor["leciona"], dados_professor["email"])
        self.__professor_DAO.add(professor)
  
    def alterar_professor(self):
        email_professor = self.__tela_professor.seleciona_professor()
        professor = self.achar_professor(email_professor)
        if professor is not None:
            novos_dados_professor = self.__tela_professor.pega_dados_professor()
            professor.nome = novos_dados_professor["nome"]
            professor.cargo = novos_dados_professor["salario"]
            professor.salario = novos_dados_professor["leciona"]
            professor.email = novos_dados_professor["email"]
            return None
        else:
            self.__tela_professor.mostra_mensagem("ATENÇÃO: Professor não existente no sistema!")

    def lista_professores(self):
        dados_professores = []
        for professor in self.__professor_DAO.get_all():
            dados_professores.append({"nome": professor.nome, "salario": professor.salario, "leciona": professor.leciona, "email": professor.email})
        if len(dados_professores) == 0:
            self.__tela_professor.mostra_mensagem("Atenção! Não existem professores cadastrados no sistema!")
        else:
            self.__tela_professor.mostra_professor(dados_professores)

    def excluir_professor(self):
        email_professor = self.__tela_professor.seleciona_professor()
        professor = self.achar_professor(email_professor)
        if professor is not None:
            self.__professor_DAO.remove(professor)
        else:
            self.__tela_professor.mostra_mensagem("Atenção! Professor selecionado não consta no sistema!")
    
    def achar_professor(self, email_professor):
        for professor in self.__professor_DAO.get_all():
            if professor.email == email_professor:
                return professor
        else:
            self.__tela_professor.mostra_mensagem("Atenção! Não existem Professores com esse email no sistema!")

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_professor, 2: self.alterar_professor, 3: self.excluir_professor, 4: self.lista_professores, 5: self.achar_professor, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_professor.tela_opcoes()]()
