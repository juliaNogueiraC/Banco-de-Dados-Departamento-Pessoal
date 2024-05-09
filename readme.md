# Banco de dados de Departamento Pessoal - Consulta SQL com Python e DuckDB

Este projeto demonstra como realizar consultas SQL em bancos de dados do Departamento Pessoal de uma empresa, utilizando Python e DuckDB. DuckDB é um banco de dados de análise em memória com suporte para consultas SQL e é especialmente útil para processamento de dados em grandes conjuntos de dados.

## Instalação

Para executar este projeto, é necessário ter o DuckDB instalado. Você pode instalá-lo usando o seguinte comando:

```bash
pip install duckdb
```

Além disso, este projeto faz uso da biblioteca pandas para manipulação de dados. Se você ainda não tiver o pandas instalado, pode instalá-lo com o seguinte comando:

```bash
pip install pandas
```

## Como usar

1. Baixe a planilha "sua_planilha_aqui.xlsx" e certifique-se de que está no mesmo diretório do seu código Python. Obs.: Por se tratar de dados sensiveis da organização, foi decidido manter secretos os dados origianis. Utilize uma planilha sua para realizar os testes. 

2. Abra o arquivo Python e execute o código fornecido.

3. O código irá ler as abas "Ativos e Desligados" e "b adessao" do arquivo Excel(neste caso, essas abas são o exemplo do meu banco de dados, mas você pode substituir pelos nomes das abas da sua planilha) e carregá-las como DataFrames pandas.

4. Em seguida, o código estabelece uma conexão com o DuckDB e carrega os DataFrames como tabelas no banco de dados.

5. Uma consulta SQL é realizada para fazer um join entre as tabelas, ignorando maiúsculas e minúsculas no campo "nome_funcionario".

6. O resultado da consulta é armazenado em um DataFrame pandas chamado "df_join".

7. Você pode manipular e analisar o resultado conforme necessário utilizando a biblioteca pandas.

## Contribuição

Contribuições são bem-vindas! Se você encontrar um problema, tiver uma sugestão ou quiser adicionar uma nova funcionalidade, sinta-se à vontade para abrir uma issue ou enviar um pull request.
