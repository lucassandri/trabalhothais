from telas.tela_abstrata import TelaAbstrata
from excecoes.entrada_invalida_exception import *
import PySimpleGUI as sg

class TelaFuncionario(TelaAbstrata):

    def __init__(self):
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('Funcionários', font=("Arial", 25))],
            [sg.Text('Escolha sua opção', font=("Arial", 15))],
            [sg.Radio('Incluir Funcionário', "RD1", key='1')],
            [sg.Radio('Alterar Funcionário', "RD1", key='2')],
            [sg.Radio('Excluir Funcionário', "RD1", key='3')],
            [sg.Radio('Listar Funcionários', "RD1", key='4')],
            [sg.Radio('Buscar Funcionário por Email', "RD1", key='6')],
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
        if values['6']:
            opcao = 6
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def pega_dados_funcionario(self):
        sg.ChangeLookAndFeel('BlueMono')
        while True:
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
            
            # If 'Cancelar' is clicked, return None immediately
            if button == 'Cancelar' or button is None:
                self.close()
                return None
            
            nome = values["nome"]
            cargo = values["cargo"]
            salario = values["salario"]
            email = values["email"]
            self.close()

            try:
                self.validar_nome(nome)
                self.validar_cargo(cargo)
                self.validar_salario(salario)
                self.validar_email(email)
                return {"nome": nome, "cargo": cargo, "salario": salario, "email": email}
            except EntradaInvalidaException as b:
                sg.popup_error(f"{b.mensagem}")

    def seleciona_funcionario(self):
        sg.ChangeLookAndFeel('BlueMono')
        while True:
            layout = [
                [sg.Text('-------- SELECIONAR FUNCIONÁRIO ----------', font=("Arial", 25))],
                [sg.Text('Digite o email do funcionário que deseja selecionar:', font=("Arial", 15))],
                [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.window = sg.Window('Seleciona funcionário').Layout(layout)

            button, values = self.open()
            
            # Se clicar em Cancelar, retorna None
            if button == 'Cancelar' or button is None:
                self.close()
                return None
            
            email = values['email']
            self.close()
            try:
                self.validar_email(email)
                return email
            except EntradaInvalidaException as b:
                sg.popup_error(f"{b.mensagem}")

    def mostra_funcionario(self, dados_funcionario):
        string_todos_funcionarios = ""
        for dado in dados_funcionario:
            string_todos_funcionarios = string_todos_funcionarios + "NOME DO FUNCIONÁRIO: " + str(dado["nome"]) + '\n'
            string_todos_funcionarios = string_todos_funcionarios + "CARGO DO FUNCIONÁRIO: " + str(dado["cargo"]) + '\n'
            string_todos_funcionarios = string_todos_funcionarios + "SALÁRIO DO FUNCIONÁRIO: " + str(dado["salario"]) + '\n'
            string_todos_funcionarios = string_todos_funcionarios + "EMAIL DO FUNCIONÁRIO: " + str(dado["email"]) + '\n\n'
        sg.Popup('-------- LISTA DE FUNCIONÁRIOS ----------', string_todos_funcionarios)

    def validar_nome(self, nome):
        if nome is None or nome == '':
            raise EntradaInvalidaException('Atenção! Vocẽ não preencheu um campo!')
        if any(x.isdigit() for x in nome):
            raise CampoNumericoException()

    def validar_cargo(self, cargo):
        if cargo is None or cargo == '':
            raise EntradaInvalidaException('Atenção! Vocẽ não preencheu um campo!')
        if any(y.isdigit() for y in cargo):
            raise CampoTextoException()

    def validar_salario(self, salario):
        if salario is None or salario == '':
            raise EntradaInvalidaException('Atenção! Vocẽ não preencheu um campo!')
        if any(z.isalpha() for z in salario):
            raise CampoNumericoException()

    def validar_email(self, email):
        if email is None or email == '':
            raise EntradaInvalidaException('Atenção! Vocẽ não preencheu um campo!')
        if not(any(w.isalnum() for w in email)):
            raise CampoTextoException()