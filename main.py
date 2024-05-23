from interface_grafica import *  # noqa: F403

new_window()  # noqa: F405
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  window, events, values = sg.read_all_windows()  # noqa: F405

  if events == "DEPOSITAR":
    try:
      depositar = float(values['depositar'].replace(',', '.'))

      if depositar > 0:
        saldo += depositar  # type: ignore
        window['saida'].update('')
        window['depositar'].update('')
        print(f"Depósito: R$ {depositar:.2f}\n")
        extrato += f"Depósito: R$ {depositar:.2f}\n"

      else:
        sg.popup("Operação falhou! O valor informado é inválido.", title='Info')  # noqa: F405

    except:  # noqa: E722
      sg.popup("Algo deu errado! Verifique se está pressionando o botão correto. \
        Só aceita números.", title='Erro')

  elif events == "SACAR":
    try:
      sacar = float(values['sacar'].replace(',', '.'))

      excedeu_saldo = sacar > saldo
      excedeu_limite = sacar > limite
      excedeu_saques = numero_saques >= LIMITE_SAQUES

      window['saida'].update('')
      window['sacar'].update('')

      if excedeu_saldo:
        sg.popup("Operação falhou! Você não tem saldo suficiente.", title='Info')  # noqa: F405
      
      elif excedeu_limite:
        sg.popup("Operação falhou! O valor do saque excede o limite.", title='Info')  # noqa: F405
      
      elif excedeu_saques:
        sg.popup("Operação falhou! Número máximo de saques excedido.", title='Info')  # noqa: F405

      elif sacar > 0:
        saldo -= sacar  # type: ignore
        print(f"Saque: R$ {sacar:.2f}\n")
        extrato += f"Saque: R$ {sacar:.2f}\n"
        numero_saques += 1
      
      else:
        sg.popup("Operação falhou! O valor informado é inválido.", title='Info')  # noqa: F405

    except:  # noqa: E722
      sg.popup("Algo deu errado! Verifique se está pressionando o botão correto. \
        Só aceita números.", title='Erro')  # noqa: F405

  elif events == "EXTRATO":
    window['saida'].update('')
    print("\n===== EXTRATO =====")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===================")

  elif events == "SAIR":
    break

  elif events == sg.WINDOW_CLOSED:  # noqa: F405
    break

  else:
    sg.popup("Operação inválida, por favor selecione novamente a operação desejada.",   # noqa: F405
             title='Info')
