import pandas as pd
from tqdm import tqdm

# Caminho para o arquivo Excel
excel_file_path = r'C:\projetos\rpa\excel\base_escolas_crm.xlsx'

# Ler a planilha específica 'as_crm' para um DataFrame
try:
    df = pd.read_excel(excel_file_path, sheet_name='as_crm')
    print("Planilha 'as_crm' carregada com sucesso.")
except FileNotFoundError:
    print(f"Erro: O arquivo {excel_file_path} não foi encontrado.")
    exit(1)
except Exception as e:
    print(f"Erro ao ler o arquivo Excel: {e}")
    exit(1)

# Especificação dos padrões a serem filtrados
padroes_para_remover = [
    'naoresponda@dsop.com.br', 
    '^naoexiste', 
    '^naotem', 
    '^naores', 
    'dsop.com.br', 
    'naotem.com', 
    'nao@tem', 
    'não@'
]

# Compilação dos padrões em uma única expressão regular
expressao_filtro = '|'.join(padroes_para_remover)

# Inicializando a barra de progresso
tqdm.pandas(desc="Filtrando registros")

# Filtrar registros que não contêm os padrões especificados com progresso
df_filtrado = df[df['email'].progress_apply(lambda x: not pd.isna(x) and not pd.Series(x).str.contains(expressao_filtro, case=False).any())]

# Caminho para o arquivo Excel de saída
output_file_path = r'C:\projetos\rpa\excel\base_escolas_crm_filtrado.xlsx'

# Gerar um novo arquivo Excel com os dados filtrados
try:
    df_filtrado.to_excel(output_file_path, index=False)
    print(f"Arquivo filtrado '{output_file_path}' gerado com sucesso.")
except Exception as e:
    print(f"Erro ao salvar o arquivo Excel: {e}")
    exit(1)
