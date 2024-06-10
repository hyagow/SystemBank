# type: ignore
from interface_grafica import *  # noqa: F403
import mysql.connector
from datetime import datetime  # noqa: F401


# Conectando ao banco de dados MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123123123"
    # database="myfirstdb"
)
cursor = mydb.cursor()
cursor.execute(
    'CREATE DATABASE IF NOT EXISTS myfirstdb \
      default character set utf8mb4 default collate utf8mb4_general_ci'
    )
cursor.execute(
  'USE myfirstdb'
)
cursor.execute(
  'CREATE TABLE IF NOT EXISTS usuarios(nome varchar(30) not null, \
        dia varchar(2) not null, mes varchar(2) not null, \
        ano varchar(4) not null, cpf varchar(11) not null, \
        endereco varchar(30), senha varchar(64)) default charset = utf8mb4'
)

# Definição do método de Transação: Depositar
def depositar(saldo, valor_depositar, extrato, /):
  if valor_depositar > 0:
        saldo += valor_depositar
        print(f"Depósito:\t\tR$ {valor_depositar:.2f}\n")
        extrato += f"Depósito:\t\tR$ {valor_depositar:.2f}\n"

  else:
    sg.popup("Operação falhou! O valor informado é inválido.",  # noqa: F405
              title='Info')
  return saldo, extrato

# Definição do método de Transação: Sacar
def saque(*, valor_sacar, saldo, limite, extrato, numero_saques, limite_saques):
  excedeu_saldo = valor_sacar > saldo
  excedeu_limite = valor_sacar > limite
  excedeu_saques = numero_saques > limite_saques

  if excedeu_saldo:
    sg.popup("Operação falhou! Você não tem saldo suficiente.",  # noqa: F405
             no_titlebar=True, auto_close=True, button_type=5, 
             font='Ubuntu 11 bold')
  
  elif excedeu_limite:
    sg.popup("Operação falhou! O valor do saque excede o limite.",  # noqa: F405
             no_titlebar=True, auto_close=True, button_type=5, 
             font='Ubuntu 11 bold')
  
  elif excedeu_saques:
    sg.popup("Operação falhou! Número máximo de saques excedido.",  # noqa: F405
             no_titlebar=True, auto_close=True, button_type=5, 
             font='Ubuntu 11 bold')
    
  elif valor_sacar > 0:
    saldo -= valor_sacar
    print(f"Saque realizado:\t\tR$ {valor_sacar:.2f}\n")
    extrato += f"Saque:\t\tR$ {valor_sacar:.2f}\n"
    numero_saques += 1

  else:
    sg.popup("Operação falhou! O valor informado é inválido.",  # noqa: F405
             no_titlebar=True, auto_close=True, button_type=5, 
             font= 'Ubuntu 11 bold')

  return saldo, extrato

# Definição do método de Transação: Extrato
def exibir_extrato(saldo, /, *, extrato):
  print("\n========== EXTRATO ==========")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print(f"\nSaldo: R$ {saldo:.2f}")
  print("=============================")

"""# Definição do método de Gerenciamento: Criação de Usuário
  
          # sg.popup(f"USUÁRIO CADASTRADO:\n\n"  # noqa: F405
          #         f"Usuário: {usuarios['cliente_nome']},\n"
          #         f"Data de Nascimento: {usuarios['cliente_data_nasc']},\n"
          #         f"CPF: {usuarios['cliente_cpf']},\n"
          #         f"Endereço: {usuarios['cliente_endereco']},\n"
          #         f"Senha: {usuarios['senha']}", font='Ubuntu 13 bold', 
          #         no_titlebar=True, button_type=5, background_color='White', 
          #         text_color='Black', auto_close=10)"""

# Definição do método de Gerenciamento: Criar Conta
def criar_conta(agencia, numero_conta, usuarios):
  pass

# Definição do método de Gerenciamento: Listar Conta
def listar_conta(contas):
  pass

# Criação do método de Armazenamento: Banco de dados e Tabela
# def create_mydb_and_table_defaults():
#   cursor.execute(
    
#     )
#   mydb.commit()

def inserir_usuario(nome, dia, mes, ano, cpf, endereco, senha):
  try:
    # Variáveis de requisitos
    requisito_senha = 8
    requisito_char_dia_mes = 2
    requisito_char_ano = 4
    requisito_char_cpf = 11
    nome.strip()
    dia.strip()
    mes.strip()
    ano.strip()
    cpf.strip()
    endereco.strip()
    senha.strip()

    if nome and str(nome) and int(dia) and int(mes) <= 12 and int(ano) \
      and int(cpf) and dia and mes and ano and cpf and endereco and senha \
      and len(senha) >= requisito_senha \
      and len(dia) == requisito_char_dia_mes \
      and len(mes) == requisito_char_dia_mes \
      and len(ano) == requisito_char_ano \
      and len(cpf) == requisito_char_cpf:
      cursor.execute('USE myfirstdb')
      cursor.execute(
        "INSERT INTO usuarios (nome, dia, mes, ano, cpf, endereco, senha) \
          VALUES (%s, %s, %s, %s, %s, %s, %s)", \
            (nome, dia, mes, ano, cpf, endereco, senha)
        )
      mydb.commit()
        # 'INSERT INTO usuarios VALUES (nome="'+str(nome)+'", dia="'+str(dia)+'", \
        #   mes="'+str(mes)+'", ano="'+str(ano)+'", cpf="'+str(cpf)+'", \
        #     endereco="'+str(endereco)+'", senha="'+str(senha)+'");')
      #print(query)
      sg.popup(f'Novo usuário inserido com sucesso:\t\t\
              {nome}, {dia}/{mes}/{ano}, {endereco}',   # noqa: F405
              text_color='Black', background_color='White', button_type=5, 
              no_titlebar=True, font='Ubuntu 13 bold', auto_close=5)

    else:
      sg.popup('Talvez você tenha feito algo errado.', text_color='Black',  # noqa: F405
                background_color='White', button_type=5, no_titlebar=True, 
                font='Ubuntu 13 bold', auto_close=5)
    
  except mysql.connector.Error as e:
    print(e)
  
#TODO: Verificação se existe o usuario e o cpf dentro do banco de dados.
#FIXME: Onde será chamada? Login? Por quem? ADMIN?
def listar_usuarios():
  try:
    cursor.execute("USE myfirstdb")
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    for u in usuarios:
      script = f"********************************************\n\
Usuário:\t\t      Data de Nascimento:\n\
{u[0]}\t\t         {u[1]}/{u[2]}/{u[3]}\n\n\
CPF:\n{u[4]}\n\n\
Endereço:\n{u[5]}\n\n\
Senha:\n{u[6]}\n\n"
      print(script)
    # print(usuarios)  # noqa: F405
  except mysql.connector.Error as e:
    print(e)