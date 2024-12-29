import streamlit as st
import requests
from fpdf import FPDF
import base64

# Configuração inicial do Streamlit
st.set_page_config(page_title="FIPE App | Preços de Veículos", layout="centered", initial_sidebar_state="auto")

# URL do logo
logo_url = "https://i.imgur.com/gLHisDS.png"

# Exibindo o logo pela URL
st.markdown(
    f"""
    <style>
        .centered-logo {{
            display: flex;
            justify-content: center;
        }}
    </style>
    <div class="centered-logo">
        <img src="{logo_url}" width="400">
    </div>
    """,
    unsafe_allow_html=True
)

st.title("FIPE App")
st.markdown(
    """
    Este aplicativo permite consultar o preço de veículos na Tabela FIPE. 
    Basta selecionar a marca, modelo e ano no menu lateral esquerdo, para consultar e baixar seu PDF.
    """
)

# Funções para interação com a API
BASE_URL = "https://parallelum.com.br/fipe/api/v1"

def get_brands(vehicle_type):
    """Obtém a lista de marcas do tipo de veículo."""
    url = f"{BASE_URL}/{vehicle_type}/marcas"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

def get_models(vehicle_type, brand_code):
    """Obtém a lista de modelos de uma marca específica."""
    url = f"{BASE_URL}/{vehicle_type}/marcas/{brand_code}/modelos"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

def get_years(vehicle_type, brand_code, model_code):
    """Obtém os anos disponíveis para um modelo específico."""
    url = f"{BASE_URL}/{vehicle_type}/marcas/{brand_code}/modelos/{model_code}/anos"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

def get_price(vehicle_type, brand_code, model_code, year_code):
    """Obtém o preço de um veículo específico."""
    url = f"{BASE_URL}/{vehicle_type}/marcas/{brand_code}/modelos/{model_code}/anos/{year_code}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else {}

def generate_pdf(data):
    """Gera um PDF com os detalhes do veículo."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Consulta Tabela FIPE", ln=True, align='C')
    pdf.ln(10)
    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
    return pdf.output(dest="S").encode("latin1")

def download_button(data, filename):
    """Cria um botão para download do PDF."""
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">Clique aqui para baixar o PDF</a>'
    st.markdown(href, unsafe_allow_html=True)

# Interface de seleção de tipo de veículo
vehicle_type = st.sidebar.selectbox("Tipo de veículo", ["carros", "motos", "caminhoes"])

# Seleção de marca
brands = get_brands(vehicle_type)
brand_options = {brand['nome']: brand['codigo'] for brand in brands}
brand_name = st.sidebar.selectbox("Selecione a marca", list(brand_options.keys()))
brand_code = brand_options[brand_name]

# Seleção de modelo
models = get_models(vehicle_type, brand_code)
model_options = {model['nome']: model['codigo'] for model in models.get("modelos", [])}
model_name = st.sidebar.selectbox("Selecione o modelo", list(model_options.keys()))
model_code = model_options[model_name]

# Seleção de ano
years = get_years(vehicle_type, brand_code, model_code)
year_options = {year['nome']: year['codigo'] for year in years}
year_name = st.sidebar.selectbox("Selecione o ano", list(year_options.keys()))
year_code = year_options[year_name]

# Exibição do preço
if st.sidebar.button("Consultar preço"):
    price_data = get_price(vehicle_type, brand_code, model_code, year_code)
    if price_data:
        st.subheader(f"Detalhes do veículo:")
        st.write(f"**Marca:** {price_data.get('Marca')}")
        st.write(f"**Modelo:** {price_data.get('Modelo')}")
        st.write(f"**Ano:** {price_data.get('AnoModelo')}")
        st.write(f"**Preço:** {price_data.get('Valor')}")
        st.write(f"**Código Fipe:** {price_data.get('CodigoFipe')}")
        st.write(f"**Combustível:** {price_data.get('Combustivel')}")
        
        # Botão para salvar em PDF
        st.markdown("### Salvar resultado em PDF")
        pdf_data = generate_pdf(price_data)
        download_button(pdf_data, "resultado_tabela_fipe.pdf")
    else:
        st.error("Não foi possível obter os dados. Tente novamente.")

# Rodapé com informações de contato (em vermelho)
st.markdown("""
---
#### Consulta Tabela FIPE
💬 Por Ary Ribeiro. Contato, através do email: aryribeiro@gmail.com
""")