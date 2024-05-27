import PySimpleGUI as sg  # type: ignore

def login_window():
  sg.theme('DarkBlack')
  coluna1 = [
    [sg.Text('Usuário:\t\t', font= 'Ubuntu 13 bold'),
     sg.Input('', size=20, font= 'Ubuntu 13 bold', key='user')],
    [sg.Text('Senha:\t\t', font= 'Ubuntu 13 bold'),
     sg.Input('', size=20, font= 'Ubuntu 13 bold', key='pwd', password_char='*')],
    [sg.Button('Fazer Login', size=15, font= 'Ubuntu 12 bold', pad=(20,0,0,0), button_color='Yellow'),
     sg.Button('Novo Usuário', size=15, font= 'Ubuntu 12 bold', pad=(20,0,0,0))]
  ]

  layout = [
    [sg.Column(coluna1)]
  ]

  return sg.Window('Login System Bank', layout=layout, 
                   finalize=True, resizable=False)


def new_user_window():
  sg.theme('DarkBlack')
  col_principal = [
    [sg.Text('Nome:\t\t\t', font= 'Ubuntu 13 bold'),
     sg.Input('', size=30, font= 'Ubuntu 13 bold', key='nome')],
    [sg.Text('Data de Nascimento:\t', font= 'Ubuntu 13 bold'),
     sg.Input('', size=30, font= 'Ubuntu 13 bold', key='data_nasc')],
    [sg.Text('CPF:\t\t\t', font= 'Ubuntu 13 bold'),
     sg.Input('', size=30, font= 'Ubuntu 13 bold', key='CPF')],
    [sg.Text('Endereço:\t\t', font= 'Ubuntu 13 bold'),
     sg.Input('', size=30, font= 'Ubuntu 13 bold', key='Endereço')],
    [sg.Text('Senha:\t\t\t', font= 'Ubuntu 13 bold'),
     sg.Input('', size=30, font= 'Ubuntu 13 bold', key='Senha')],
    [sg.Button('CADASTRAR', font= 'Ubuntu 13 bold', size=14, pad=(70,0,0,0)),
     sg.Button('VOLTAR', font= 'Ubuntu 13 bold', size=14, pad=(0,0,0,0))]
  ]

  layout = [
    [sg.Column(col_principal)]
  ]

  return sg.Window('New user System Bank', layout=layout, finalize=True, 
                   resizable=False)


def transfers_window():
  sg.theme('DarkBlue4')

  col1 = [
    [sg.Text('DEPOSITAR: ', font= 'Ubuntu 13 bold'), 
     sg.Input('', size=20, font= 'Ubuntu 13', key='depositar'), 
     sg.Button('DEPOSITAR', font= 'Ubuntu 13', size=11)],
    [sg.Text('SACAR: ', font= 'Ubuntu 13 bold'), 
     sg.Text(' '*5, font= 'Ubuntu 13'), 
     sg.Input('', size=20, font= 'Ubuntu 13', key='sacar'), 
     sg.Button('SACAR', font= 'Ubuntu 13', size=11)],
    [sg.Text('EXTRATO: ', font= 'Ubuntu 13 bold'), 
     sg.Text(' '*39, font= 'Ubuntu 13'), 
     sg.Button('EXTRATO', font= 'Ubuntu 13', size=11)],
    [sg.Text('SAIR: ', font= 'Ubuntu 13 bold'), 
     sg.Text(' '*47, font= 'Ubuntu 13'), 
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