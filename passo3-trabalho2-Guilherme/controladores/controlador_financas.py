from telas.tela_financas import TelaFinancas
from entidades.financas import Financas
from controladores.controlador_abstrato import ControladorAbstrato


class ControladorFinancas(ControladorAbstrato):

    def __init__(self, controlador_sistema, controlador_aluno, controlador_professor, controlador_funcionario):
        super().__init__(controlador_sistema)
        self.__controlador_aluno = controlador_aluno
        self.__controlador_professor = controlador_professor
        self.__controlador_funcionario = controlador_funcionario
        self.__tela_financas = TelaFinancas()
        self.__financa = []

    def cadastrar_basicas(self):
        if len(self.__financa) == 0:
            dados_financas = self.__tela_financas.pega_dados_financas()
            entidade_financa = Financas(dados_financas["agua"], dados_financas["luz"], dados_financas["internet"],
                                        dados_financas["estrutura"])

            self.__financa.append(entidade_financa)
        else:
            self.__tela_financas.mostra_mensagem("Atenção! Você não pode cadastrar mais despesas básicas!")

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
            self.__tela_financas.mostra_mensagem(
                "Atenção! Você precisa cadastradar as despesas básicas para acessar esse campo!")

    def mostrar_trabalhadores(self):
        if len(self.__financa) == 1:
            valor = self.despesa_colaboradores()
            self.__tela_financas.mostra_trabalhadores(valor)
        else:
            self.__tela_financas.mostra_mensagem(
                "Atenção! Você precisa cadastradar as despesas básicas para acessar esse campo!")

    def mostrar_basicas(self):
        if len(self.__financa) == 1:
            basicas = self.despesas_basicas()
            self.__tela_financas.mostra_basicas(basicas)
        else:
            self.__tela_financas.mostra_mensagem(
                "Atenção! Você precisa cadastradar as despesas básicas para acessar esse campo!")

    def mostrar_todas_despesas(self):
        todas = self.despesa_escola()
        self.__tela_financas.mostra_despesa(todas)

    def mostrar_lucro(self):
        lucro = self.lucro_escola()
        self.__tela_financas.mostra_lucro(lucro)

    def mostrar_faturamento(self):
        faturamento = self.faturamento_escola()
        self.__tela_financas.mostra_faturamento(faturamento)

    def alunos_bolsistas(self):
        if len(self._controlador_sistema.controlador_aluno.alunos) == 0:
            self.__tela_financas.mostra_mensagem("Atenção! Nenhum aluno está cadastrado no sistema!")
            return None
        else:
            soma = 0
            for aluno in self._controlador_sistema.controlador_aluno.alunos:
                if aluno.bolsa == 'Bolsista':
                    soma += 1
            if soma > 0:
                porcentagem = float(soma / len(self._controlador_sistema.controlador_aluno.alunos)) * 100
                porcentagem = f"{porcentagem:.2f}"
                self.__tela_financas.mostra_bolsistas(porcentagem)
                return None
            else:
                self.__tela_financas.mostra_mensagem("Não há alunos com bolsas")

    def excluir_basicas(self):
        if len(self.__financa) == 1:
            self.__financa.remove(self.__financa[0])
        else:
            self.__tela_financas.mostra_mensagem("Atenção! Não existem despesas básicas cadastradas!")

    def faturamento_escola(self):
        faturamento = 0
        for aluno in self._controlador_sistema.controlador_aluno.alunos:
            faturamento += aluno.mensalidade
        return faturamento

    def despesa_escola(self):
        if len(self.__financa) == 1:
            for financa in self.__financa:
                dados_despesas = {"agua": financa.despesas_agua, "luz": financa.despesas_luz,
                                  "internet": financa.despesas_internet, "estrutura": financa.despesas_estrutura}
                despesa = 0
                for professor in self._controlador_sistema.controlador_professor.professores:
                    despesa += professor.salario
                for funcionario in self._controlador_sistema.controlador_funcionario.funcionarios:
                    despesa += funcionario.salario
                despesa += int(dados_despesas["agua"])
                despesa += int(dados_despesas["luz"])
                despesa += int(dados_despesas["internet"])
                despesa += int(dados_despesas["estrutura"])
                return despesa
        else:
            self.__tela_financas.mostra_mensagem(
                "Atenção! Você precisa cadastradar as despesas básicas para acessar esse campo!")

    def despesas_basicas(self):
        if len(self.__financa) == 1:
            for financa in self.__financa:
                dados_despesas = {"agua": financa.despesas_agua, "luz": financa.despesas_luz,
                                  "internet": financa.despesas_internet, "estrutura": financa.despesas_estrutura}
                despesa = 0
                despesa += int(dados_despesas["agua"])
                despesa += int(dados_despesas["luz"])
                despesa += int(dados_despesas["internet"])
                despesa += int(dados_despesas["estrutura"])
                return despesa
        else:
            self.__tela_financas.mostra_mensagem(
                "Atenção! Você precisa cadastradar as despesas básicas para acessar esse campo!")

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

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_basicas, 2: self.alterar_basicas, 3: self.mostrar_trabalhadores,
                        4: self.mostrar_basicas, 5: self.mostrar_todas_despesas, 6: self.mostrar_lucro,
                        7: self.mostrar_faturamento, 8: self.alunos_bolsistas, 9: self.excluir_basicas,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_financas.tela_opcoes()]()
