 Automação de Cadastro de Produtos 🖥️🤖

Esse projeto é uma **automação em Python** que cadastra produtos de forma automática a partir de um arquivo CSV usando **PyAutoGUI**.

## 📋 Como funciona
1. O script lê o arquivo `produtos.csv`.
2. Para cada linha da tabela, ele preenche os campos de cadastro na tela automaticamente.
3. Utiliza o PyAutoGUI para clicar, digitar e navegar entre os campos.

## 📂 Estrutura do projeto
├── cadastrar produto.py # Script principal da automação
├── loc.py # Serve para pegar a posição do mouse
├── produtos.csv # Base de dados 
├── requirements.txt # Dependências do projeto
└── .gitignore # Arquivo de ignore do Git
