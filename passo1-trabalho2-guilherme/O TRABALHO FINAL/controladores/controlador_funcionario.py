from controladores.controlador_abstrato import ControladorAbstrato
from telas.tela_funcionario import TelaFuncionario
from entidades.funcionario import Funcionario

class ControladorFuncionario(ControladorAbstrato):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__funcionarios = []
        self.__tela_funcionario = TelaFuncionario()

    @property
    def funcionarios(self):
        return self.__funcionarios

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
        funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["cargo"], dados_funcionario["salario"], dados_funcionario["email"])
        
        if len(self.__funcionarios) == 0:
            self.__funcionarios.append(funcionario)
        else:
            try:
                for worker in self.__funcionarios:
                    if worker.email == funcionario.email:
                        raise KeyError
                else:
                    self.__funcionarios.append(funcionario)
            except KeyError:
                self.__tela_funcionario.mostra_mensagem('Atenção! Funcionário já existente no sistema!')
  
    def alterar_funcionario(self):
        email_funcionario = self.__tela_funcionario.seleciona_funcionario()
        for worker in self.__funcionarios:
            if worker.email == email_funcionario:
                funcionario = worker
                novos_dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
                funcionario.nome = novos_dados_funcionario["nome"]
                funcionario.cargo = novos_dados_funcionario["cargo"]
                funcionario.salario = novos_dados_funcionario["salario"]
                funcionario.email = novos_dados_funcionario["email"]
                return None
        else:
            self.__tela_funcionario.mostra_mensagem("ATENÇÃO: Funcionário não existente no sistema!")

    def lista_funcionarios(self):
        if len(self.__funcionarios) == 0:
            self.__tela_funcionario.mostra_mensagem("Atenção! Não existem funcionários cadastrados no sistema!")
            return None
        else:
            dados_funcionarios = []
            for dado in dados_funcionarios:
                dados_funcionarios.append({"nome": funcionario.nome, "cargo": funcionario.cargo, "salario": funcionario.salario, "email": funcionario.email})
            self.__tela_funcionario.mostra_funcionario(dados_funcionarios)

    def excluir_funcionario(self):
        email_funcionario = self.__tela_funcionario.seleciona_funcionario()
        for funcionario in self.__funcionarios:
            if funcionario.email == email_funcionario:
                self.__funcionarios.remove(funcionario)
                return None
        else:
            self.__tela_funcionario.mostra_mensagem("Atenção! Funcionário selecionado não consta no sistema!")
    
    def achar_funcionario(self):
        email_funcionario = self.__tela_funcionario.seleciona_funcionario()
        for funcionario in self.__funcionarios:
            if funcionario.email == email_funcionario:
                self.__tela_funcionario.mostra_funcionario({"nome": funcionario.nome, "cargo": funcionario.cargo, "salario": funcionario.salario, "email": funcionario.email})
                return None
        else:
            self.__tela_funcionario.mostra_mensagem("Atenção! Não existem funcionários com esse email no sistema!")

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_funcionario, 2: self.alterar_funcionario, 3: self.excluir_funcionario, 4: self.lista_funcionarios, 5: self.achar_funcionario, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_funcionario.tela_opcoes()]()