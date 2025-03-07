# 1. Type Hint
# O uso de Type Hint ajuda a tornar o código mais legível e seguro, especificando o tipo de dados esperados por funções e variáveis. Na engenharia de dados, isso é especialmente útil para garantir que as funções de manipulação e análise de dados recebam os dados no formato correto, reduzindo erros em tempo de execução.

# Para demonstrar como utilizar Type Hints com tipos primitivos em Python, vamos criar quatro variáveis representando os tipos mais comuns: int para números inteiros, float para números de ponto flutuante, str para strings (cadeias de caracteres) e bool para valores booleanos. Type Hints são usados para indicar o tipo de uma variável no momento da sua declaração, melhorando a legibilidade do código e facilitando a detecção de erros.

# Sem Type Hint

idade = 30
altura = 1.75
nome = "Alice"
is_estudante = True
# Com Type Hint

idade: int = 30
altura: float = 1.75
nome: str = "Alice"
estudante: bool = True
# O uso de Type Hint ajuda a tornar o código mais legível e seguro, especificando o tipo de dados esperados por funções e variáveis. Na engenharia de dados, isso é especialmente útil para garantir que as funções de manipulação e análise de dados recebam os dados no formato correto, reduzindo erros em tempo de execução.

# Na Python, a tipagem de funções é facilitada pelo uso de "Type Hints" (Dicas de Tipo), uma característica introduzida no Python 3.5 através do PEP 484. Os Type Hints permitem aos desenvolvedores especificar os tipos de dados esperados para os parâmetros de uma função e o tipo de dado que a função deve retornar. Embora essas dicas de tipo não sejam estritamente aplicadas em tempo de execução, elas são extremamente úteis para ferramentas de análise estática de código, melhorando a legibilidade do código e ajudando na detecção precoce de erros.

# Tipagem Fraca vs. Forte
# Tipagem Forte: Em linguagens com tipagem forte, uma vez que uma variável é atribuída a um tipo, não pode ser automaticamente tratada como outro tipo sem uma conversão explícita. Python é um exemplo de linguagem com tipagem forte. Isso significa que operações que misturam tipos incompatíveis (como adicionar um número a uma string) resultarão em erro.

# Tipagem Fraca: Linguagens com tipagem fraca permitem maior flexibilidade nas operações entre diferentes tipos, fazendo conversões de tipo implícitas. JavaScript é um exemplo clássico, onde você pode adicionar números a strings sem erros, resultando em uma concatenação de texto.

# Tipagem Estática vs. Dinâmica
# Tipagem Estática: Linguagens de tipagem estática, como Java e C++, exigem que o tipo de cada variável seja declarado explicitamente no momento da compilação. Isso ajuda a detectar erros de tipo antes da execução do programa, aumentando a segurança do tipo e potencialmente melhorando o desempenho.

# Tipagem Dinâmica: Python é um exemplo de linguagem com tipagem dinâmica, onde os tipos são inferidos em tempo de execução e não precisam ser declarados explicitamente. Isso oferece flexibilidade e rapidez no desenvolvimento, mas pode aumentar o risco de erros de tipo que só serão detectados em tempo de execução.

# Exercício será tipar o desafio da aula 03

nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

while not nome_valido:
    try:
        nome = input("Digite seu nome: ")

        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float

try:
    salario: float = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
try:
    bonus: float = float(input("Digite o valor do bônus recebido: "))
    if bonus < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

bonus_recebido: float = 1000 + salario * bonus  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")
# 2. Listas e Dicionários
# Importância na Engenharia de Dados
# Listas e dicionários são estruturas de dados versáteis que permitem armazenar e manipular coleções de dados de forma eficiente. Na engenharia de dados, essas estruturas são fundamentais para organizar dados coletados de diversas fontes, facilitando operações como filtragem, busca, agregação e transformação de dados.

# Exercícios de Listas e Dicionários
# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
# Exercícios de Listas e Dicionários resolvidos
# Resoluções de Listas e Dicionários

# 1. Lista de números ao quadrado
numeros: list = list(range(1, 11))

for numero in numeros:
    print(numero**2)

# 2. Modificar lista de linguagens
linguagens = ["Python", "Java", "C++", "JavaScript"]
linguagens.remove("C++")
linguagens.append("Ruby")
print(linguagens)

# 3. Informações de um livro
livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
for chave, valor in livro.items():
    print(f"{chave}: {valor}")

# 4. Contar ocorrências de caracteres
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))

# 5. Preço total da lista de compras
lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[item] for item in lista_compras)
print(f"Preço total: {total}")

# Exercícios intermediários e mais avançados

# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))

print(emails_unicos)

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades = [22, 15, 30, 17, 18]
idades_validas = [idade for idade in idades if idade >= 18]

print(idades_validas)

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.

numeros = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)

print("Média:", media)

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]

print("Pares:", pares)
print("Ímpares:", impares)

# Exercícios com Dicionários

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar o preço do produto com id 2 para 90
for produto in produtos:
    if produto["id"] == 2:
        produto["preço"] = 90

print(produtos)

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido)

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.


dicionario = {"a": 1, "b": 2, "c": 3}
chaves = list(dicionario.keys())
valores = list(dicionario.values())

print("Chaves:", chaves)
print("Valores:", valores)

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)