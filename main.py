# type: ignore
# Importando métodos das funcionalidades da interface gráfica.py
from interface_grafica import *  # noqa: F403
from metodos import *  # noqa: F403


# Janela de inicialização do programa 
initial_window()  # noqa: F405
while True:
  window, events, values = sg.read_all_windows()  # noqa: F405
  if events == sg.WINDOW_CLOSED:  # noqa: F405
    break
  
  # Janela de transações
  elif events == "SYSTEM TRANSFERS":
    # Tela de Login
    login_window()  # noqa: F405
    window.close()

    # Laço de eventos da janela de login
    while True:
      window, events, values = sg.read_all_windows()  # noqa: F405
        
      # Verificação de acesso da tela de login
      if events == "Fazer Login":
        usuario = values['user'].strip()
        senha = values['pwd'].strip()
        if usuario == "q" and senha == "q":
          sg.popup(f"Bem vindo!\n\t{usuario}",  # noqa: F405
                   font='Ubuntu 13 bold', auto_close=True, no_titlebar=True, 
                   button_type=5, background_color="#fff", text_color="#333")
          
          # Janela para realizar as transações bancária do usuário
          transfers_window()  # noqa: F405
          window.close()

          # Variáveis para as funções de transação.
          AGENCIA = "0001"
          LIMITE_SAQUES = 3

          saldo = 0
          limite = 500
          extrato = ""
          numero_saques = 0
          contas = []   

          # Laço de eventos da janela de transações
          while True:
            window, events, values = sg.read_all_windows()  # noqa: F405

            if events == "DEPOSITAR":
              try:
                valor_depositar = float(values['depositar'].replace(',', '.'))
                window['saida'].update('')
                window['depositar'].update('')
                window['depositar'].set_focus()
                
                saldo, extrato = depositar(saldo,\
                                           valor_depositar,\
                                           extrato)  # noqa: F405

              except:  # noqa: E722
                sg.popup("Algo deu errado!\n"   # noqa: F405
                        "Verifique se está pressionando o botão correto. \
                        Este campo só aceita números.", font= "Ubuntu 11 bold", 
                        auto_close=True, no_titlebar=True, button_type=5, 
                        background_color="#fff", text_color="#333")

            elif events == "SACAR":
              try:
                valor_sacar = float(values['sacar'].replace(',', '.'))
                window['saida'].update('')
                window['sacar'].update('')
                
                saldo, extrato = saque(saldo=saldo,   # noqa: F405
                                       valor_sacar=valor_sacar,
                                       limite=limite, extrato=extrato, 
                                       numero_saques=numero_saques, 
                                       limite_saques=LIMITE_SAQUES)
                numero_saques += 1
              except Exception as e:  # noqa: E722
                print(e)
                sg.popup("Algo deu errado!\n"  # noqa: F405
                          "Verifique se está pressionando o botão correto. \
                          Este campo só aceita números.", 
                          no_titlebar=True, auto_close=True, button_type=5,
                          font='Ubuntu 11 bold')

            elif events == "EXTRATO":
              try:
                window['saida'].update('')
                exibir_extrato(saldo, extrato=extrato)  # noqa: F405
              except:  # noqa: E722
                sg.popup("Algo deu errado!\n"  # noqa: F405
                        "Verifique se está pressionando o botão correto.", 
                        font= "Ubuntu 11 bold", auto_close=True, 
                        no_titlebar=True, button_type=5, 
                        background_color="#fff", text_color="#333")

            elif events == sg.WINDOW_CLOSED or "SAIR":  # noqa: F405
              login_window() # noqa: F405
              window.close()
              break

            else:
              sg.popup("Operação inválida!\n"  # noqa: F405
                      "Por favor selecione novamente a operação desejada.",
                      font= "Arial 13 bold", auto_close=True, no_titlebar=True, 
                      button_type=5, background_color="#fff", text_color="#333")
        else:
          sg.popup("Algo deu errado!\n"  # noqa: F405
                  "Verifique seus dados ou crie um novo usuário", 
                  font= "Ubuntu 11 bold", auto_close=True, no_titlebar=True, 
                  button_type=5, background_color="#fff", text_color="#333")
          window['user'].set_focus()

      elif events == sg.WINDOW_CLOSED or "VOLTAR":  # noqa: F405
        initial_window()  # noqa: F405
        window.close()
        break

  # Janela de cadastro de novos usuários
  elif events == "NEW USER":
    new_user_window()  # noqa: F405
    window.close()
  
    # Laço de eventos da janela de cadastro novos usuários
    while True:
      window, events, values = sg.read_all_windows()  # noqa: F405

      if events == "CADASTRAR":
        # Limpando as informações inseridas na tela
        window["nome"].update('')
        window["dia"].update('')
        window["mes"].update('')
        window["ano"].update('')
        window["cpf"].update('')
        window["endereco"].update('')
        window["senha"].update('')
        window["nome"].set_focus()

        # Limpando os espaços vazios da direita e da esquerda dos # campos de
        # inserção
        nome = values["nome"].strip()
        dia = values["dia"].strip()
        mes = values["mes"].strip()
        ano = values["ano"].strip()
        cpf = values["cpf"].strip()
        endereco = values["endereco"].strip()
        senha = values["senha"].strip()

        # Função para cadastrar novos usuários
        inserir_usuario(nome, dia, mes, ano, cpf, endereco, senha)  # noqa: F405

  
      # Chamando janela da lista de usuários
      elif events == "LISTAR USUÁRIOS":
        list_of_users() # noqa: F405
        window.close()

        # Laço de eventos da janela de lista de usuários
        while True:
          window, events, values = sg.read_all_windows()  # noqa: F405

          if events == "USUÁRIOS":
            try:
              window['saida_lista_usuarios'].update('')
              listar_usuarios()  # noqa: F405
            except Exception as erro:
              print(erro)

          elif events == "CONTAS":
            try:
              window['saida_lista_usuarios'].update('')
              listar_contas()  # noqa: F405
            except Exception as erro:
              print(erro)

        # Eventos para retornar a interface de cadastro de usuarios
          elif events == sg.WINDOW_CLOSED or "VOLTAR":  # noqa: F405
            new_user_window()  # noqa: F405
            window.close()
            break


      # Chamando janela de gerar conta bancária
      elif events == "GERAR CONTA":
        gerator_of_account_bank()  # noqa: F405
        window.close()

        AGENCIA = "0001"
        numero_conta = 0
        # contas = []

        # Laço de eventos da janela de gerar conta bancária
        while True:
          window, events, values = sg.read_all_windows()  # noqa: F405
          cpf_account = values["cpf_account"]

          if events == "GERAR":
              try:
                numero_conta += 1
                criar_conta(AGENCIA, numero_conta, cpf_account)  # noqa: F405
              except Exception as erro:
                print(erro)
                
          elif events == sg.WINDOW_CLOSED:  # noqa: F405
            new_user_window()  # noqa: F405
            window.close()
            break

          
      # Eventos para retornar a interface de inicialização
      elif events == sg.WINDOW_CLOSED or "VOLTAR":  # noqa: F405
        initial_window()  # noqa: F405
        window.close()
        break
