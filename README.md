# Udacity Fundamentos de IA e Machine Learning
Projeto I - Chicago Bikeshare

# Detalhes do projeto:

## Dados sobre compartilhamento de bicicletas
Na última década, os sistemas de compartilhamento de bicicletas têm crescido em número e popularidade nas cidades de todo o mundo. Sistemas de compartilhamento de bicicletas permitem que os usuários aluguem bicicletas por um período curtíssimo, por um preço específico. Isso permite que pessoas retirem uma bicicleta do ponto A e a devolvam no ponto B, embora também possam devolvê-la no mesmo local, caso queiram apenas sair para um passeio. Independentemente disso, cada bicicleta pode servir vários usuários por dia.

Graças à ascensão das tecnologias de informação, é fácil para um usuário acessar uma estação dentro do sistema para desbloquear ou devolver as bicicletas. Essas tecnologias também fornecem uma riqueza de dados que podem ser utilizados para explorar como esses sistemas de compartilhamento de bicicletas são usados.

Neste projeto, você usará os dados fornecidos pelo Motivate, um provedor de sistema de bicicletas compartilhadas para diversas grandes cidades dos Estados Unidos, para descobrir os padrões de uso do compartilhamento de bicicletas. Você analisará o uso do sistema de uma das maiores cidades dos Estados Unidos: Chicago.

### Os conjuntos de dados
Os dados para os primeiros seis meses de 2017 são fornecidos. O arquivo de dados contêm seis (6) colunas principais:

- Horário de início (ex., 2017-01-01 00:07:57)
- Horário de término (ex., 2017-01-01 00:20:53)
- Duração da viagem (em segundos, ex., 776)
- Estação inicial (ex., Broadway & Barry Avenue)
- Estação final (ex., Sedgwick St & do North Ave)
- Tipo de usuário (assinante ou cliente)
- Gênero do usuário
- Ano de nascimento do usuário
- Os arquivos originais - que podem ser acessados aqui: Chicago, Nova Iorque e Washington - tinham mais colunas, e elas diferiam em formato em muitos casos. Alguns processos de data wrangling foram realizados para condensar esses arquivos nas seis colunas principais citadas acima, para simplificar sua análise e a avaliação de suas habilidades de Python. No curso de data wrangling que sucede este curso no programa, os alunos aprendem a manipular os conjuntos de dados mais obscuros e desorganizados, então não se preocupe em perder algo.

### As perguntas
Você vai escrever um código para completar as seguintes tarefas sobre os dados de compartilhamento de bicicletas:

- Tarefa 1: Mostre as 20 primeiras amostras (linhas) da base de dados
- Tarefa 2: Mostre o gênero (coluna) das 20 primeiras amostras
- Tarefa 3: Cria uma função para pegar colunas como lista
- Tarefa 4: Conte quantas pessoas de cada gênero
- Tarefa 5: Crie uma função para contar os gêneros
- Tarefa 6: Mostre o gênero mais popular
- Tarefa 7: Mostre um gráfico usando os dados anteriores
- Tarefa 8: Responda o motivo do número de homens e mulheres não bater com a quantidade de amostras
- Tarefa 9: Encontre o valor mínimo, máximo, média e mediana da duração de viagens
- Tarefa 10: Mostre todas as estações da base de dados
- Tarefa 11: Confira se documentou todas suas funções
- Tarefa 12: Crie uma função que conte a ocorrência de qualquer coluna (opcional)

## Passo a passo do código

### ToDos
Você deve preencher o código chicago_bikeshare_pt.py nos locais com comentários que começam com "ToDo". Leia todo o código e entenda o fluxo do script e quais partes você deve desenvolver.

### ASSERTs
Nós estamos utilizando assert para garantir que seu código está retornando valores esperados ou que a saída do seu código está no formato correto. NÃO ALTERE ELES. Se você não conseguir passar por um assert, peça ajuda no fórum ou busque ajuda na internet.

# Screenshots: resultado do terminal e graficos
## Tarefa 1
![captura de tela 2018-12-29 as 19 57 15](https://user-images.githubusercontent.com/35881112/50542440-86770580-0ba4-11e9-9d0f-0c1beba86382.png)
## Tarefa 2, 3, 4 e 5
![captura de tela 2018-12-29 as 19 57 52](https://user-images.githubusercontent.com/35881112/50542441-8971f600-0ba4-11e9-8b5c-00818d737ee2.png)
## Tarefa 6, 7, 8 e 9
![captura de tela 2018-12-29 as 20 06 19](https://user-images.githubusercontent.com/35881112/50542476-4cf2ca00-0ba5-11e9-9089-1d960d837fa1.png)
### Graficos:
![figure_1](https://user-images.githubusercontent.com/35881112/50542497-bbd02300-0ba5-11e9-9e50-87829e305f8f.png)
![figure_2](https://user-images.githubusercontent.com/35881112/50542498-bbd02300-0ba5-11e9-8691-9ef6149c94d0.png)
## Tarefa 10
![captura de tela 2018-12-29 as 20 11 14](https://user-images.githubusercontent.com/35881112/50542503-fb970a80-0ba5-11e9-9da0-7f4d554c3572.png)
## Tarefa 12
![captura de tela 2018-12-29 as 20 15 12](https://user-images.githubusercontent.com/35881112/50542530-ac050e80-0ba6-11e9-8ba1-a13a1de7b34a.png)
![figure_3](https://user-images.githubusercontent.com/35881112/50542519-50d31c00-0ba6-11e9-9d40-81fbf463a8bb.png)
