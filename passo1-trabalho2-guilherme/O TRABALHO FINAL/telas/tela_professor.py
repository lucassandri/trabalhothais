from telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaProfessor(TelaAbstrata):

    def __init__(self):
        self.init_components()

    def init_components(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('Professores', font=("Arial", 25))],
            [sg.Text('Escolha sua opção', font=("Arial", 15))],
            [sg.Radio('Incluir professor', "RD1", key='1')],
            [sg.Radio('Alterar professor', "RD1", key='2')],
            [sg.Radio('Excluir professor', "RD1", key='3')],
            [sg.Radio('Listar professores', "RD1", key='4')],
            [sg.Radio('Mostrar professor por email', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Professores').Layout(layout)

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

    def pega_dados_professor(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('-------- DADOS PROFESSOR ----------', font=("Arial", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Salário:', size=(15, 1)), sg.InputText('', key='salario')],
            [sg.Text('Leciona:', size=(15, 1)), sg.InputText('', key='leciona')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Professores').Layout(layout)

        button, values = self.open()
        nome = values["nome"]
        salario = values["salario"]
        leciona = values["leciona"]
        email = values["email"]
        self.close()
        return {"nome": nome, "salario": salario, "leciona": leciona, "email": email}

    def seleciona_professor(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('-------- SELECIONAR PROFESSOR ----------', font=("Arial", 25))],
            [sg.Text('Digite o email do professor que deseja selecionar:', font=("Arial", 15))],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Seleciona professor').Layout(layout)

        button, values = self.open()
        email = values['email']
        self.close()
        return email

    def mostra_professor(self, dados_professor):
        string_todos_professores = ""
        for dado in dados_professor:
            string_todos_professores = string_todos_professores + "NOME DO PROFESSOR: " + str(dado["nome"]) + '\n'
            string_todos_professores = string_todos_professores + "SALÁRIO DO PROFESSOR: " + str(dado["salario"]) + '\n'
            string_todos_professores = string_todos_professores + "MATÉRIA QUE PROFESSOR LECIONA: " + str(dado["leciona"]) + '\n'
            string_todos_professores = string_todos_professores + "EMAIL DO PROFESSOR: " + str(dado["email"]) + '\n\n'
        sg.Popup('-------- LISTA DE PROFESSORES ----------', string_todos_professores)
