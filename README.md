# Trabalho Prático de Introdução a Ciência dos Dados

O objetivo do trabalho é analisar como os usuários do twitter encaram o chatGPT, de modo que também seja analisado esse fato ao longo do tempo e conforme localização geográfica.

### Para instalar as dependências:
```
python3 installPackages.py
```

### Instruções para desenvolvimento
 
Primeiramente, é interessante a criação de um ambiente virtual para tal.

Utilizando o anaconda, é possível criar um ambiente de desenvolvimento utilizando o comando:

```conda create --name tpICD python=3.10.11```

Para ativá-lo em sistemas baseados em unix digite:

```conda activate tpICD```

Além disso, é importante que o desenvolvimento siga essas regras:

- Sempre ao instalar novas bibliotecas inserir as dependências novas no arquivo `requirements.txt`
- Sempre atualizar o decorrer das tarefas na aba projects

### Análise Exploratória dos Dados

Nessa segunda etapa do trabalho sobre o tema: **Como estão as reações sobre o ChatGPT no twitter?**

Buscamos realizar a Análise exploratória dos dados para entender melhor o principal database selecionado, além de iniciar os preparativos para algumas funções que serão úteis para o desenvolvimento do trabalho.

Primeiramente, aumentamos a base de dados utilizando algumas fontes complementares, referenciadas a seguir: 

https://www.kaggle.com/datasets/edomingo/chatgpt-1000-daily-tweets

https://www.kaggle.com/datasets/khalidryder777/500k-chatgpt-tweets-jan-mar-2023

https://www.kaggle.com/datasets/manishabhatt22/tweets-onchatgpt-chatgpt

https://www.kaggle.com/datasets/tariqsays/chatgpt-twitter-dataset

Tal decisão foi motivada visto que a database selecionada primeiramente continha relativamente poucos dados, então buscamos novas fontes razoavelmente semelhantes a original (contendo atributos importantes, como número de retweets, conteúdo do tweet, quantidade de likes ...).

Dessa forma, algumas ações sobre os dados foram feitas (a partir do database mais completo - chatgpt-1000-daily-tweets, tais análises estão no notebook <analiseInicial.ipynb>). Assim, foi feito uma filtragem inicial, retirando algumas colunas com informações que não são relevantes (como user_id, user_created...) além de uma filtragem nos tweets (usamos apenas tweets com mais de 0 curtidas). Após isso, outras análises são feitas, tendo em vista a língua e quantidade de curtidas juntamente de outros aspectos do trabalho como análise de sentimento e traduções, que podem ser acompanhadas melhor seguindo o notebook.

Além disso, outro arquivos também foram desenvolvidos nessa etapa, como o teste e utilização de algumas bibliotecas e funcionalidades que serão úteis futuramente. Como exemplo, foram feitos notebooks voltados para a utilizacao da biblioteca "vader" que faz a Análise de sentimento dos conteúdos dos tweets. Além disso, tal funcionalidade foi feita testando diferentes conteúdos, como textos em português, inglês e outras línguas. Tal fato é importante pois além de nos familiarizarmos com a Análise de sentimento, também iniciamos o processo de tradução com a utilização da biblioteca do Google tradutor para fazer esse trabalho. Todas essas ações estão representadas nos notebooks presentes nesse trabalho.
