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
            string_todos_alunos += "NOME DO ALUNO: " + str(dado["nome"]) + '\n'
            string_todos_alunos += "MATRICULA DO ALUNO: " + str(dado["matricula"]) + '\n'
            string_todos_alunos += "RESPONSAVEL DO ALUNO: " + str(dado["responsavel"]) + '\n'
            string_todos_alunos += "SÉRIE DO ALUNO: " + str(dado["serie"]) + '\n'
            string_todos_alunos += "ALUNO BOLSISTA: " + str(dado["bolsa"]) + '\n'
            string_todos_alunos += "MENSALIDADE DO ALUNO: " + str(dado["mensalidade"]) + '\n'

            if dado["boletim"] is not None:
                medias = [
                    dado["boletim"].media_matematica,
                    dado["boletim"].media_lingua_portuguesa,
                    dado["boletim"].media_geografia,
                    dado["boletim"].media_historia,
                    dado["boletim"].media_ciencias,
                    dado["boletim"].media_artes,
                    dado["boletim"].media_filosofia,
                    dado["boletim"].media_lingua_inglesa,
                    dado["boletim"].media_educacao_fisica
                ]
                media_geral = sum(medias) / len(medias)
                string_todos_alunos += f"MÉDIA GERAL DO ALUNO: {media_geral:.2f}\n"
                string_todos_alunos += f"FREQUÊNCIA: {dado['boletim'].frequencia} dias\n"
                string_todos_alunos += f"SITUAÇÃO: {'Aprovado' if dado['boletim'].aprovado() else 'Reprovado'}\n"
            else:
                string_todos_alunos += "BOLETIM: Não cadastrado\n"
            
            string_todos_alunos += "\n"
        
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
            
            matricula = values['matricula']
            if not matricula:
                raise ValueError("A matrícula não pode estar vazia.")
            
            responsavel = str(values['responsavel'])
            if not responsavel:
                raise ValueError("O responsável não pode estar vazio.")
            
            serie = str(values['serie'])
            bolsa = str(values['bolsa'])
            mensalidade = float(values['mensalidade'])
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
        
        def validar_nota(nota_str, disciplina):
            try:
                nota = float(nota_str)
                if nota < 0 or nota > 10:
                    sg.popup_error(f"Nota de {disciplina} deve estar entre 0 e 10")
                    return False
                return True
            except ValueError:
                sg.popup_error(f"Nota de {disciplina} deve ser um número válido")
                return False

        disciplinas = {
            'semestre_mtm1': 'matemática (1º semestre)',
            'semestre_mtm2': 'matemática (2º semestre)',
            'semestre_lp1': 'língua portuguesa (1º semestre)',
            'semestre_lp2': 'língua portuguesa (2º semestre)',
            'semestre_geo1': 'geografia (1º semestre)',
            'semestre_geo2': 'geografia (2º semestre)',
            'semestre_hst1': 'história (1º semestre)',
            'semestre_hst2': 'história (2º semestre)',
            'semestre_cie1': 'ciências (1º semestre)',
            'semestre_cie2': 'ciências (2º semestre)',
            'semestre_art1': 'artes (1º semestre)',
            'semestre_art2': 'artes (2º semestre)',
            'semestre_fil1': 'filosofia (1º semestre)',
            'semestre_fil2': 'filosofia (2º semestre)',
            'semestre_ing1': 'língua inglesa (1º semestre)',
            'semestre_ing2': 'língua inglesa (2º semestre)',
            'semestre_edf1': 'educação física (1º semestre)',
            'semestre_edf2': 'educação física (2º semestre)'
        }

        for key, disciplina in disciplinas.items():
            if not validar_nota(values[key], disciplina):
                self.close()
                return None

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
            sg.popup_error("Erro na validação das notas. Certifique-se de digitar números válidos.")
            self.close()
            return None
        
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

            if frequencia < 0 or frequencia > 200:
                raise ValueError("A frequência deve ser um número entre 0 e 200 dias")
        
        except ValueError as e:
            self.close()
            raise CampoNumericoException(str(e))
        
        self.close()
        return frequencia
