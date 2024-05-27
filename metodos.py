# type: ignore
from interface_grafica import *  # noqa: F403

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
  excedeu_saques = numero_saques >= limite_saques

  if excedeu_saldo:
    sg.popup("Operação falhou! Você não tem saldo suficiente.", title='Info')  # noqa: F405
  
  elif excedeu_limite:
    sg.popup("Operação falhou! O valor do saque excede o limite.", title='Info')  # noqa: F405
  
  elif excedeu_saques:
    sg.popup("Operação falhou! Número máximo de saques excedido.", title='Info')  # noqa: F405

  elif valor_sacar > 0:
    saldo -= valor_sacar
    print(f"Saque:\t\tR$ {valor_sacar:.2f}\n")
    extrato += f"Saque:\t\tR$ {valor_sacar:.2f}\n"
    numero_saques += 1 

  else:
    sg.popup("Operação falhou! O valor informado é inválido.", title='Info')  # noqa: F405

  return saldo, extrato

# Definição do método de Transação: Extrato
def exibir_extrato(saldo, /, *, extrato):
  print("\n========== EXTRATO ==========")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print(f"\nSaldo: R$ {saldo:.2f}")
  print("=============================")

# Definição do método de Gerenciamento: Criação de Usuário
def criar_usuario(nome, data_nasc, cpf, endereco, senha):
  lista_usuario = {"cliente_nome": nome, "cliente_data_nasc": data_nasc,
                  "cliente_cpf": cpf, "cliente_endereco": endereco, 
                  "senha": senha}

  sg.popup(f'USUÁRIO CADASTRADO:\n\n'  # noqa: F405
          f'Usuário: {lista_usuario["cliente_nome"]},\n'
          f'Data de Nascimento: {lista_usuario["cliente_data_nasc"]},\n'
          f'CPF: {lista_usuario["cliente_cpf"]},\n'
          f'Endereço: {lista_usuario["cliente_endereco"]},\n'
          f'Senha: {lista_usuario["senha"]}', font='Ubuntu 13 bold', 
          no_titlebar=True, button_type=5, background_color='White', 
          text_color='Black', auto_close=10)

# Definição do método de Gerenciamento: Criar Conta
def criar_conta():
  pass

# Definição do método de Gerenciamento: Listar Conta
def listar_conta():
  pass

# Definição do método de Gerenciamento: Listar Usuário
def listar_usuario():
  pass