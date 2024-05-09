import duckdb as db
import pandas as pd

# Leia a aba "Ativos e Desligados"
df_ativos_desligados = pd.read_excel('Relação de funcionários.xlsx', sheet_name='Ativos e Desligados')

# Leia a aba "b adessao"
df_b_adesao = pd.read_excel('Relação de funcionários.xlsx', sheet_name='b adessao')

# Renomeie colunas na df_ativos_desligados (opcional)
df_ativos_desligados.rename(columns={'Nome completo': 'nome_funcionario'}, inplace=True)

# Renomeie colunas na df_b_adesao (opcional)
df_b_adesao.rename(columns={'NOME': 'nome_funcionario'}, inplace=True)

# Crie a conexão DuckDB
con = db.connect()

# Carregue o DataFrame 'ativos_desligados' para a tabela 'ativos_desligados' no DuckDB
con.from_df(df_ativos_desligados, 'ativos_desligados')
#Load the DataFrame 'ativos_desligados' into the table 'ativos_desligados' in DuckDB
#con.from_df(df_ativos_desligados, name='ativos_desligados')
# Carregue o DataFrame 'ativos_desligados' para a tabela 'ativos_desligados' no DuckDB
#con.from_df(df_ativos_desligados, table='ativos_desligados')

# Carregue o DataFrame 'b_adesao' para a tabela 'bcard_adesao' no DuckDB
con.from_df(df_b_adesao, 'b_adesao')

# Realize o join entre as tabelas, ignorando maiúsculas e minúsculas no 'nome_funcionario'
query = """
SELECT *
FROM ativos_desligados a
JOIN b_adesao b
ON LOWER(a.nome_funcionario) = LOWER(b.nome_funcionario)
"""

# Execute a consulta e armazene o resultado em um DataFrame
df_join = pd.DataFrame(con.execute(query))

