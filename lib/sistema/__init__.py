from lib.interface import Interface

class Calculadora:
    def __init__(self):
        self.leitura = 30

    def calcular_agua_saiu(self):
        Interface.cabecalho('MENU ÁGUA')
        valor_agua = Interface.leia_float('Valor total da conta: R$')
        quantidade_total_pessoas = Interface.leia_int('Quantidade total de pessoas no lote: ')
        pescasa1 = Interface.leia_int('Quantidade de pessoas da Casa 1: ')
        pescasa2 = Interface.leia_int('Quantidade de pessoas da Casa 2: ')
        pescasa3 = Interface.leia_int('Quantidade de pessoas da Casa 3: ')
        leitura_casa1 = Interface.leia_int('Quantidade de dias que ficaram na Casa 1: ')
        leitura_casa2 = Interface.leia_int('Quantidade de dias que ficaram na Casa 2: ')
        leitura_casa3 = Interface.leia_int('Quantidade de dias que ficaram na Casa 3: ')

        valor_ppessoa = valor_agua / quantidade_total_pessoas
        valor_pdia = valor_ppessoa / self.leitura
        casa1 = pescasa1 * valor_pdia * leitura_casa1
        casa2 = pescasa2 * valor_pdia * leitura_casa2
        casa3 = pescasa3 * valor_pdia * leitura_casa3

        valor_inquilinos = casa1 + casa2 + casa3
        valor_sobrou = (valor_agua - valor_inquilinos) / 2

        if leitura_casa1 == 30:
            casa1 += valor_sobrou
        if leitura_casa2 == 30:
            casa2 += valor_sobrou
        if leitura_casa3 == 30:
            casa3 += valor_sobrou

        Interface.cabecalho('VALOR A SER PAGO')
        print(f'Casa 1: R${casa1:.2f}')
        print(f'Casa 2: R${casa2:.2f}')
        print(f'Casa 3: R${casa3:.2f}')

    def calcular_agua(self):
        Interface.cabecalho('MENU ÁGUA')
        valor_agua = Interface.leia_float('Valor total da conta: R$')
        quantidade_total_pessoas = Interface.leia_int('Quantidade total de pessoas no lote: ')
        pescasa1 = Interface.leia_int('Quantidade de pessoas da Casa 1: ')
        pescasa2 = Interface.leia_int('Quantidade de pessoas da Casa 2: ')
        pescasa3 = Interface.leia_int('Quantidade de pessoas da Casa 3: ')

        valor_ppessoa = valor_agua / quantidade_total_pessoas
        valor_pdia = valor_ppessoa / self.leitura
        casa1 = pescasa1 * valor_pdia * self.leitura
        casa2 = pescasa2 * valor_pdia * self.leitura
        casa3 = pescasa3 * valor_pdia * self.leitura

        Interface.cabecalho('VALOR A SER PAGO')
        print(f'Casa 1: R${casa1:.2f}')
        print(f'Casa 2: R${casa2:.2f}')
        print(f'Casa 3: R${casa3:.2f}')

    def calcular_luz_saiu(self):
        Interface.cabecalho('MENU LUZ')
        valor_total = Interface.leia_float('Valor total da luz: R$')
        quantidade_dias = Interface.leia_int('Quantidade de dias que ficou na casa: ')
        valor_pdia = valor_total / self.leitura
        valor_inquilino = valor_pdia * quantidade_dias
        proprietario = valor_total - valor_inquilino

        Interface.cabecalho('VALOR A SER PAGO')
        print(f'Valor Inquilino: R${valor_inquilino:.2f}')
        print(f'Proprietário: R${proprietario:.2f}')
