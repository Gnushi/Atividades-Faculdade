# 🧮 Calculadora de Desconto em Python

## 📌 Sobre o projeto

Esta atividade foi desenvolvida durante meus estudos iniciais de Python no curso de Análise e Desenvolvimento de Sistemas.

O programa recebe o valor de um produto e o percentual de desconto informado pelo usuário. Em seguida, realiza o cálculo do desconto, apresenta o valor final do produto e verifica se o cliente atende aos critérios para receber um cupom de desconto.

---

## 🎯 Objetivo

O objetivo desta atividade foi praticar conceitos básicos de programação em Python, principalmente:

- Entrada de dados
- Saída de dados
- Variáveis
- Conversão de tipos
- Operações matemáticas
- Cálculo de porcentagem
- Estruturas condicionais
- Operadores lógicos
- Arredondamento de valores
- Formatação de textos

---

## 🧠 Conceitos utilizados

### `input()`

Utilizei a função `input()` para receber informações digitadas pelo usuário.

```python
valor_produto = float(input("Digite o valor do produto: "))
valor_desconto = float(input("Digite o valor do desconto: "))

#float()

Utilizei float() para converter os valores recebidos pelo input() para números decimais.
Isso permite trabalhar com valores como:

499.90
510.50
15.5

#Variáveis

Utilizei variáveis para armazenar os valores e resultados utilizados pelo programa.

valor_produto
valor_desconto
valor_do_produto
valor_final

#Cálculo de porcentagem

Para calcular o valor do desconto, utilizei:
valor_produto * valor_desconto / 100
Depois, o valor do desconto é subtraído do preço original:

valor_do_produto = valor_produto - (valor_produto * valor_desconto / 100)

#round()

Utilizei a função round() para arredondar o resultado do cálculo.
valor_final = round(valor_do_produto, 2)

O número 2 indica que quero manter duas casas decimais.

#print()

Utilizei a função print() para apresentar informações e resultados na tela.
print(f"O valor final do produto com desconto é: R$ {valor_final:.2f}")

Nesse caso, o programa apresenta ao usuário o valor final da compra.

#f-string

Utilizei uma f-string para inserir o conteúdo de uma variável diretamente dentro de um texto.
print(f"O valor final do produto com desconto é: R$ {valor_final:.2f}")

O f antes das aspas indica que aquela string permite utilizar variáveis dentro de {}.

#if

Utilizei o if para criar uma condição no programa.
if valor_produto >= 500 and valor_desconto >= 15:

O programa verifica se as condições estabelecidas são verdadeiras.
Nesse caso, ele verifica se:

*O produto custa R$500 ou mais.
*O desconto informado é de 15% ou mais.

Se as condições forem verdadeiras, o programa informa que o cliente recebeu o cupom.

#else

Utilizei o else para definir o que acontece quando a condição do if não é atendida.

else:
    print("Você não ganhou o cupom de desconto.")

Dessa forma, o programa possui dois caminhos possíveis:
Condição verdadeira → executa o if
Condição falsa → executa o else

#Operador and

Utilizei o operador lógico and para exigir que duas condições sejam verdadeiras ao mesmo tempo.

if valor_produto >= 500 and valor_desconto >= 15:
Nesse caso, as duas condições precisam ser verdadeiras:
valor_produto >= 500
        E
valor_desconto >= 15
Se apenas uma delas for verdadeira, o if não será executado.










































