from telas.tela_abstrata import TelaAbstrata

class TelaFinancas(TelaAbstrata):

    def __init__(self):
        pass

    def tela_opcoes(self):
        print('--------FINANÇAS--------')
        print('1 - Cadastrar despesas básicas da escola')
        print('2 - Alterar despesas básicas da escola')
        print('3 - Mostrar despesas de todos os trabalhadores da escola')
        print('4 - Mostrar despesas básicas da escola')
        print('5 - Mostrar despesas totais da escola')
        print('6 - Mostrar lucro da escola')
        print('7 - Mostrar faturamento total da escola')
        print('8 - Mostrar porcentagem de alunos bolsistas da escola')
        print('9 - Excluir finança')
        print('0 - Retornar')
        opcao = self.le_num_inteiro("Escolha a opção:", [0,1,2,3,4,5,6,7,8,9])
        return opcao
    
    def pega_dados_financas(self):
        print('------GASTOS BÁSICOS DA ESCOLA----------')
        agua = self.le_float('Dinheiro gasto com água: ')
        luz = self.le_float('Dinheiro gasto com luz: ')
        internet = self.le_float('Dinheiro gasto com internet: ')
        estrutura = self.le_float('Dinheiro gasto com estrutura: ')
        return {"agua": agua, "luz": luz, "internet": internet, "estrutura": estrutura}
    
    def mostra_trabalhadores(self, valor):
        print (f"As despesas com os colaboradores é de R$: {valor}")
        print ("----------------------------------------------------")

    def mostra_despesa(self, valor):
        print (f"A despesa total da escola é de R$: {valor}")
        print ("----------------------------------------------------")

    def mostra_basicas(self, valor):
        print (f"A despesa das contas básicas da escola é de R$: {valor}")
        print ("----------------------------------------------------")

    def mostra_lucro(self, valor):
        print (f"O lucro da escola é de R$: {valor}")
        print ("----------------------------------------------------")

    def mostra_faturamento(self, valor):
        print (f"O faturamento da escola é de R$: {valor}")
        print ("----------------------------------------------------")

    def mostra_bolsistas(self, valor):
        print (f"A porcentagem de alunos bolsistas é de {valor:.2f}%")
        print ("----------------------------------------------------")
