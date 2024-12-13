from telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from excecoes.entrada_invalida_exception import *

class TelaProfessor(TelaAbstrata):

    def __init__(self):
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('Professores', font=("Arial", 25))],
            [sg.Text('Escolha sua opção', font=("Arial", 15))],
            [sg.Radio('Incluir professor', "RD1", key='1')],
            [sg.Radio('Alterar professor', "RD1", key='2')],
            [sg.Radio('Excluir professor', "RD1", key='3')],
            [sg.Radio('Listar professores', "RD1", key='4')],
            [sg.Radio('Mostrar professor por email', "RD1", key='5')],  # Nova opção
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
        if values['5']:  # Adicionar condição para a nova opção
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
            [sg.Text('Série:', size=(15, 1)), sg.Combo(
                [f'{i}° ano' for i in range(1, 10)], 
                default_value='1° ano', 
                key='serie', 
                readonly=True)],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Professores').Layout(layout)

        button, values = self.open()
        
        if button in (None, 'Cancelar'):
            self.close()
            return None
        
        try:
            if not values["nome"].replace(' ', '').isalpha():
                raise CampoTextoException("Nome deve conter apenas letras")
            
            try:
                float(values["salario"])
            except ValueError:
                raise CampoNumericoException("Salário deve ser um número")
            
            if not values["leciona"].replace(' ', '').isalpha():
                raise CampoTextoException("Matéria deve conter apenas letras")
            
            if '@' not in values["email"] or '.' not in values["email"]:
                raise ValueError("Email inválido")
        
        except (CampoNumericoException, CampoTextoException, ValueError) as e:
            sg.popup_error(str(e))
            self.close()
            return None
        
        nome = values["nome"]
        salario = values["salario"]
        leciona = values["leciona"]
        email = values["email"]
        serie = values["serie"]
        self.close()
        
        return {
            "nome": nome, 
            "salario": salario, 
            "leciona": leciona, 
            "email": email, 
            "serie": serie
        }

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
        
        
        if button in (None, 'Cancelar'):
            self.close()
            return None
        
        email = values['email']
        self.close()
        return email

    def mostra_professor(self, dados_professor):
        string_todos_professores = ""
        for dado in dados_professor:
            string_todos_professores = string_todos_professores + "NOME DO PROFESSOR: " + str(dado["nome"]) + '\n'
            string_todos_professores = string_todos_professores + "SALÁRIO DO PROFESSOR: " + str(dado["salario"]) + '\n'
            string_todos_professores = string_todos_professores + "MATÉRIA QUE PROFESSOR LECIONA: " + str(dado["leciona"]) + '\n'
            string_todos_professores = string_todos_professores + "EMAIL DO PROFESSOR: " + str(dado["email"]) + '\n'
            string_todos_professores = string_todos_professores + "SÉRIE DO PROFESSOR: " + str(dado["serie"]) + '\n\n'
        sg.Popup('-------- LISTA DE PROFESSORES ----------', string_todos_professores)