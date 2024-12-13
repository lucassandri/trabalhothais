from telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from excecoes.entrada_invalida_exception import *

class TelaFinancas(TelaAbstrata):

    def __init__(self):
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('-------- FINANÇAS ----------', font=("Arial", 25))],
            [sg.Text('Escolha sua opção', font=("Arial", 15))],
            [sg.Radio('Cadastrar despesas básicas da escola', "RD1", key='1')],
            [sg.Radio('Alterar despesas básicas da escola', "RD1", key='2')],
            [sg.Radio('Mostrar despesas de todos os trabalhadores da escola', "RD1", key='3')],
            [sg.Radio('Mostrar despesas básicas da escola', "RD1", key='4')],
            [sg.Radio('Mostrar despesas totais da escola', "RD1", key='5')],
            [sg.Radio('Mostrar lucro da escola', "RD1", key='6')],
            [sg.Radio('Mostrar faturamento total da escola', "RD1", key='7')],
            [sg.Radio('Mostrar porcentagem de alunos bolsistas da escola', "RD1", key='8')],
            [sg.Radio('Excluir finança', "RD1", key='9')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Finanças').Layout(layout)

    def tela_opcoes(self):
        self.init_components()
        button, values = self.window.Read()
        
        if button in (None, 'Cancelar'):
            opcao = 0
        
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['8']:
            opcao = 8
        if values['9']:
            opcao = 9
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

        # def pega_dados_financas(self):
        #agua = self.le_float('Gasto com água: ')
        #luz = self.le_float('Gasto com luz: ')
        #internet = self.le_float('Gasto com internet: ')
        #estrutura = self.le_float('Gasto com estrutura: ')
        #return {"agua": agua, "luz": luz, "internet": internet, "estrutura": estrutura}

    def pega_dados_financas(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('-------- DADOS FINANCAS ----------', font=("Arial", 25))],
            [sg.Text('Gasto com água:', size=(15, 1)), sg.InputText('', key='agua')],
            [sg.Text('Gasto com luz:', size=(15, 1)), sg.InputText('', key='luz')],
            [sg.Text('Gasto com internet:', size=(15, 1)), sg.InputText('', key='internet')],
            [sg.Text('Gasto com estrutura:', size=(15, 1)), sg.InputText('', key='estrutura')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.window = sg.Window('DADOS FINANCAS').Layout(layout)

        button, values = self.open()
        
        if button in (None, 'Cancelar'):
            self.close()
            return None

        try:
            agua = float(values['agua'])
        except ValueError:
            raise CampoNumericoException('Gasto com água deve ser um número')

        try:
            luz = float(values['luz'])
        except ValueError:
            raise CampoNumericoException('Gasto com luz deve ser um número')

        try:
            internet = float(values['internet'])
        except ValueError:
            raise CampoNumericoException('Gasto com internet deve ser um número')

        try:
            estrutura = float(values['estrutura'])
        except ValueError:
            raise CampoNumericoException('Gasto com estrutura deve ser um número')
        
        self.close()

        return {"agua": agua, "luz": luz, "internet": internet, "estrutura": estrutura}


        # def mostra_trabalhadores(self, valor):
        #print(f"As despesas com os colaboradores é de R$: {valor}")
        #print("----------------------------------------------------")
        
    def selecionar_financa(self, financas):

        sg.ChangeLookAndFeel('BlueMono')

        if not financas:
            sg.popup_error("Não existem finanças cadastradas!")
            return None

        ids_financas = [str(financa.id) for financa in financas]
        
        layout = [
            [sg.Text('-------- SELECIONAR FINANÇA ----------', font=("Arial", 25))],
            [sg.Text('Selecione o ID da Finança:', font=("Arial", 15))],
            [sg.Combo(ids_financas, key='id_financa', size=(10, 1))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Selecionar Finança').Layout(layout)
        button, values = window.Read()
        window.close()

        if button in (None, 'Cancelar'):
            return None
        
        if not values['id_financa']:
            self.mostra_mensagem("Nenhuma finança selecionada!")
            return None
        
        return int(values['id_financa'])

    def mostra_trabalhadores(self, valor):
        string_financas = ""
        string_financas = string_financas + "As despesas com os colaboradores é de R$: " + str(valor) + '\n\n'
        sg.Popup('-------- VALOR DESPESA COLABORADORES ----------', string_financas)

    def mostra_despesa(self, valor):
        string_financas = ""
        string_financas = string_financas + "As despesa total da escola é de R$: " + str(valor) + '\n\n'
        sg.Popup('-------- VALOR TODAS AS DESPESAS ----------', string_financas)

    def mostra_basicas(self, valor):
        string_financas = ""
        string_financas = string_financas + "As despesa das contas básicas da escola é de R$: " + str(valor) + '\n\n'
        sg.Popup('-------- VALOR DESPESAS BÁSICAS ----------', string_financas)

    def mostra_lucro(self, valor):
        string_financas = ""
        string_financas = string_financas + "O lucro da escola é de R$: " + str(valor) + '\n\n'
        sg.Popup('-------- VALOR DO LUCRO ----------', string_financas)

    def mostra_faturamento(self, valor):
        string_financas = ""
        string_financas = string_financas + "O faturamento da escola é de R$: " + str(valor) + '\n\n'
        sg.Popup('-------- VALOR DO FATURAMENTO ----------', string_financas)

    def mostra_bolsistas(self, valor):
        string_financas = ""
        string_financas = string_financas + "A porcentagem de alunos bolsistas é de " + str(valor) + "%" + '\n\n'
        sg.Popup('-------- ALUNOS BOLSISTAS ----------', string_financas)
