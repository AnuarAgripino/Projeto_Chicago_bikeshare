# coding: utf-8

"""
    Fontes dos sites utilizados para o desenvolvimento desse projeto:
    http://excript.com/curso-de-python.html
    https://docs.python.org/3/library/
    https://matplotlib.org/gallery/index.html
    Foi utilizado também como base os exemplos dados em aula.

    Função format f"string: {}" - versão para python > 3.6
    https://www.python.org/dev/peps/pep-0498/
"""

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")


# Vamos verificar quantas linhas nós temos
print(f"Número de linhas: {len(data_list)}")

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print(f"Linha 0: {data_list[0]}")
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print(f"Linha 1: {data_list[1]}")

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
"""
Outra forma de imprimir as 20 primeiras linhas através do loop while 
i = 0
while i <= 20:
    print("Line", i, data_list[i])
    i += 1
"""
for i, line_enume in enumerate(data_list[:21]):
    print(f"Line {i}: {line_enume}")

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for i, line_enume in enumerate(data_list[:20]):
    print(f"Line {i}: {line_enume[-2]}")

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

"""
    Função para adicionar as colunas de caracteristicas de uma lista em outra lista, seguindo a mesma ordem.
    Argumentos:
        data: dados da coluna
        index: indice da coluna
    Retorna:
        Uma lista com as colunas da outra lista.

"""


def column_to_list(data, index):
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for line_list in data:
        column_list.append(line_list[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)
            ) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)
           ) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(
    data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
gender_list = column_to_list(data_list, -2)

for gender in gender_list:
    if gender == 'Male':
        male += 1
    elif gender == 'Female':
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

"""
    Função de contagem dos gêneros.
    Argumentos:
        male: variável que armazena a quantidade de gênero masculino.
        female: variável que armazena a quantidade de gênero feminino.
    Retorna:
        retorna uma lista com a quantidade total de gênero masculino e feminino, através do if e elif em que analisa se o valor contido na
        lista é 'Male' ou 'Female' e assim adiciona +1 as suas respectivas variáveis.

"""


def count_gender(data_list):
    male = 0
    female = 0
    for gender in gender_list:
        if gender == 'Male':
            male += 1
        elif gender == 'Female':
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)
            ) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)
           ) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[
    1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.

"""
    Função de amostragem do genero mais popular.
    Argumentos:
        genders_pop: recebe o count_gender(data_list) com os valores [935854, 298784], valores que serão comparados no if através do index. 
        answer: variável que armazena a string do gênero.
    Retorna:
        gênero mais predominante na lista.

"""


def most_popular_gender(data_list):
    answer = ""
    genders_pop = count_gender(data_list)
    if genders_pop[0] > genders_pop[1]:
        answer = "Male"
    elif genders_pop[0] < genders_pop[1]:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)
            ) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(
    data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

"""
    Função para construção de gráfico do tipo de usuários.
    Argumentos:
        customer: apenas cliente.
        subscriber: usuários subscritos.
        dependent: usuários que são dependentes.
    Retorna:
        Uma lista com os valores totais de customer, subscriber, dependent. Em seguida é feito um gráfico com os valores.

"""


def count_user_type(data_list):
    customer = 0
    subscriber = 0
    dependent = 0
    for line in data_list:
        if line[-3] == 'Customer':
            customer += 1
        elif line[-3] == 'Subscriber':
            subscriber += 1
        elif line[-3] == 'Dependent':
            dependent += 1
    return [customer, subscriber, dependent]


user_type_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber", "Dependent"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Usuários')
plt.xticks(y_pos, types)
plt.title('Quantidade por tipo de usuário:')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Resposta é falsa, pois alguns usuários não declararam seu gênero, onde se localiza os campos vazios, logo, a soma sera apenas entre aqueles que declararam."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
"""
    Para o cálculo dos valores de min e max, foi utilizado o loop for, if e elif para analizar o maior e o menor numero através da comparação
    de duas variáveis uma com o valor atual e outra com o valor anterior/posterior a atual, dessa forma ela chega até o menor e maior valor.

    Para o cálculo da mediana me basiei na seguinte resposta do Stackoverflow: 
    https://stackoverflow.com/questions/24101524/finding-median-of-list-in-python

    Outras fontes que usei para auxiliar no desenvolvimento/analise das funções para obter min e max:
    https://classroom.udacity.com/nanodegrees/nd109/parts/4a35eebf-3732-4fd0-93b5-8261ea3b32ff/modules/f06769ff-84ff-4b78-b571-f49c7b158189/lessons/e91dc8c3-aed0-4c0c-9a43-438c36df7b0f/concepts/41c9267a-c9bd-42c8-9897-78e49b376471
    https://github.com/moreirab/chicago-bikeshare/blob/master/chicago_bikeshare_pt.py

"""
trip_duration_list = [float(num) for num in column_to_list(data_list, 2)]
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
len_list_trip = len(trip_duration_list)
sum_trip = 0

sorted_list = sorted(trip_duration_list)
# Min trip:
min_trip = sorted_list[0]
# Max trip:
max_trip = sorted_list[-1]

# Mean trip
for i_count in trip_duration_list:
    sum_trip += i_count

mean_trip = sum_trip / len_list_trip

# Median trip:
list_len = len(sorted_list)
index_lst = (list_len - 1) // 2
if list_len % 2:
    median_trip = sorted_list[index_lst]
else:
    median_trip = (sorted_list[index_lst] + sorted_list[index_lst + 1]) / 2

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip,
      "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(
    start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
    Função de exemplo com anotações.
    Argumentos:
        param1: O primeiro parâmetro.
        param2: O segundo parâmetro.
    Retorna:
        Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

"""
    Função para contar os tipos de usuários, porém sem definir os tipos.
    Argumentos:
        item_types: tipos de item, uso do da função set() para eliminar as repetiçõs e criar um conjunto com elementos não repetitivos.
        count_items: contagem de item, usando a função .count() para saber a quantidade de vezes que um
        item se repete por meio do loop for.
    Retorna:
        tipos de genêros incluindo os valores nulos dentro das listas e a quantidade de cada um.

"""


def count_items(column_list):
    item_types = set(column_list)
    count_items = []

    for items in item_types:
        count_items.append(column_list.count(items))

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------

input("\nGostaria de ver o gráfico que fiz da questão 12? Aperte ENTER")
print("\nGráfico com os gêneros masculino, feminino e nulo")


def count_type_user(data_list):
    gender_nulo = 0
    gender_m = 0
    gender_f = 0
    for gender in gender_list:
        if gender == '':
            gender_nulo += 1
        elif gender == 'Male':
            gender_m += 1
        elif gender == 'Female':
            gender_f += 1
    return [gender_nulo, gender_m, gender_f]


gender_list = column_to_list(data_list, -2)
types = ["nulo", "Male", "Female"]
quantity = count_type_user(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade:')
plt.xlabel('Gênero:')
plt.xticks(y_pos, types)
plt.title('Usuários do gênero masculino, feminino e nulos')
plt.show(block=True)
