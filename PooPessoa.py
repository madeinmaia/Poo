# -*- coding: utf-8 -*-

class Pessoa:
    def __init__(self, nomeAluno, pesoAluno, idadeAluno, comendo=False, falando=False, dormindo=False):
        self.nome = nomeAluno
        self.peso = pesoAluno
        self.idade = idadeAluno
        self.comendo = comendo
        self.falando = falando
        self.dormindo = dormindo

    def acao(self, novaacao):
        if self.comendo or self.falando or self.dormindo:
            print(f"{self.nome} não pode {novaacao} agora, está ocupado.")
            return False
        return True

    def comer(self, alimento):
        if self.acao("comer"):
            print(f"{self.nome} está comendo {alimento}.")
            self.comendo = True

    def parardecomer(self):
        if self.comendo:
            print(f"{self.nome} parou de comer.")
            self.comendo = False
        else:
            print(f"{self.nome} não está comendo.")

    def falar(self):
        if self.acao("falar"):
            print(f"{self.nome} está falando.")
            self.falando = True

    def parardefalar(self):
        if self.falando:
            print(f"{self.nome} parou de falar.")
            self.falando = False
        else:
            print(f"{self.nome} não está falando.")

    def dormir(self):
        if self.acao("dormir"):
            print(f"{self.nome} está dormindo.")
            self.dormindo = True

    def parardedormir(self):
        if self.dormindo:
            print(f"{self.nome} acordou.")
            self.dormindo = False
        else:
            print(f"{self.nome} não está dormindo.")

    def menu(self):
        op = 1
        while op != 0:
            print('\n1 - Comer\n2 - Parar de Comer\n3 - Falar\n4 - Parar de Falar\n5 - Dormir\n6 - Parar de Dormir\n0 - Sair')
            op = int(input('Escolha uma das opções acima.\n> '))
            if op == 1:
                comida = str(input('O que você gostaria de comer?\n> '))
                self.comer(comida)
            elif op == 2:
                self.parardecomer()
            elif op == 3:
                self.falar()
            elif op == 4:
                self.parardefalar()
            elif op == 5:
                self.dormir()
            elif op == 6:
                self.parardedormir()
            elif op == 0:
                print('Obrigado e até a próxima!')
            elif op > 6:
                print('Valor não reconhecido.')
            else:
                print('Não reconheço. Digite novamente.')

pessoa1 = Pessoa("Pythaon", 70, 25)
print('Seu nome é {}, você tem {} anos e seu peso é de {}kg'.format(pessoa1.nome, pessoa1.idade, pessoa1.peso))


pessoa1.menu()