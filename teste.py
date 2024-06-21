# Neste exemplo você verá o seguinte:
#TODO: Importe as bibliotecas.


#TODO: Defina as classes e outros métodos:
class Usuario():
    # Este método aqui fará o sistema inicializar solicitando login e senha
    # Eu não quis passar mais nada nos parâmetros, já que eles serão inseridos durante a execução.
    def __init__(self):
        self.login = input('Informe seu login: ')
        self.senha = input('Informe sua senha: ')

    # Este método aqui eu estou definindo como será a verificação das informações
    def verificar_acesso(self):
        if self.login == 'teste' and self.senha == 'teste':
            print(f'Seja bem vindo: {self.login}!')
        return

# Esse método está definido diretamente no escopo geral da aplicação.
def main():
    while True:
        # aqui estou definindo quem será o usuario
        p1 = Usuario()
        # aqui eu estou chamando o método para ver se batem as informações
        p1.verificar_acesso()

# Aqui você chama o método que iniciará a sua lógica do programa:
main()
