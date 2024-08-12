from setuptools import setup, find_packages

setup(
    name='excel_data_filter',
    version='0.1.0',
    description='Projeto para filtrar registros de e-mail em planilhas Excel',
    author='Charles',
    author_email='charles.rodrigues@dsop.com.br',
    url='https://github.com/seu_usuario/excel_data_filter',
    packages=find_packages(),  # Procurar pacotes na raiz do projeto
    install_requires=[
        'pandas',    # Biblioteca necessária para manipulação de dados
        'openpyxl',  # Necessário para leitura/escrita de arquivos Excel
        'tqdm'       # Necessário para exibir barras de progresso
    ],
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
