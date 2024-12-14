from entidades.professor import Professor
from telas.tela_professor import TelaProfessor
from controladores.controlador_abstrato import ControladorAbstrato
from daos.professor_dao import ProfessorDAO
from daos.turma_dao import TurmaDAO
from excecoes.entrada_invalida_exception import *


class ControladorProfessor(ControladorAbstrato):
    
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__professor_DAO = ProfessorDAO()
        self.__tela_professor = TelaProfessor()
        self.__turma_DAO = TurmaDAO()
    
    @property
    def professor_DAO(self):
        return self.__professor_DAO

    def incluir_professor(self):
        try:
            dados_professor = self.__tela_professor.pega_dados_professor()
 
            if dados_professor is None:
                return
            
            professor = Professor(
                dados_professor["nome"], 
                float(dados_professor["salario"]), 
                dados_professor["leciona"], 
                dados_professor["email"],
                dados_professor["serie"]
            )
            
            turma = self.__turma_DAO.get(f"{dados_professor['serie']}° Ano")
            if turma:
                turma.adicionar_professor(professor)
            
            self.__professor_DAO.add(professor)
        
        except EntradaInvalidaException as e:
            self.__tela_professor.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_professor.mostra_mensagem(f"Erro ao incluir professor: {str(e)}")
  
    def alterar_professor(self):
        email_professor = self.__tela_professor.seleciona_professor()
        professor = self.achar_professor(email_professor)
        if professor is not None:
            novos_dados_professor = self.__tela_professor.pega_dados_professor()
            professor.nome = novos_dados_professor["nome"]
            professor.salario = novos_dados_professor["salario"]
            professor.leciona = novos_dados_professor["leciona"]
            professor.email = novos_dados_professor["email"]
            professor.serie = novos_dados_professor["serie"]
            return None
        else:
            self.__tela_professor.mostra_mensagem("ATENÇÃO: Professor não existente no sistema!")

    def lista_professores(self):
        dados_professores = []
        for professor in self.__professor_DAO.get_all():
            dados_professores.append({
                "nome": professor.nome, 
                "salario": professor.salario, 
                "leciona": professor.leciona, 
                "email": professor.email,
                "serie": professor.serie
            })
        if len(dados_professores) == 0:
            self.__tela_professor.mostra_mensagem("Atenção! Não existem professores cadastrados no sistema!")
        else:
            self.__tela_professor.mostra_professor(dados_professores)

    def excluir_professor(self):
        email_professor = self.__tela_professor.seleciona_professor()
        if email_professor is None:
            return
        
        professor = self.achar_professor(email_professor)
        if professor is not None:
            self.__professor_DAO.remove(email_professor)
            self.__tela_professor.mostra_mensagem("Professor excluído com sucesso!")
        else:
            self.__tela_professor.mostra_mensagem("Atenção! Professor selecionado não consta no sistema!")
            
            
    def busca_professor_por_email(self):
        email_professor = self.__tela_professor.seleciona_professor()
        
        if email_professor is None:
            return
        
        if not email_professor:
            self.__tela_professor.mostra_mensagem("Por favor, digite um email válido.")
            return
        
        professor = self.achar_professor(email_professor)
        
        if professor is not None:
            dados_professor = [{
                "nome": professor.nome, 
                "salario": professor.salario, 
                "leciona": professor.leciona, 
                "email": professor.email,
                "serie": professor.serie
            }]
            self.__tela_professor.mostra_professor(dados_professor)
    
    def mostrar_professor_por_email(self):
        email_professor = self.__tela_professor.seleciona_professor()
        if email_professor is None:
            return
        
        professor = self.achar_professor(email_professor)
        if professor is not None:
            dados_professores = [{
                "nome": professor.nome, 
                "salario": professor.salario, 
                "leciona": professor.leciona, 
                "email": professor.email,
                "serie": professor.serie
            }]
            self.__tela_professor.mostra_professor(dados_professores)
        else:
            self.__tela_professor.mostra_mensagem("Atenção! Professor não encontrado no sistema!")

    def achar_professor(self, email_professor=None):
        if email_professor is None:
            email_professor = self.__tela_professor.seleciona_professor()
        
        if email_professor is None:
            return None
        
        for professor in self.__professor_DAO.get_all():
            if professor.email == email_professor:
                return professor
        
        self.__tela_professor.mostra_mensagem("Atenção! Não existem Professores com esse email no sistema!")
        return None

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_professor, 2: self.alterar_professor, 3: self.excluir_professor, 4: self.lista_professores, 5: self.mostrar_professor_por_email, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_professor.tela_opcoes()]()