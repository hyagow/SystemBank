# type: ignore
# Importando métodos das funcionalidades da interface gráfica
from interface_grafica import *  # noqa: F403
from metodos import *  # noqa: F403


# Criação do banco de dados e da tabela padrão
create_mydb_and_table_defaults()  # noqa: F405

# Tela de inicialização do programa (Tela de Login)
login_window()  # noqa: F405
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

      # Variáveis para aproveitamento nas funções de transação.
      AGENCIA = "0001"
      LIMITE_SAQUES = 3
      
      saldo = 0
      limite = 500
      extrato = ""
      numero_saques = 0
      contas = []

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
                    Este campo só aceita números.", font= "Arial 13 bold", 
                    auto_close=True, no_titlebar=True, button_type=5, 
                    background_color="#fff", text_color="#333")

        elif events == "SACAR":
          try:
            valor_sacar = float(values['sacar'].replace(',', '.'))
            window['saida'].update('')
            window['sacar'].update('')
            
            saldo, extrato = saque(valor_sacar=valor_sacar, saldo=saldo,  # noqa: F405
                                  limite=limite, extrato=extrato,
                                  numero_saques=numero_saques,
                                  limite_saques=LIMITE_SAQUES)
            
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
                    font= "Arial 13 bold", auto_close=True, no_titlebar=True, 
                    button_type=5, background_color="#fff", text_color="#333")

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
              font= "Arial 13 bold", auto_close=True, no_titlebar=True, 
              button_type=5, background_color="#fff", text_color="#333")

  if events == "Novo Usuário":
    new_user_window()  # noqa: F405
    window.close()

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

        # Limpando os espaços vazios da direita e da esquerda dos 
        # campos de inserção
        nome = values["nome"].strip()
        dia = values["dia"].strip()
        mes = values["mes"].strip()
        ano = values["ano"].strip()
        cpf = values["cpf"].strip()
        endereco = values["endereco"].strip()
        senha = values["senha"].strip()

        # Função para cadastrar novos usuários
        inserir_usuario(nome, dia, mes, ano, cpf, endereco, senha)  # noqa: F405

      # Eventos para retornar a interface anterior
      elif events == sg.WINDOW_CLOSED or "VOLTAR":  # noqa: F405
        login_window()  # noqa: F405
        window.close()
        break
      