import PySimpleGUI as sg  # type: ignore

def new_window():
  sg.theme('DarkBlue4')

  col1 = [
    [sg.Text('DEPOSITAR: ', font= 'Arial 13 bold'), 
     sg.Input('', size=20, font= 'Arial 13', key='depositar'), 
     sg.Button('DEPOSITAR', font= 'Arial 13', size=11)],
    [sg.Text('SACAR: ', font= 'Arial 13 bold'), 
     sg.Text(' '*5, font= 'Arial 13'), 
     sg.Input('', size=20, font= 'Arial 13', key='sacar'), 
     sg.Button('SACAR', font= 'Arial 13', size=11)],
    [sg.Text('EXTRATO: ', font= 'Arial 13 bold'), 
     sg.Text(' '*39, font= 'Arial 13'), 
     sg.Button('EXTRATO', font= 'Arial 13', size=11)],
    [sg.Text('SAIR: ', font= 'Arial 13 bold'), 
     sg.Text(' '*47, font= 'Arial 13'), 
     sg.Button('SAIR', font= 'Arial 13', size=11)]
  ]
  
  col_out = [
    [sg.Output(background_color= 'White', size=(20, 10), font= 'Arial 14 bold', 
               text_color= 'blue', key= 'saida')]
  ]

  layout = [
    [sg.Column(col1), sg.Column(col_out)],
  ]

  return sg.Window('SYSTEM BANK', layout=layout, finalize=True, resizable=False)