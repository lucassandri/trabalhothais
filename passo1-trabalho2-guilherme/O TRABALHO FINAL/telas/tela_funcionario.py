from telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaFuncionario(TelaAbstrata):

    def __init__(self):
        self.init_components()

    def init_components(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('Funcionários', font=("Arial", 25))],
            [sg.Text('Escolha sua opção', font=("Arial", 15))],
            [sg.Radio('Incluir Funcionário', "RD1", key='1')],
            [sg.Radio('Alterar Funcionário', "RD1", key='2')],
            [sg.Radio('Excluir Funcionário', "RD1", key='3')],
            [sg.Radio('Listar Funcionários', "RD1", key='4')],
            [sg.Radio('Mostrar funcionário por email', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Funcionários').Layout(layout)

    def tela_opcoes(self):
        self.init_components()
        button, values = self.window.Read()
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
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def pega_dados_funcionario(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('-------- DADOS FUNCIONÁRIO ----------', font=("Arial", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Cargo:', size=(15, 1)), sg.InputText('', key='cargo')],
            [sg.Text('Salário:', size=(15, 1)), sg.InputText('', key='salario')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('FUNCIONÁRIOS').Layout(layout)

        button, values = self.open()
        nome = values["nome"]
        cargo = values["cargo"]
        salario = values["salario"]
        email = values["email"]
        self.close()
        return {"nome": nome, "cargo": cargo, "salario": salario, "email": email}

    def seleciona_funcionario(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('-------- SELECIONAR FUNCIONÁRIO ----------', font=("Arial", 25))],
            [sg.Text('Digite o email do funcionário que deseja selecionar:', font=("Arial", 15))],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Seleciona funcionário').Layout(layout)

        button, values = self.open()
        email = values['email']
        self.close()
        return email

    def mostra_funcionario(self, dados_funcionario):
        string_todos_funcionarios = ""
        string_todos_funcionarios = string_todos_funcionarios + "NOME DO FUNCIONÁRIO: " + str(dados_funcionario["nome"]) + '\n'
        string_todos_funcionarios = string_todos_funcionarios + "CARGO DO FUNCIONÁRIO: " + str(dados_funcionario["cargo"]) + '\n'
        string_todos_funcionarios = string_todos_funcionarios + "SALÁRIO DO FUNCIONÁRIO: " + str(dados_funcionario["salario"]) + '\n'
        string_todos_funcionarios = string_todos_funcionarios + "EMAIL DO FUNCIONÁRIO: " + str(dados_funcionario["email"]) + '\n\n'


        sg.Popup('-------- LISTA DE FUNCIONÁRIOS ----------', string_todos_funcionarios)
