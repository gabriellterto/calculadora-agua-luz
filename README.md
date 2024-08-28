# Sistema de Cálculo de Contas

Este projeto é um sistema de cálculo de contas de água e luz, projetado para ser usado em ambientes residenciais. O sistema permite calcular os valores a serem pagos por diferentes casas com base na quantidade de pessoas e dias de uso.

## Estrutura do Projeto

- **lib/**: Contém os módulos de código que gerenciam a lógica do sistema e a interação com o usuário.
  - `interface.py`: Define a classe `Interface` para gerenciar a interação com o usuário.
  - `sistema.py`: Define a classe `Calculadora` para realizar cálculos das contas.
- **aplicativo/**: Contém o arquivo principal que executa o aplicativo.
  - `app.py`: O ponto de entrada do programa que coordena a execução.
- **tela.py**: Gerencia o menu principal e as interações com o usuário, usando os módulos da pasta `lib`.

## Funcionalidades

1. **Cálculo de Conta de Água**:
   - Calcula o valor a ser pago pelas casas considerando a quantidade de pessoas e dias de uso.
   - Ajusta o valor se a casa estiver ocupada por 30 dias.

2. **Cálculo de Conta de Luz**:
   - Calcula o valor da conta de luz considerando os dias de uso do inquilino e o valor restante para o proprietário.

3. **Menu Interativo**:
   - Permite ao usuário escolher entre calcular contas de água ou luz ou sair do programa.
   - Oferece opções adicionais para calcular com base na presença ou ausência dos inquilinos.

## Requisitos

Certifique-se de ter Python 3.x instalado em seu sistema.

