from telas.tela_financas import TelaFinancas
from entidades.financas import Financas
from controladores.controlador_abstrato import ControladorAbstrato
from daos.financas_dao import FinancasDAO
from excecoes.entrada_invalida_exception import *


class ControladorFinancas(ControladorAbstrato):
    
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela_financas = TelaFinancas()
        self.__financas_DAO = FinancasDAO()
        self.__financa = []

    @property
    def financas_DAO(self):
        return self.__financas_DAO
    
    @property
    def tela_financas(self):
        return self.__tela_financas

    def cadastrar_basicas(self):
        if len(self.__financa) == 0:
            try:
                dados_financas = self.__tela_financas.pega_dados_financas()
                
                entidade_financa = Financas(
                    dados_financas["agua"], 
                    dados_financas["luz"], 
                    dados_financas["internet"], 
                    dados_financas["estrutura"]
                )
                self.__financa.append(entidade_financa)
                self.__financas_DAO.add(entidade_financa)
            except CampoNumericoException as e:
                self.__tela_financas.mostra_mensagem(str(e))
        else:
            self.__tela_financas.mostra_mensagem("Atenção! Você não pode cadastrar mais despesas básicas!")

    def alterar_basicas(self):
        if len(self.__financa) == 1:
            try:
                dados_financas = self.__tela_financas.pega_dados_financas()
                
                financa = self.__financa[0]
                financa.despesas_agua = dados_financas["agua"]
                financa.despesas_luz = dados_financas["luz"]
                financa.despesas_internet = dados_financas["internet"]
                financa.despesas_estrutura = dados_financas["estrutura"]
            except CampoNumericoException as e:
                self.__tela_financas.mostra_mensagem(str(e))
        else:
            self.__tela_financas.mostra_mensagem("Atenção! Você precisa cadastrar as despesas básicas para acessar esse campo!")  
    
    def mostrar_trabalhadores(self):
        if len(self.__financa) == 1:
            professores = self._controlador_sistema.controlador_professor.professores
            funcionarios = self._controlador_sistema.controlador_funcionario.funcionarios
            
            valor = self.__financa[0].despesa_colaboradores(professores, funcionarios)
            self.__tela_financas.mostra_trabalhadores(valor)
        else:
            self.__tela_financas.mostra_mensagem("Atenção! Você precisa cadastrar as despesas básicas para acessar esse campo!")
    
    def mostrar_basicas(self):
        if len(self.__financa) == 1:
            basicas = self.__financa[0].despesas_basicas()
            self.__tela_financas.mostra_basicas(basicas)
        else:
            self.__tela_financas.mostra_mensagem("Atenção! Você precisa cadastrar as despesas básicas para acessar esse campo!")
    
    def mostrar_todas_despesas(self):
        if len(self.__financa) == 1:
            professores = self._controlador_sistema.controlador_professor.professores
            funcionarios = self._controlador_sistema.controlador_funcionario.funcionarios
            
            todas = self.__financa[0].despesa_escola(professores, funcionarios)
            self.__tela_financas.mostra_despesa(todas)
        else:
            self.__tela_financas.mostra_mensagem("Atenção! Você precisa cadastrar as despesas básicas para acessar esse campo!")
    
    def mostrar_lucro(self):
        if len(self.__financa) == 1:
            alunos = self._controlador_sistema.controlador_aluno.alunos
            professores = self._controlador_sistema.controlador_professor.professores
            funcionarios = self._controlador_sistema.controlador_funcionario.funcionarios
            
            lucro = self.__financa[0].lucro_escola(alunos, professores, funcionarios)
            self.__tela_financas.mostra_lucro(lucro)
        else:
            self.__tela_financas.mostra_mensagem("Atenção! Você precisa cadastrar as despesas básicas para acessar esse campo!")
    
    def mostrar_faturamento(self):
        if len(self.__financa) == 1:
            alunos = self._controlador_sistema.controlador_aluno.alunos
            faturamento = self.__financa[0].faturamento_escola(alunos)
            self.__tela_financas.mostra_faturamento(faturamento)
        else:
            self.__tela_financas.mostra_mensagem("Atenção! Você precisa cadastrar as despesas básicas para acessar esse campo!")

    def alunos_bolsistas(self):
        alunos = self._controlador_sistema.controlador_aluno.alunos
        
        if not alunos:
            self.__tela_financas.mostra_mensagem("Atenção! Nenhum aluno está cadastrado no sistema!")
            return
        
        if len(self.__financa) == 1:
            porcentagem = self.__financa[0].porcentagem_bolsistas(alunos)
            self.__tela_financas.mostra_bolsistas(f"{porcentagem:.2f}")
        else:
            self.__tela_financas.mostra_mensagem("Atenção! Você precisa cadastrar as despesas básicas para acessar esse campo!")

    def excluir_basicas(self):
        if len(self.__financa) == 1:
            self.__financa.clear()
            # Se quiser remover do DAO também, descomentar a linha abaixo
            # self.__financas_DAO.remove(alguma_chave)
        else:
            self.__tela_financas.mostra_mensagem("Atenção! Não existem despesas básicas cadastradas!")

    def abre_tela(self):
            lista_opcoes = {1: self.cadastrar_basicas, 2: self.alterar_basicas, 3: self.mostrar_trabalhadores, 4: self.mostrar_basicas, 5: self.mostrar_todas_despesas, 6: self.mostrar_lucro, 7: self.mostrar_faturamento, 8: self.alunos_bolsistas, 9: self.excluir_basicas, 0: self.retornar}
            continua = True
            while continua:
                lista_opcoes[self.__tela_financas.tela_opcoes()]()
