from processamento_dados import Dados

#############################
# Caminhos dos dados brutos:
#############################
PATH_JSON = 'data_raw/dados_empresaA.json'
PATH_CSV = 'data_raw/dados_empresaB.csv'

##############
# Extract:
##############
dados_empresaA = Dados.load_data(PATH_JSON, "json")
print("nomes 01:", dados_empresaA.name_columns)

dados_empresaB = Dados.load_data(PATH_CSV, "CSV")
print("\nnomes 02:", dados_empresaB.name_columns)

##############
# Transform:
##############
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_empresaB.rename_columns(key_mapping)
print("\nNovos Nomes:", dados_empresaB.name_columns)
print("\nEmpresaA Nª Linhas:", dados_empresaA.len_rows)
print("\nEmpresaB Nª Linhas:", dados_empresaB.len_rows)

dados_fusao = Dados.merge(dados_empresaA, dados_empresaB)
print("\ndados_fusao_inicio:", dados_fusao.dados[0])
print("\ndados_fusao_fim:", dados_fusao.dados[-1])
print("\nFusão Nª Linhas:", dados_fusao.len_rows)


##############
# Load:
##############
PATH_DATA_PROCESSED = "data_processed/dados_combinados.csv"
dados_fusao.save_csv(PATH_DATA_PROCESSED)
print(PATH_DATA_PROCESSED)
