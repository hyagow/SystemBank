# type: ignore
# Importando métodos das funcionalidades da interface gráfica.py
from interface_grafica import initial_window, login_window, new_user_window, transfers_window,\
  list_of_users, gerator_of_account_bank, sg
from metodos import depositar, saque, exibir_extrato, criar_conta, listar_contas, listar_usuarios, \
  inserir_usuario, cursor

# Janela de inicialização do programa
initial_window()
while True:
  window, events, values = sg.read_all_windows()
  if events == sg.WINDOW_CLOSED:
    break
  
  # Janela de transações
  elif events == "SYSTEM TRANSFERS":
    # Tela de Login
    login_window()
    window.close()

    # Laço de eventos da janela de login
    while True:
      window, events, values = sg.read_all_windows()
        
      # Verificação de acesso da tela de login
      if events == "Fazer Login":
        try:
          usuario = values['user'].strip()
          senha = values['pwd'].strip()

          cursor.execute(f"SELECT senha FROM usuarios WHERE nome = '{usuario}'")
          senhas = cursor.fetchall()

          if senha == senhas[0][0]:
            print(f'senhas: {senhas[0][0]}')
            sg.popup(f"Bem vindo!\n\t{usuario.title()}",
                  font='Ubuntu 13 bold', auto_close=True, no_titlebar=True, 
                  button_type=5, background_color="#fff", text_color="#333")
          
            # Janela para realizar as transações bancária do usuário
            transfers_window()
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
              window, events, values = sg.read_all_windows()

              if events == "DEPOSITAR":
                try:
                  valor_depositar = float(values['depositar'].replace(',', '.'))
                  window['saida'].update('')
                  window['depositar'].update('')
                  window['depositar'].set_focus()
                  
                  saldo, extrato = depositar(saldo, valor_depositar, extrato)

                except Exception as e:
                  print(e)
                  sg.popup("Algo deu errado!\n" 
                          "Verifique se está pressionando o botão correto. \
                          Este campo só aceita números.", font= "Ubuntu 11 bold", 
                          auto_close=True, no_titlebar=True, button_type=5, 
                          background_color="#fff", text_color="#333")

              elif events == "SACAR":
                try:
                  valor_sacar = float(values['sacar'].replace(',', '.'))
                  window['saida'].update('')
                  window['sacar'].update('')
                  
                  saldo, extrato = saque(saldo=saldo, valor_sacar=valor_sacar, limite=limite, 
                                          extrato=extrato, numero_saques=numero_saques, 
                                          limite_saques=LIMITE_SAQUES)
                  numero_saques += 1
                except Exception as e:
                  print(e)
                  sg.popup("Algo deu errado!\n"
                            "Verifique se está pressionando o botão correto. \
                            Este campo só aceita números.", 
                            no_titlebar=True, auto_close=True, button_type=5,
                            font='Ubuntu 11 bold')

              elif events == "EXTRATO":
                try:
                  window['saida'].update('')
                  exibir_extrato(saldo, extrato=extrato)
                except Exception as error:
                  sg.popup("Algo deu errado!\n"
                          "Verifique se está pressionando o botão correto.", 
                          font= "Ubuntu 11 bold", auto_close=True, 
                          no_titlebar=True, button_type=5, 
                          background_color="#fff", text_color="#333")
                  print(error)

              elif events == sg.WINDOW_CLOSED or "SAIR":
                login_window()
                window.close()
                break

              else:
                sg.popup("Operação inválida!\n"
                        "Por favor selecione novamente a operação desejada.",
                        font= "Arial 13 bold", auto_close=True, no_titlebar=True, 
                        button_type=5, background_color="#fff", text_color="#333")
        except Exception as e:
          print(e)
          sg.popup("Algo deu errado!\n"
                  "Usuário ou senha incorretos ou não existe.", 
                  font= "Ubuntu 11 bold", auto_close=True, no_titlebar=True, 
                  button_type=5, background_color="#fff", text_color="#333")
          window['user'].set_focus()

      elif events == sg.WINDOW_CLOSED or "VOLTAR":
        initial_window()
        window.close()
        break

  # Janela de cadastro de novos usuários
  elif events == "NEW USER":
    new_user_window()
    window.close()
  
    # Laço de eventos da janela de cadastro novos usuários
    while True:
      window, events, values = sg.read_all_windows()

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
        inserir_usuario(nome, dia, mes, ano, cpf, endereco, senha)

  
      # Chamando janela da lista de usuários
      elif events == "LISTAR USUÁRIOS":
        list_of_users()
        window.close()

        # Laço de eventos da janela de lista de usuários
        while True:
          window, events, values = sg.read_all_windows()

          if events == "USUÁRIOS":
            try:
              window['saida_lista_usuarios'].update('')
              listar_usuarios()
            except Exception as erro:
              print(erro)

          elif events == "CONTAS":
            try:
              window['saida_lista_usuarios'].update('')
              listar_contas()
            except Exception as erro:
              print(erro)

        # Eventos para retornar a interface de cadastro de usuarios
          elif events == sg.WINDOW_CLOSED or "VOLTAR":
            new_user_window()
            window.close()
            break


      # Chamando janela de gerar conta bancária
      elif events == "GERAR CONTA":
        gerator_of_account_bank()
        window.close()

        AGENCIA = "0001"
        numero_conta = 0

        # Laço de eventos da janela de gerar conta bancária
        while True:
          window, events, values = sg.read_all_windows()
          cpf_account = values["cpf_account"]

          if events == "GERAR":
              try:
                # numero_conta += 1
                criar_conta(AGENCIA, cpf_account)
              except Exception as erro:
                print(erro)
                
          elif events == sg.WINDOW_CLOSED:
            new_user_window()
            window.close()
            break

          
      # Eventos para retornar a interface de inicialização
      elif events == sg.WINDOW_CLOSED or "VOLTAR":
        initial_window()
        window.close()
        break
