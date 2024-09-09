class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    def gritar(self):
        print("olaaaaa, tá aíiii? ")
    def dizer_ola(self):
        print(f'OLÁAAAAA PESSOAL, TUDO BEM? ')

luciano = Pessoa("Luciano")
luciano.gritar()
luciano.dizer_ola()
