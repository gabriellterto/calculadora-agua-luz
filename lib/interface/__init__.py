class Interface:
    @staticmethod
    def leia_int(msg):
        while True:
            try:
                n = int(input(msg))
            except (ValueError, TypeError):
                print('ERRO! Por favor, digite um número inteiro válido.')
                continue
            except KeyboardInterrupt:
                print('Usuário preferiu não digitar esse número.')
                return 0
            else:
                return n

    @staticmethod
    def leia_float(msg):
        while True:
            try:
                n = float(input(msg))
            except (ValueError, TypeError):
                print('ERRO! Por favor, digite um número válido.')
                continue
            except KeyboardInterrupt:
                print('Usuário preferiu não digitar esse número.')
                return 0
            else:
                return n

    @staticmethod
    def linhas(tam=40):
        return '-' * tam

    @staticmethod
    def cabecalho(txt):
        print(Interface.linhas())
        print(f'{txt:^40}')
        print(Interface.linhas())

    @staticmethod
    def menu(lista):
        for i, item in enumerate(lista, 1):
            print(f'{i} - {item}')
        print(Interface.linhas())
        escolha = Interface.leia_int('Sua escolha: ')
        return escolha
