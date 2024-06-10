# type: ignore
from PySimpleGUI import PySimpleGUI as sg
import mysql.connector

# Conectando ao banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="myfirstdb"
)
cursor = conexao.cursor()

# Layout da interface gráfica
layout = [
    [sg.Text("Nome:"), sg.InputText(key='nome')],
    [sg.Text("Dia:"), sg.InputText(key='dia')],
    [sg.Text("Mes:"), sg.InputText(key='mes')],
    [sg.Text("Ano:"), sg.InputText(key='ano')],
    [sg.Text("CPF:"), sg.InputText(key='cpf')],
    [sg.Text("Endereço:"), sg.InputText(key='endereco')],
    [sg.Text("Senha:"), sg.InputText(key='senha', password_char='*')],
    [sg.Button("Confirmar Cadastro")]
]

# Criando a janela
janela = sg.Window("Cadastro de Usuário").Layout(layout)

# Loop de eventos
while True:
    evento, valores = janela.Read()
    if evento == sg.WINDOW_CLOSED:
        break
    elif evento == "Confirmar Cadastro":
        nome = valores['nome']
        dia = valores['dia']
        mes = valores['mes']
        ano = valores['ano']
        cpf = valores['cpf']
        endereco = valores['endereco']
        senha = valores['senha']
        
        # Inserindo os dados no banco de dados
        try:
            cursor.execute("INSERT INTO usuarios (nome, dia, mes, ano, cpf, endereco, senha) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nome, dia, mes, ano, cpf, endereco, senha))
            conexao.commit()
            sg.popup("Cadastro realizado com sucesso!")
        except mysql.connector.Error as erro:
            sg.popup(f"Erro ao cadastrar: {erro}")

# Fechando a conexão com o banco de dados
conexao.close()
