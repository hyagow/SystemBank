from PySimpleGUI import PySimpleGUI as sg  # type: ignore

# Criando janela de login
def login_window():
  sg.theme('DarkBlack')
  coluna1 = [
    [sg.Text('Usuário:\t\t', font= 'Ubuntu 13 bold'),
     sg.Input('', size=20, font= 'Ubuntu 13 bold', key='user')],
    [sg.Text('Senha:\t\t', font= 'Ubuntu 13 bold'),
     sg.Input('', size=20, font= 'Ubuntu 13 bold', key='pwd', 
              password_char='*')],
    [sg.Button('Fazer Login', size=15, font= 'Ubuntu 12 bold', pad=(20,0,0,0), 
               button_color='Yellow'),
     sg.Button('Novo Usuário', size=15, font= 'Ubuntu 12 bold', pad=(20,0,0,0)),
     sg.Button('LISTAR USUÁRIOS', size=15, 
               font= 'Ubuntu 12 bold', pad=(20,0,0,0), button_color='#8cbfe6')]
  ]

  layout = [
    [sg.Column(coluna1)]
  ]

  return sg.Window('Login System Bank', layout=layout, finalize=True, 
                   resizable=False)


# Criando janela de novos usuários
def new_user_window():
  sg.theme('DarkBlack')
  col_principal = [
    [sg.Text('Nome:\t\t\t', font= 'Ubuntu 13 bold'),
     sg.Input('', size=30, font= 'Ubuntu 13 bold', key='nome')],
    [sg.Text('Data de Nascimento:\t', font= 'Ubuntu 13 bold'),
     sg.Input('', key='dia', size=3, font= 'Ubuntu 13 bold'),
     sg.Input('', key='mes', size=3, font= 'Ubuntu 13 bold'),
     sg.Input('', key='ano', size=5, font= 'Ubuntu 13 bold')],
    [sg.Text('CPF:\t\t\t', font= 'Ubuntu 13 bold'),
     sg.Input('', size=30, font= 'Ubuntu 13 bold', key='cpf')],
    [sg.Text('Endereço:\t\t', font= 'Ubuntu 13 bold'),
     sg.Input('', size=30, font= 'Ubuntu 13 bold', key='endereco')],
    [sg.Text('Senha:\t\t\t', font= 'Ubuntu 13 bold'),
     sg.Input('', size=30, font= 'Ubuntu 13 bold', password_char='*', 
              key='senha')],
    [sg.Button('CADASTRAR', font= 'Ubuntu 13 bold', size=14, pad=(70,0,0,0)),
     sg.Button('VOLTAR', font= 'Ubuntu 13 bold', size=14, pad=(0,0,0,0))]
  ]

  layout = [
    [sg.Column(col_principal)]
  ]

  return sg.Window('New user System Bank', layout=layout, finalize=True, 
                   resizable=False)


# Criando janela de transações
def transfers_window():
  sg.theme('DarkBlue4')

  col1 = [
    [sg.Text('DEPOSITAR:\t', font= 'Ubuntu 13 bold'), 
     sg.Input('', size=20, font= 'Ubuntu 13', key='depositar'), 
     sg.Button('DEPOSITAR', font= 'Ubuntu 13', size=11)],
    [sg.Text('SACAR:\t\t', font= 'Ubuntu 13 bold'), 
     sg.Input('', size=20, font= 'Ubuntu 13', key='sacar'), 
     sg.Button('SACAR', font= 'Ubuntu 13', size=11)],
    [sg.Text('EXTRATO:\t', font= 'Ubuntu 13 bold'), 
     sg.Button('EXTRATO', font= 'Ubuntu 13', size=11)],
    [sg.Text('SAIR:\t\t', font= 'Ubuntu 13 bold'), 
     sg.Button('SAIR', font= 'Ubuntu 13', size=11)]
  ]
  
  col_out = [
    [sg.Output(background_color= 'White', size=(30, 10), font= 'Ubuntu 14 bold', 
               text_color= 'blue', key= 'saida')]
  ]

  layout = [
    [sg.Column(col1), sg.Column(col_out)]
  ]

  return sg.Window('SYSTEM BANK', layout=layout, finalize=True, resizable=False)


def list_of_users():
  sg.theme('DarkBlue4')
  col1 = [
    
  ]

  col_out = [
    [sg.Output(background_color= 'White', size=(40, 10), font= 'Ubuntu 14 bold', 
               text_color= 'blue', key= 'saida')],
    [sg.Button('ATUALIZAR', font= 'Ubuntu 13', size=11)],
    [sg.Button('VOLTAR', font= 'Ubuntu 13', size=11)]
  ]

  layout = [
    [sg.Column(col1), sg.Column(col_out)]
  ]
  return sg.Window('LIST OF USER SYSTEM BANK', layout=layout, finalize=True)