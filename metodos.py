# type: ignore
from interface_grafica import *  # noqa: F403
import mysql.connector
from datetime import datetime  # noqa: F401

# Conectando ao banco de dados MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123123123"
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
        endereco varchar(30), senha varchar(64), contas int not null auto_increment, \
        primary key(contas)) default charset = utf8mb4'
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
def saque(*, saldo, valor_sacar, extrato, limite, numero_saques, limite_saques):
  try:
    excedeu_saldo = valor_sacar > saldo
    excedeu_limite = valor_sacar > limite
    excedeu_saques = numero_saques >= limite_saques

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
      try:
        saldo -= valor_sacar
        print(f"Saque realizado:\t\tR$ {valor_sacar:.2f}\n")
        extrato += f"Saque:\t\tR$ {valor_sacar:.2f}\n"

      except Exception as erro:
        print(erro)

  except Exception as erro:
    print(erro)
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

# Definição do método de Gerenciamento: Criar Conta
def criar_conta(agencia, numero_conta, cpf_account):
  try:
    if cpf_account and int(cpf_account):
      cursor.execute("select * from usuarios")
      dados = cursor.fetchall()
      for dado in dados:
        if dado[4] == cpf_account:
          try:
            print(dado[4])
            cursor.execute("use myfirstdb")
            cursor.execute(
              "create table if not exists contas (agencia varchar(4),\
              numero_conta int auto_increment,\
                  cpf_account varchar(12),\
                  primary key(numero_conta)) default charset = utf8mb4"
              )
            cursor.execute(
              "insert into contas values (%s, %s, %s)",
              (agencia, numero_conta, cpf_account))
            mydb.commit()
            sg.popup("Conta criada com sucesso:", agencia,  # noqa: F405
                     numero_conta, cpf_account)
          except Exception as erro:
            sg.popup('Ocorreu o seguinte erro:', erro,  # noqa: F405
                     no_titlebar=True, button_type=5, auto_close=True, 
                     font='Ubuntu 11')
      else:
        sg.popup('CPF não cadastrado, verifique novamente.',  # noqa: F405
                no_titlebar=True, button_type=5, auto_close=True,
                font='Ubuntu 11')
      
    else:
      sg.popup('CPF inválido ou campo em branco',  # noqa: F405
                no_titlebar=True, button_type=5, auto_close=True, 
                font='Ubuntu 11')
  except Exception as e:  # noqa: E722
    print(e)
    sg.popup('CPF inválido ou campo em branco',  # noqa: F405
              no_titlebar=True, button_type=5, auto_close=True, 
              font='Ubuntu 11')

# Definição do método de Gerenciamento: Listar Conta
def listar_contas():
  try:
    cursor.execute('SELECT * FROM contas')
    contas = cursor.fetchall()
    for conta in contas:
      script_conta = f"********************************************\n\
Agência:\t\t      Número da Conta:\n\
{conta[0]}\t\t         {conta[1]}\n\n\
CPF:\n{conta[2]}\n\n"
      print(script_conta)
  except Exception as erro:
    sg.popup('Ocorreu o seguinte erro:', erro)  # noqa: F405

# Definição do método de Gerenciamento: Cadastrar usuários
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
      sg.popup(f'Novo usuário inserido com sucesso:\t\t\
              {nome},\nNascido: {dia}/{mes}/{ano},\nResidindo no(a): {endereco}',   # noqa: F405
              text_color='Black', background_color='White', button_type=5, 
              no_titlebar=True, font='Ubuntu 13 bold', auto_close=5)

    else:
      sg.popup('Talvez você tenha feito algo errado.', text_color='Black',  # noqa: F405
                background_color='White', button_type=5, no_titlebar=True, 
                font='Ubuntu 13 bold', auto_close=5)
    
  except mysql.connector.Error as e:
    print(e)
  
# Lista os usuários e o cpf's existentes do banco de dados.
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
  except mysql.connector.Error as e:
    print(e)