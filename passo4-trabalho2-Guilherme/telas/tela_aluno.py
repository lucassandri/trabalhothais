import PySimpleGUI as sg
from telas.tela_abstrata import TelaAbstrata
from excecoes.entrada_invalida_exception import *

class TelaAluno(TelaAbstrata):
    def __init__(self):
        self.init_components()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('-------- ALUNOS ----------', font=("Arial", 25))],
            [sg.Text('Escolha sua opção', font=("Arial", 15))],
            [sg.Radio('Incluir Aluno', "RD1", key='1')],
            [sg.Radio('Alterar Aluno', "RD1", key='2')],
            [sg.Radio('Listar Alunos', "RD1", key='3')],
            [sg.Radio('Excluir Aluno', "RD1", key='4')],
            [sg.Radio('Cadastrar boletim de um aluno', "RD1", key='5')],
            [sg.Radio('Mostrar aluno por matricula', "RD1", key='6')],
            [sg.Radio('Verificar se o aluno está aprovado', "RD1", key='7')],
            [sg.Radio('Alterar boletim de um aluno', "RD1", key='8')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Alunos').Layout(layout)

    def tela_opcoes(self):
        self.init_components()
        button, values = self.open()
        
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
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def seleciona_aluno(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('-------- SELECIONAR ALUNO ----------', font=("Arial", 25))],
            [sg.Text('Digite a matricula do aluno que deseja selecionar:', font=("Arial", 15))],
            [sg.Text('Matricula:', size=(15, 1)), sg.InputText('', key='matricula')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Seleciona aluno').Layout(layout)

        button, values = self.open()
        
        if button in (None, 'Cancelar'):
            self.close()
            return None
        
        matricula = values['matricula']
        self.close()
        return matricula

    def mostra_aluno(self, dados_aluno):
        string_todos_alunos = ""
        for dado in dados_aluno:
            string_todos_alunos = string_todos_alunos + "NOME DO ALUNO: " + str(dado["nome"]) + '\n'
            string_todos_alunos = string_todos_alunos + "MATRICULA DO ALUNO: " + str(dado["matricula"]) + '\n'
            string_todos_alunos = string_todos_alunos + "RESPONSAVEL DO ALUNO: " + str(dado["responsavel"]) + '\n'
            string_todos_alunos = string_todos_alunos + "SÉRIE DO ALUNO: " + str(dado["serie"]) + '\n'
            string_todos_alunos = string_todos_alunos + "ALUNO BOLSISTA: " + str(dado["bolsa"]) + '\n'
            string_todos_alunos = string_todos_alunos + "MENSALIDADE DO ALUNO: " + str(dado["mensalidade"]) + '\n'
            string_todos_alunos = string_todos_alunos + "BOLETIM DO ALUNO: " + str(dado["boletim"]) + '\n\n'
        sg.Popup('-------- LISTA DE ALUNOS ----------', string_todos_alunos)

    def pega_dados_aluno(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('-------- DADOS ALUNO ----------', font=("Arial", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Matricula:', size=(15, 1)), sg.InputText('', key='matricula')],
            [sg.Text('Responsável:', size=(15, 1)), sg.InputText('', key='responsavel')],
            [sg.Text('Série:', size=(15, 1)), sg.Combo(
                [f'{i}° ano' for i in range(1, 10)], 
                default_value='1° ano', 
                key='serie', 
                readonly=True)],
            [sg.Text('Bolsa:', size=(15, 1)), sg.Combo(
                ['Sim', 'Não'], 
                default_value='Não', 
                key='bolsa', 
                readonly=True)],
            [sg.Text('Mensalidade:', size=(15, 1)), sg.InputText('', key='mensalidade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.window = sg.Window('DADOS ALUNO').Layout(layout)

        button, values = self.open()
        
        if button in (None, 'Cancelar'):
            self.close()
            return None

        try:
            nome = str(values['nome'])
            if not nome:
                raise ValueError("O nome não pode estar vazio.")
            
            matricula = int(values['matricula'])  # Deve ser um inteiro
            responsavel = str(values['responsavel'])
            if not responsavel:
                raise ValueError("O responsável não pode estar vazio.")
            
            serie = str(values['serie'])  # Deve ser uma string (já controlado pelo ComboBox)
            bolsa = str(values['bolsa'])   # Converte 'Sim' para True e 'Não' para False
            mensalidade = float(values['mensalidade'])  # Deve ser um número decimal
            if mensalidade < 0:
                raise ValueError("A mensalidade não pode ser negativa.")
        except ValueError as e:
            self.close()
            raise CampoNumericoException(f"Erro na validação dos dados: {e}")

        self.close()
        return {
            "nome": nome, 
            "matricula": matricula, 
            "responsavel": responsavel, 
            "serie": serie, 
            "bolsa": bolsa,
            "mensalidade": mensalidade
        }


    def pega_dados_notas_boletim(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('-------- CADASTRO DE NOTAS ----------', font=("Arial", 25))],
            [sg.Text("Nota do primeiro semestre de matemática do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_mtm1')],
            [sg.Text("Nota do segundo semestre de matemática do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_mtm2')],
            [sg.Text("Nota do primeiro semestre de língua portuguesa do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_lp1')],
            [sg.Text("Nota do segundo semestre de língua portuguesa do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_lp2')],
            [sg.Text("Nota do primeiro semestre de geografia do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_geo1')],
            [sg.Text("Nota do segundo semestre de geografia do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_geo2')],
            [sg.Text("Nota do primeiro semestre de história do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_hst1')],
            [sg.Text("Nota do segundo semestre de história do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_hst2')],
            [sg.Text("Nota do primeiro semestre de ciências do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_cie1')],
            [sg.Text("Nota do segundo semestre de ciências do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_cie2')],
            [sg.Text("Nota do primeiro semestre de artes do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_art1')],
            [sg.Text("Nota do segundo semestre de artes do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_art2')],
            [sg.Text("Nota do primeiro semestre de filosofia do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_fil1')],
            [sg.Text("Nota do segundo semestre de filosofia do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_fil2')],
            [sg.Text("Nota do primeiro semestre de língua inglesa do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_ing1')],
            [sg.Text("Nota do segundo semestre de língua inglesa do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_ing2')],
            [sg.Text("Nota do primeiro semestre de educação física do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_edf1')],
            [sg.Text("Nota do segundo semestre de educação física do aluno: ", size=(15, 1)),
             sg.InputText('', key='semestre_edf2')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.window = sg.Window('DADOS ALUNO').Layout(layout)

        button, values = self.open()
        
        if button in (None, 'Cancelar'):
            self.close()
            return None
        
        semestre_mtm1 = values['semestre_mtm1']
        semestre_mtm2 = values['semestre_mtm2']
        semestre_lp1 = values['semestre_lp1']
        semestre_lp2 = values['semestre_lp2']
        semestre_geo1 = values['semestre_geo1']
        semestre_geo2 = values['semestre_geo2']
        semestre_hst1 = values['semestre_hst1']
        semestre_hst2 = values['semestre_hst2']
        semestre_cie1 = values['semestre_cie1']
        semestre_cie2 = values['semestre_cie2']
        semestre_art1 = values['semestre_art1']
        semestre_art2 = values['semestre_art2']
        semestre_fil1 = values['semestre_fil1']
        semestre_fil2 = values['semestre_fil2']
        semestre_ing1 = values['semestre_ing1']
        semestre_ing2 = values['semestre_ing2']
        semestre_edf1 = values['semestre_edf1']
        semestre_edf2 = values['semestre_edf2']

        media_notas = {"matematica": (semestre_mtm1 + semestre_mtm2) / 2,
                       "lingua_portuguesa": (semestre_lp1 + semestre_lp2) / 2,
                       "geografia": (semestre_geo1 + semestre_geo2) / 2,
                       "historia": (semestre_hst1 + semestre_hst2) / 2, "ciencias": (semestre_cie1 + semestre_cie2) / 2,
                       "artes": (semestre_art1 + semestre_art2) / 2, "filosofia": (semestre_fil1 + semestre_fil2) / 2,
                       "lingua_inglesa": (semestre_ing1 + semestre_ing2) / 2,
                       "educacao_fisica": (semestre_edf1 + semestre_edf2) / 2}
        self.close()
        
        try:
            media_notas = {
            "matematica": (float(values['semestre_mtm1']) + float(values['semestre_mtm2'])) / 2,
            "lingua_portuguesa": (float(values['semestre_lp1']) + float(values['semestre_lp2'])) / 2,
            "geografia": (float(values['semestre_geo1']) + float(values['semestre_geo2'])) / 2,
            "historia": (float(values['semestre_hst1']) + float(values['semestre_hst2'])) / 2,
            "ciencias": (float(values['semestre_cie1']) + float(values['semestre_cie2'])) / 2,
            "artes": (float(values['semestre_art1']) + float(values['semestre_art2'])) / 2,
            "filosofia": (float(values['semestre_fil1']) + float(values['semestre_fil2'])) / 2,
            "lingua_inglesa": (float(values['semestre_ing1']) + float(values['semestre_ing2'])) / 2,
            "educacao_fisica": (float(values['semestre_edf1']) + float(values['semestre_edf2'])) / 2,
        }
        except ValueError:
            raise CampoNumericoException("Nota deve ser um número válido")
        
        self.close()
        return media_notas

    def pega_dados_frequencia_boletim(self):
        sg.ChangeLookAndFeel('BlueMono')
        layout = [
            [sg.Text('-------- CADASTRO DA FREQUÊNCIA ----------', font=("Arial", 25))],
            [sg.Text("Frequência anual do aluno durante o ano letivo (em dias): ", size=(15, 1)),
            sg.InputText('', key='frequencia')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('ALUNO').Layout(layout)
        button, values = self.open()
        
        if button in (None, 'Cancelar'):
            self.close()
            return None
        
        try:
            frequencia = int(values['frequencia'])
        except ValueError:
            self.close()
            raise CampoNumericoException("A frequência deve ser um número inteiro válido.")
        
        self.close()
        return frequencia
