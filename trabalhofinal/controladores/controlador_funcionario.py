from controladores.controlador_abstrato import ControladorAbstrato
from telas.tela_funcionario import TelaFuncionario
from entidades.funcionario import Funcionario
from daos.funcionario_dao import FuncionarioDAO


class ControladorFuncionario(ControladorAbstrato):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__funcionario_DAO = FuncionarioDAO()
        self.__tela_funcionario = TelaFuncionario()

    @property
    def funcionario_DAO(self):
        return self.__funcionario_DAO

    @property
    def tela_funcionario(self):
        return self.__tela_funcionario
    
    def mostrar_funcionario_por_email(self):
        email_funcionario = self.__tela_funcionario.seleciona_funcionario()
        if email_funcionario is None:
            return
        
        funcionario = self.achar_funcionario(email_funcionario)
        if funcionario is not None:
            dados_funcionarios = [{
                "nome": funcionario.nome, 
                "cargo": funcionario.cargo, 
                "salario": funcionario.salario, 
                "email": funcionario.email
            }]
            self.__tela_funcionario.mostra_funcionario(dados_funcionarios)
        else:
            self.__tela_funcionario.mostra_mensagem("Atenção! Funcionário não encontrado no sistema!")

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
        if dados_funcionario is not None:
            funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["cargo"], dados_funcionario["salario"], dados_funcionario["email"])
            self.__funcionario_DAO.add(funcionario)
  
    def alterar_funcionario(self):
        email_funcionario = self.__tela_funcionario.seleciona_funcionario()
        if email_funcionario is None:
            return
        
        funcionario = self.achar_funcionario(email_funcionario)
        if funcionario is not None:
            novos_dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
            if novos_dados_funcionario is not None:
                funcionario.nome = novos_dados_funcionario["nome"]
                funcionario.cargo = novos_dados_funcionario["cargo"]
                funcionario.salario = novos_dados_funcionario["salario"]
                funcionario.email = novos_dados_funcionario["email"]
                return None
        else:
            self.__tela_funcionario.mostra_mensagem("ATENÇÃO: Funcionário não existente no sistema!")

    def lista_funcionarios(self):
        dados_funcionarios = []
        for funcionario in self.__funcionario_DAO.get_all():
            dados_funcionarios.append({"nome": funcionario.nome, "cargo": funcionario.cargo, "salario": funcionario.salario, "email": funcionario.email})
        if len(dados_funcionarios) == 0:
            self.__tela_funcionario.mostra_mensagem("Atenção! Não existem funcionários cadastrados no sistema!")
        else:
            self.__tela_funcionario.mostra_funcionario(dados_funcionarios)

    def excluir_funcionario(self):
        email_funcionario = self.__tela_funcionario.seleciona_funcionario()
        if email_funcionario is None:
            return
        
        funcionario = self.achar_funcionario(email_funcionario)
        if funcionario is not None:
            self.__funcionario_DAO.remove(email_funcionario)
        else:
            self.__tela_funcionario.mostra_mensagem("Atenção! Funcionário selecionado não consta no sistema!")
    
    def achar_funcionario(self, email_funcionario=None):
        if email_funcionario is None:
            email_funcionario = self.__tela_funcionario.seleciona_funcionario()
        for funcionario in self.__funcionario_DAO.get_all():
            if funcionario.email == email_funcionario:
                return funcionario
        else:
            self.__tela_funcionario.mostra_mensagem("Atenção! Não existem funcionários com esse email no sistema!")

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_funcionario, 2: self.alterar_funcionario, 3: self.excluir_funcionario, 4: self.lista_funcionarios, 5: self.achar_funcionario, 6: self.mostrar_funcionario_por_email, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_funcionario.tela_opcoes()]()