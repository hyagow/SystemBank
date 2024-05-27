# type: ignore
from interface_grafica import *  # noqa: F403
from metodos import *  # noqa: F403

login_window()  # noqa: F405
lista_usuario = {
  # Neste dicionário será inserido os dados cadastrais dos usuários
}
while True:
  window, events, values = sg.read_all_windows()  # noqa: F405
  if events == sg.WINDOW_CLOSED:  # noqa: F405
    break

  if events == "Fazer Login":
    usuario = values['user'].strip()
    senha = values['pwd'].strip()
    if usuario == "teste" and senha == "teste":
      sg.popup(f"Bem vindo!\t\t{usuario}", font='Arial 19 bold',   # noqa: F405
              auto_close=True, no_titlebar=True, button_type=5, 
              background_color="#fff", text_color="#333")
      window.close()
      transfers_window()  # noqa: F405
      saldo = 0
      limite = 500
      extrato = ""
      numero_saques = 0
      LIMITE_SAQUES = 3

      while True:
        window, events, values = sg.read_all_windows()  # noqa: F405

        if events == "DEPOSITAR":
          try:
            valor_depositar = float(values['depositar'].replace(',', '.'))
            window['saida'].update('')
            window['depositar'].update('')
            saldo, extrato = depositar(saldo, valor_depositar, extrato)  # noqa: F405

          except:  # noqa: E722
            sg.popup("Algo deu errado!\n"   # noqa: F405
                    "Verifique se está pressionando o botão correto. \
                    Este campo só aceita números.", title='Erro')

        elif events == "SACAR":
          try:
            valor_sacar = float(values['sacar'].replace(',', '.'))
            window['saida'].update('')
            window['sacar'].update('')
            
            saldo, extrato = saque(valor_sacar=valor_sacar, saldo=saldo,  # noqa: F405
                                  limite=limite, extrato=extrato,
                                  numero_saques=numero_saques,
                                  limite_saques=LIMITE_SAQUES
                                  )
          except:  # noqa: E722
            sg.popup("Algo deu errado!\n"  # noqa: F405
                      "Verifique se está pressionando o botão correto. \
                      Este campo só aceita números.", title='Erro')

        elif events == "EXTRATO":
          try:
            window['saida'].update('')
            exibir_extrato(saldo, extrato=extrato)  # noqa: F405
          except:  # noqa: E722
            sg.popup("Algo deu errado!\n"  # noqa: F405
                    "Verifique se está pressionando o botão correto.", 
                    title='Erro')

        elif events == "SAIR":
          window.close()
          break

        elif events == sg.WINDOW_CLOSED:  # noqa: F405
          break

        else:
          sg.popup("Operação inválida!\n"  # noqa: F405
                  "Por favor selecione novamente a operação desejada.",
                  title='Info')
    else:
      sg.popup("Algo deu errado!\n"  # noqa: F405
              "Verifique seus dados ou crie um novo usuário", 
              font= "Arial 13 bold", auto_close=True, no_titlebar=True, 
              button_type=5, background_color="#fff", text_color="#333")

  if events == "Novo Usuário":
    new_user_window()  # noqa: F405

    while True:
      window, events, values = sg.read_all_windows()  # noqa: F405
      if events == sg.WINDOW_CLOSED:  # noqa: F405
        window.close()
        break

      if events == "CADASTRAR":
        nome = values["nome"].strip()
        data_nasc = values["data_nasc"].strip()
        cpf = values["cpf"].strip()
        endereço = values["endereço"].strip()
        senha = values["senha"].strip()

        caracteres_minimos = 8
        requisito_cpf = 11

        if nome and str(nome) \
          and data_nasc and len(data_nasc) == caracteres_minimos \
          and len(cpf) == requisito_cpf and int(cpf) and cpf and endereço \
          and senha:
          sg.popup(f'{nome}, {data_nasc}, {cpf}, {endereço}.')  # noqa: F405
        else:
          sg.popup('Preencha todos os campos!\n'\
                   'Verifique se os campos atendem aos requisitos:\n'\
                   'Nome: ---------------> [Letras]\n'\
                   'Data Nascimento: -> [Números[Quantidade: 8]]\n'\
                   'CPF: -----------------> [Números[Quantidade: 11]]\n'\
                   'Senha: --------------> [Mínimo: 8 dígitos]',  # noqa: F405
                   font='Ubuntu 13 bold', auto_close=True, no_titlebar=True, 
                   auto_close_duration=15, button_type=5, 
                   background_color="#fff", text_color="#333")


      if events == "VOLTAR":
        window.close()
        break
