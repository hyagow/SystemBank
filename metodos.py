# type: ignore
from interface_grafica import *  # noqa: F403

saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, valor_depositar, extrato, /):
  if valor_depositar > 0:
        saldo += valor_depositar
        print(f"Depósito:\t\tR$ {valor_depositar:.2f}\n")
        extrato += f"Depósito:\t\tR$ {valor_depositar:.2f}\n"

  else:
    sg.popup("Operação falhou! O valor informado é inválido.",  # noqa: F405
              title='Info')
  return saldo, extrato

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

def exibir_extrato(saldo, /, *, extrato):
  print("\n========== EXTRATO ==========")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print(f"\nSaldo: R$ {saldo:.2f}")
  print("=============================")

def criar_usuario(nome, data_nasc, cpf, endereco):
  lista_usuario = {"cliente_nome": nome, "cliente_data_nasc": data_nasc,
                    "cliente_cpf": cpf, "cliente_endereco": endereco}
  return print(lista_usuario["cliente_nome"]["cliente_data_nasc"]
               ["cliente_cpf"]["cliente_endereco"])

  # lista_usuario[nome, data_nasc, cpf, endereco]

def criar_conta():
  pass
