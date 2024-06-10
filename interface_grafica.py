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
    [sg.Text('', font= 'Ubuntu 13 bold')],
    [sg.Button('Fazer Login', size=15, font= 'Ubuntu 12 bold', pad=(20,0,0,0), 
               button_color='Yellow'),
     sg.Button('VOLTAR', size=15, font= 'Ubuntu 12 bold', pad=(20,0,0,0))]
  ]

  layout = [
    [sg.Column(coluna1)]
  ]

  return sg.Window('Login System Bank', layout=layout, finalize=True, 
                   resizable=False)


# Criando janela de cadastro de novos usuários
def new_user_window():
  sg.theme('DarkBlack')
  col_principal = [
    [sg.Text('', font='Ubuntu 13 bold')],
    [sg.Text('Nome:\t\t\t\t', font= 'Ubuntu 13 bold', pad=(40,0,0,0)),
     sg.Input('', size=30, font= 'Ubuntu 13 bold', key='nome')],
    [sg.Text('Data de Nascimento:\t\t', font= 'Ubuntu 13 bold', pad=(40,0,0,0)),
     sg.Input('', key='dia', size=3, font= 'Ubuntu 13 bold'), 
     sg.Text('/', font='Ubuntu 13 bold'),
     sg.Input('', key='mes', size=3, font= 'Ubuntu 13 bold'),
     sg.Text('/', font='Ubuntu 13 bold'),
     sg.Input('', key='ano', size=5, font= 'Ubuntu 13 bold')],
    [sg.Text('CPF:\t\t\t\t', font= 'Ubuntu 13 bold', pad=(40,0,0,0)),
     sg.Input('', size=30, font= 'Ubuntu 13 bold', key='cpf')],
    [sg.Text('Endereço:\t\t\t', font= 'Ubuntu 13 bold', pad=(40,0,0,0)),
     sg.Input('', size=30, font= 'Ubuntu 13 bold', key='endereco')],
    [sg.Text('Senha:\t\t\t\t', font= 'Ubuntu 13 bold', pad=(40,0,0,0)),
     sg.Input('', size=30, font= 'Ubuntu 13 bold', password_char='*', 
              key='senha')],
    [sg.Text('', font= 'Ubuntu 13 bold')],
    [sg.Button('CADASTRAR', font= 'Ubuntu 13 bold', size=15, pad=(20,0,0,0)),
     sg.Button('LISTAR USUÁRIOS', font= 'Ubuntu 13 bold', size=15, 
               pad=(20,0,0,0)),
     sg.Button('GERAR CONTA', font= 'Ubuntu 13 bold', size=15, pad=(20,0,0,0)),
     sg.Button('VOLTAR', font= 'Ubuntu 13 bold', size=15, pad=(20,0,0,0))]
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


# Criando janela de usuarios
def list_of_users():
  sg.theme('DarkBlue4')
  col_out = [
    [sg.Output(background_color= 'White', size=(40, 10), font= 'Ubuntu 14 bold', 
               text_color= 'blue', key= 'saida_lista_usuarios')],
    [sg.Button('ATUALIZAR', font= 'Ubuntu 13 bold', size=11, pad=(60,0,0,0)),
     sg.Button('VOLTAR', font= 'Ubuntu 13 bold', size=11, pad=(20,0,0,0))]
  ]

  layout = [
    [sg.Column(col_out)]
  ]
  return sg.Window('LIST OF USER SYSTEM BANK', layout=layout, finalize=True)


# Criando janela de inicialização
def initial_window():
  sg.theme('DarkTeal12')

  col1 = [
    [sg.Text('', font='Ubuntu 13 bold')],
    [sg.Text('ABRIR CADASTRO DE NOVO USUÁRIO\t', font='Ubuntu 11 bold'), 
     sg.Button('NEW USER', font='Ubuntu 11 bold', size=17, 
               button_color="Teal")],
    [sg.Text('', font='Ubuntu 13 bold')],
    [sg.Text('ABRIR SISTEMA DE TRANSFERENCIA\t', font='Ubuntu 11 bold'), 
     sg.Button('SYSTEM TRANSFERS', font='Ubuntu 11 bold', size=17, 
               button_color="purple")],
    [sg.Text('', font='Ubuntu 13 bold')]
  ]

  layout = [
    [sg.Column(col1)]
  ]

  return sg.Window('INITIAL SYSTEM BANK', layout=layout, finalize=True)


# Criando janela para gerar conta
def gerator_of_account_bank():
  sg.theme('DarkBlue3')

  col = [
    [sg.Text('CPF', font='Ubuntu 11 bold'), 
     sg.Input('', font='Ubuntu 11 bold', key='cpf_account')],
    [sg.Button('GERAR', font='Ubuntu 11 bold', pad=(185, 0, 0))]
  ]

  layout = [
    [sg.Column(col)]
  ]

  return sg.Window('Gerator Account Bank', layout=layout, finalize=True)