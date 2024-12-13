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
        self.__financa = list(self.__financas_DAO.get_all())
        self.__proximo_id = max([f.id for f in self.__financa], default=0) + 1

    @property
    def financas_DAO(self):
        return self.__financas_DAO
    
    @property
    def tela_financas(self):
        return self.__tela_financas

    def cadastrar_basicas(self):
        try:
            dados_financas = self.__tela_financas.pega_dados_financas()
            
            entidade_financa = Financas(
                dados_financas["agua"], 
                dados_financas["luz"], 
                dados_financas["internet"], 
                dados_financas["estrutura"]
            )
            
            entidade_financa.id = self.__proximo_id
            self.__proximo_id += 1
            
            self.__financa.append(entidade_financa)
            self.__financas_DAO.add(entidade_financa)
            
        except CampoNumericoException as e:
            self.__tela_financas.mostra_mensagem(str(e))

    def alterar_basicas(self):
        if len(self.__financa) > 0:
            id_selecionado = self.__tela_financas.selecionar_financa(self.__financa)
            
            if id_selecionado is None:
                return
            
            financa_selecionada = next((f for f in self.__financa if f.id == id_selecionado), None)
            
            if financa_selecionada is None:
                self.__tela_financas.mostra_mensagem("Finança não encontrada!")
                return
            
            try:
                dados_financas = self.__tela_financas.pega_dados_financas()
                
                financa_selecionada.despesas_agua = dados_financas["agua"]
                financa_selecionada.despesas_luz = dados_financas["luz"]
                financa_selecionada.despesas_internet = dados_financas["internet"]
                financa_selecionada.despesas_estrutura = dados_financas["estrutura"]
                self.__financas_DAO.update(financa_selecionada)
            except CampoNumericoException as e:
                self.__tela_financas.mostra_mensagem(str(e))
        else:
            self.__tela_financas.mostra_mensagem("Atenção! Você precisa cadastrar as despesas básicas para acessar esse campo!") 
    
    def mostrar_trabalhadores(self):
        id_selecionado = self.__tela_financas.selecionar_financa(self.__financa)
        
        if id_selecionado is None:
            return
        
        financa_selecionada = next((f for f in self.__financa if f.id == id_selecionado), None)
        
        if financa_selecionada is None:
            self.__tela_financas.mostra_mensagem("Finança não encontrada!")
            return
        
        professores = self._controlador_sistema.controlador_professor.professor_DAO.get_all()
        funcionarios = self._controlador_sistema.controlador_funcionario.funcionario_DAO.get_all()
        
        valor = financa_selecionada.despesa_colaboradores(professores, funcionarios)
        self.__tela_financas.mostra_trabalhadores(valor)
    
    def mostrar_basicas(self):
        id_selecionado = self.__tela_financas.selecionar_financa(self.__financa)
        
        if id_selecionado is None:
            return
        
        financa_selecionada = next((f for f in self.__financa if f.id == id_selecionado), None)
        
        if financa_selecionada is None:
            self.__tela_financas.mostra_mensagem("Finança não encontrada!")
            return
        
        basicas = financa_selecionada.despesas_basicas()
        self.__tela_financas.mostra_basicas(basicas)
    
    def mostrar_todas_despesas(self):
        id_selecionado = self.__tela_financas.selecionar_financa(self.__financa)
        
        if id_selecionado is None:
            return
        
        financa_selecionada = next((f for f in self.__financa if f.id == id_selecionado), None)
        
        if financa_selecionada is None:
            self.__tela_financas.mostra_mensagem("Finança não encontrada!")
            return
        
        professores = self._controlador_sistema.controlador_professor.professor_DAO.get_all()
        funcionarios = self._controlador_sistema.controlador_funcionario.funcionario_DAO.get_all()
        
        todas = financa_selecionada.despesa_escola(professores, funcionarios)
        self.__tela_financas.mostra_despesa(todas)
    
    def mostrar_lucro(self):
        id_selecionado = self.__tela_financas.selecionar_financa(self.__financa)
        
        if id_selecionado is None:
            return
        
        financa_selecionada = next((f for f in self.__financa if f.id == id_selecionado), None)
        
        if financa_selecionada is None:
            self.__tela_financas.mostra_mensagem("Finança não encontrada!")
            return
        
        alunos = self._controlador_sistema.controlador_aluno.alunos_DAO.get_all()
        professores = self._controlador_sistema.controlador_professor.professor_DAO.get_all()
        funcionarios = self._controlador_sistema.controlador_funcionario.funcionario_DAO.get_all()
        
        lucro = financa_selecionada.lucro_escola(alunos, professores, funcionarios)
        self.__tela_financas.mostra_lucro(lucro)
    
    def mostrar_faturamento(self):
        id_selecionado = self.__tela_financas.selecionar_financa(self.__financa)
        
        if id_selecionado is None:
            return
        
        financa_selecionada = next((f for f in self.__financa if f.id == id_selecionado), None)
        
        if financa_selecionada is None:
            self.__tela_financas.mostra_mensagem("Finança não encontrada!")
            return
        
        
        alunos = self._controlador_sistema.controlador_aluno.alunos_DAO.get_all()
        faturamento = financa_selecionada.faturamento_escola(alunos)
        self.__tela_financas.mostra_faturamento(faturamento)


    def alunos_bolsistas(self):
        alunos = self._controlador_sistema.controlador_aluno.alunos_DAO.get_all()
        
        if not alunos:
            self.__tela_financas.mostra_mensagem("Atenção! Nenhum aluno está cadastrado no sistema!")
            return
        
        if len(self.__financa) == 1:
            porcentagem = self.__financa[0].porcentagem_bolsistas(alunos)
            self.__tela_financas.mostra_bolsistas(f"{porcentagem:.2f}")
        else:
            self.__tela_financas.mostra_mensagem("Atenção! Você precisa cadastrar as despesas básicas para acessar esse campo!")

    def excluir_basicas(self):
        id_selecionado = self.__tela_financas.selecionar_financa(self.__financa)
        
        if id_selecionado is None:
            return
        
        financa_selecionada = next((f for f in self.__financa if f.id == id_selecionado), None)
        
        if financa_selecionada is None:
            self.__tela_financas.mostra_mensagem("Finança não encontrada!")
            return
        
        self.__financa.remove(financa_selecionada)
        self.__financas_DAO.remove(financa_selecionada.id)

    def abre_tela(self):
            lista_opcoes = {1: self.cadastrar_basicas, 2: self.alterar_basicas, 3: self.mostrar_trabalhadores, 4: self.mostrar_basicas, 5: self.mostrar_todas_despesas, 6: self.mostrar_lucro, 7: self.mostrar_faturamento, 8: self.alunos_bolsistas, 9: self.excluir_basicas, 0: self.retornar}
            continua = True
            while continua:
                lista_opcoes[self.__tela_financas.tela_opcoes()]()
