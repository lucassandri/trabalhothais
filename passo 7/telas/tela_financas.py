from tela_abstrata import TelaAbstrata

class TelaFinancas(TelaAbstrata):

    def __init__(self):
        pass

    def tela_opcoes(self):
        print('--------FINANÇAS--------')
        print('1 - Cadastrar despesas básicas da escola')
        print('2 - Alterar despesas básicas da escola')
        print('3 - Excluir despesas básicas da escola')
        print('4 - Mostrar despesas com todos os trabalhadores da escola')
        print('5 - Mostrar despesas básicas da escola')
        print('6 - Mostrar despesas totais da escola')
        print('7 - Mostrar lucro da escola')
        print('8 - Mostrar faturamento total da escola')
        print('9 - Mostrar porcentagem de alunos bolsistas da escola')
        print('0 - Retornar')
    
    def pega_dados_financas(self):
        print('------GASTOS BÁSICOS DA ESCOLA----------')
        agua = self.le_float('Valor mensal gasto com água: ')
        luz = self.le_float('Valor mensal gasto com luz: ')
        internet = self.le_float('Valor mensal gasto com internet: ')
        estrutura = self.le_float('Valor mensal gasto com estrutura: ')

        return {"agua": agua, "luz": luz, "internet": internet, "estrutura": estrutura}