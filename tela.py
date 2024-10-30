import os
from lib.interface import Interface
from lib.sistema import Calculadora

class App:
    def __init__(self):
        self.calculadora = Calculadora()

    def run(self):
        while True:
            Interface.cabecalho('MENU PRINCIPAL')
            escolha = Interface.menu(['Conta de água', 'Conta de luz', 'Sair do Programa'])
            if os.name == "nt":
                os.system('cls')
            else:
                os.system('clear')

            if escolha == 1:
                if os.name == "nt":
                    os.system('cls')
                else:
                    os.system('clear')
                print('-' * 40)
                num_casas = Interface.leia_int('Digite o número de casas: ')
                print('-' * 40)
                agua_escolha = Interface.menu(['Caso a pessoa tenha saído', 'Caso a pessoa não tenha saído', 'Voltar ao menu principal'])
                if agua_escolha == 1:
                    self.calculadora.calcular_agua_saiu(num_casas)
                elif agua_escolha == 2:
                    self.calculadora.calcular_agua(num_casas)
                elif agua_escolha == 3:
                    continue
                else:
                    print('ERRO! Digite uma opção válida!')
            elif escolha == 2:
                num_casas = Interface.leia_int('Digite o número de casas: ')
                luz_escolha = Interface.menu(['Cálculo por Cabeça', 'Voltar ao menu principal'])
                if luz_escolha == 1:
                    self.calculadora.calcular_luz_por_cabeca(num_casas)
                elif luz_escolha == 2:
                    continue
                else:
                    print('ERRO! Digite uma opção válida!')
            elif escolha == 3:
                Interface.cabecalho('Saindo do Programa')
                print('Volte Sempre!')
                break
            else:
                print('ERRO! Digite uma opção válida!')

if __name__ == "__main__":
    app = App()
    app.run()
