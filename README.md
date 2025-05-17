Obs.: caso o app esteja no modo "sleeping" (dormindo) ao entrar, basta clicar no botão que estará disponível e aguardar, para ativar o mesmo.
![print fipe app](https://github.com/user-attachments/assets/4f2633a6-20c0-421f-bdc3-d3e558a3f56b)

## FIPE App | Preços de Veículos

**Descrição**

Este aplicativo Streamlit permite consultar preços de veículos (carros, motos, caminhões) na Tabela FIPE. O usuário seleciona o tipo, marca, modelo e ano, exibe detalhes e faz download de um PDF com os resultados.

## Funcionalidades
•	Seleção de tipo de veículo: carros, motos e caminhões.
•	Consulta de marcas, modelos e anos via API FIPE (Parallelum).
•	Exibição de detalhes: marca, modelo, ano, preço, código FIPE e combustível.
•	Geração de PDF com os resultados da consulta.
•	Download do PDF diretamente na aplicação.
•	Layout personalizado com logo.

## Tecnologias
•	Python
•	Streamlit
•	Requests
•	FPDF

## Instalação
1. Clone este repositório:
   ```bash
   git clone <URL do repositório>
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd fipe-app
   ```
3. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```

## Uso
Execute o aplicativo com:
```bash
streamlit run app.py
```
Em seguida, abra seu navegador em http://localhost:8501 para acessar o FIPE App.

## Arquivos
•	`app.py`: Código-fonte principal do Streamlit.
•	`requirements.txt`: Lista de dependências do projeto.
•	`README.md`: Este arquivo de documentação.

## Contato
Por Ary Ribeiro  
Email: aryribeiro@gmail.com

## Licença
Distribuído sob a licença MIT.