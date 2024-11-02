from telas.tela_financas import TelaFinancas
from entidades.financas import Financas
from controladores.controlador_abstrato import ControladorAbstrato

class ControladorFinancas(ControladorAbstrato):
    
    def __init__(self, controlador_sistema, controlador_aluno, controlador_professor, controlador_funcionario):
        super().__init__(controlador_sistema)
        self.__tela_financas = TelaFinancas()
        self.__financa = []
    
    def cadastrar_basicas(self):
        if len(self.__financa) == 0:
            dados_financas = self.__tela_financas.pega_dados_financas()
            entidade_financa = Financas(dados_financas["agua"], dados_financas["luz"], dados_financas["internet"], dados_financas["estrutura"])

            self.__financa.append(entidade_financa)
        else:
            self.__tela_financas.mostra_mensagem("Você não pode cadastrar mais de uma financa por vez")

    def alterar_basicas(self):
        if len(self.__financa) == 1:
            novos_dados = self.__tela_financas.pega_dados_financas()
            for nova_financa in self.__financa:
                nova_financa.despesas_agua = novos_dados["agua"]
                nova_financa.despesas_luz = novos_dados["luz"]
                nova_financa.despesas_internet = novos_dados["internet"]
                nova_financa.despesas_estrutura = novos_dados["estrutura"]
                return None
        else:
            self.__tela_financas.mostra_mensagem("Ainda não foram cadastradas as despesas basicas")
        
    
    def mostrar_trabalhadores(self):
        if len(self.__financa) == 1:
            valor = self.despesa_colaboradores()
            self.__tela_financas.mostra_trabalhadores(valor)
        else:
            self.__tela_financas.mostra_mensagem("Você precisa cadastradar as despesas basicas antes!")
    
    def mostrar_basicas(self):
        if len(self.__financa) == 1:
            valor = self.despesas_basicas()
            self.__tela_financas.mostra_basicas(valor)
        else:
            self.__tela_financas.mostra_mensagem("Ainda não foram cadastradas as despesas basicas")
    
    def mostrar_todas_despesas(self):
        if len(self.__financa) == 1:
            valor = self.despesa_escola()
            self.__tela_financas.mostra_despesa(valor)
        else:
            self.__tela_financas.mostra_mensagem("Ainda não foram cadastradas as despesas basicas")
            
    def mostrar_lucro(self):
        if len(self.__financa) == 1:
            valor = self.lucro_escola()
            self.__tela_financas.mostra_lucro(valor)
        else:
            self.__tela_financas.mostra_mensagem("Ainda não foram cadastradas as despesas basicas")

    def mostrar_faturamento(self):
        if len(self.__financa) == 1:
            valor = self.faturamento_escola()
            self.__tela_financas.mostra_faturamento(valor)
        else:
            self.__tela_financas.mostra_mensagem("Ainda não foram cadastradas as despesas basicas")

    
    def alunos_bolsistas(self):
        if self._controlador_sistema.controlador_aluno.alunos == 0:
            self.__tela_financas.mostra_mensagem("Nenhum aluno cadastrado ainda")
            return None
        else:
            soma = 0
            for aluno in self._controlador_sistema.controlador_aluno.alunos:
                if aluno.bolsa == 'Bolsista':
                    soma += 1
            if soma > 0:
                porcentagem = float(soma / len(self._controlador_sistema.controlador_aluno.alunos)) * 100
                self.__tela_financas.mostra_bolsistas(porcentagem)
                return None
            else:
                self.__tela_financas.mostra_mensagem("Não há alunos com bolsas")

    def excluir_basicas(self):
        if len(self.__financa) == 1:
            self.__financa.remove(self.__financa[0])
        else:
            self.__tela_financas.mostra_mensagem("Não há mais nenhuma finança cadastrada")


    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_basicas, 2: self.alterar_basicas, 3: self.mostrar_trabalhadores, 4: self.mostrar_basicas, 5: self.mostrar_todas_despesas, 6: self.mostrar_lucro, 7: self.mostrar_faturamento, 8: self.alunos_bolsistas, 9: self.excluir_basicas, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_financas.tela_opcoes()]()

    def faturamento_escola(self):
        faturamento = 0
        for aluno in self._controlador_sistema.controlador_aluno.alunos:
            faturamento += aluno.mensalidade
        return faturamento
    
    def despesa_escola(self):
        if len(self.__financa) == 1:
            for financa in self.__financa:
                dados_despesas = {"agua": financa.despesas_agua, "luz": financa.despesas_luz, "internet": financa.despesas_internet, "estrutura": financa.despesas_estrutura}
                despesa = 0
                for professor in self._controlador_sistema.controlador_professor.professores:
                    despesa += professor.salario
                for funcionario in self._controlador_sistema.controlador_funcionario.funcionarios:
                    despesa += funcionario.salario
                despesa += dados_despesas["agua"]
                despesa += dados_despesas["luz"]
                despesa += dados_despesas["internet"]
                despesa += dados_despesas["estrutura"]
                return despesa
        else:
            self.__tela_financas.mostra_mensagem("Ainda não foram cadastradas as despesas basicas")
    
    def despesas_basicas(self):
        if len(self.__financa) == 1:
            for financa in self.__financa:
                dados_despesas = {"agua": financa.despesas_agua, "luz": financa.despesas_luz, "internet": financa.despesas_internet, "estrutura": financa.despesas_estrutura}
                despesa = 0
                despesa += dados_despesas["agua"]
                despesa += dados_despesas["luz"]
                despesa += dados_despesas["internet"]
                despesa += dados_despesas["estrutura"]
                return despesa
        else:
            self.__tela_financas.mostra_mensagem("Ainda não foram cadastradas as despesas basicas")

    def despesa_colaboradores(self):
        despesa = 0
        if self._controlador_sistema.controlador_professor.professores != 0:
            for professor in self._controlador_sistema.controlador_professor.professores:
                despesa += professor.salario

        if self._controlador_sistema.controlador_funcionario.funcionarios != 0:       
            for funcionario in self._controlador_sistema.controlador_funcionario.funcionarios:
                despesa += funcionario.salario
        return despesa

    def lucro_escola(self):
        lucro = self.faturamento_escola() - self.despesa_escola()
        return lucro
