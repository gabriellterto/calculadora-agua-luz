from lib.interface import Interface

class Calculadora:
    def __init__(self):
        self.leitura = 30

    def calcular_agua_saiu(self, num_casas):
        Interface.cabecalho('MENU ÁGUA')
        valor_agua = Interface.leia_float('Valor total da conta: R$')
        
        pessoas_por_casa = []
        leitura_por_casa = []
        valores_por_casa = []

        # Lê a quantidade de pessoas de cada casa
        for i in range(1, num_casas + 1):
            pescasa = Interface.leia_int(f'Quantidade de pessoas da Casa {i}: ')
            pessoas_por_casa.append(pescasa)

        # Lê a quantidade de dias que cada casa ficou
        for i in range(1, num_casas + 1):
            leitura_casa = Interface.leia_int(f'Quantidade de dias que ficaram na Casa {i}: ')
            leitura_por_casa.append(leitura_casa)

        # Calcula a quantidade total de pessoas
        quantidade_total_pessoas = sum(pessoas_por_casa)

        valor_ppessoa = valor_agua / quantidade_total_pessoas
        valor_pdia = valor_ppessoa / self.leitura
        valor_inquilinos = 0

        for i in range(num_casas):
            valor_casa = pessoas_por_casa[i] * valor_pdia * leitura_por_casa[i]
            valores_por_casa.append(valor_casa)
            valor_inquilinos += valor_casa

        valor_sobrou = valor_agua - valor_inquilinos

        for i in range(num_casas):
            if leitura_por_casa[i] < 30:
                valores_por_casa[i] += (valor_sobrou / sum(leitura_por_casa) * leitura_por_casa[i])

        Interface.cabecalho('VALOR A SER PAGO')
        for i in range(num_casas):
            print(f'Casa {i + 1}: R${valores_por_casa[i]:.2f}')

    def calcular_agua(self, num_casas):
        Interface.cabecalho('MENU ÁGUA')
        valor_agua = Interface.leia_float('Valor total da conta: R$')
        
        pessoas_por_casa = []
        valores_por_casa = []

        # Lê a quantidade de pessoas de cada casa
        for i in range(1, num_casas + 1):
            pescasa = Interface.leia_int(f'Quantidade de pessoas da Casa {i}: ')
            pessoas_por_casa.append(pescasa)

        # Calcula a quantidade total de pessoas
        quantidade_total_pessoas = sum(pessoas_por_casa)

        valor_ppessoa = valor_agua / quantidade_total_pessoas
        valor_pdia = valor_ppessoa / self.leitura

        for i in range(num_casas):
            valor_casa = pessoas_por_casa[i] * valor_pdia * self.leitura
            valores_por_casa.append(valor_casa)

        Interface.cabecalho('VALOR A SER PAGO')
        for i in range(num_casas):
            print(f'Casa {i + 1}: R${valores_por_casa[i]:.2f}')

    def calcular_luz_por_cabeca(self, num_casas):
        Interface.cabecalho('MENU LUZ')
        valor_total = Interface.leia_float('Valor total da conta de luz: R$')
        
        pessoas_por_casa = []
        valores_por_casa = []

        # Lê a quantidade de pessoas de cada casa
        for i in range(1, num_casas + 1):
            pescasa = Interface.leia_int(f'Quantidade de pessoas da Casa {i}: ')
            pessoas_por_casa.append(pescasa)

        # Calcula a quantidade total de pessoas
        quantidade_total_pessoas = sum(pessoas_por_casa)

        valor_ppessoa = valor_total / quantidade_total_pessoas

        for i in range(num_casas):
            valor_casa = pessoas_por_casa[i] * valor_ppessoa
            valores_por_casa.append(valor_casa)

        Interface.cabecalho('VALOR A SER PAGO')
        for i in range(num_casas):
            print(f'Casa {i + 1}: R${valores_por_casa[i]:.2f}')
