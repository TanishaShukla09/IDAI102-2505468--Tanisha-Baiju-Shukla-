import streamlit as st
import pandas as pd
from datetime import datetime, time
import json

st.set_page_config(page_title="MedTimer", page_icon="🐢", layout="centered", initial_sidebar_state="expanded")

THEMES = {
    "Sage Garden 🌿": {
        "primary": "#A7C4A0",
        "secondary": "#8A9A5B",
        "background": "linear-gradient(to bottom, #FFFCF7 0%, #F5F0E6 50%, #DDEAF2 100%)",
        "card_bg": "linear-gradient(135deg, #FFFFFF 0%, #F5F0E6 100%)",
        "text": "#2C3E2F",
        "button_gradient": "linear-gradient(135deg, #A7C4A0 0%, #8A9A5B 100%)",
        "button_hover": "linear-gradient(135deg, #8A9A5B 0%, #6B7A46 100%)",
        "icon": "🌿"
    },
    "Ocean Breeze 🌊": {
        "primary": "#4A90A4",
        "secondary": "#2E6F85",
        "background": "linear-gradient(to bottom, #E0F2F7 0%, #B3E5F0 50%, #81D4E8 100%)",
        "card_bg": "linear-gradient(135deg, #FFFFFF 0%, #E0F7FA 100%)",
        "text": "#1B3A47",
        "button_gradient": "linear-gradient(135deg, #4DD0E1 0%, #26C6DA 100%)",
        "button_hover": "linear-gradient(135deg, #26C6DA 0%, #00ACC1 100%)",
        "icon": "🌊"
    },
    "Sunset Warmth 🌅": {
        "primary": "#E8956B",
        "secondary": "#D97847",
        "background": "linear-gradient(to bottom, #FFF8E1 0%, #FFE0B2 50%, #FFCCBC 100%)",
        "card_bg": "linear-gradient(135deg, #FFFFFF 0%, #FFF3E0 100%)",
        "text": "#4E2A1B",
        "button_gradient": "linear-gradient(135deg, #FFB74D 0%, #FF9800 100%)",
        "button_hover": "linear-gradient(135deg, #FF9800 0%, #F57C00 100%)",
        "icon": "🌅"
    },
    "Lavender Dreams 💜": {
        "primary": "#B39DDB",
        "secondary": "#9575CD",
        "background": "linear-gradient(to bottom, #F3E5F5 0%, #E1BEE7 50%, #CE93D8 100%)",
        "card_bg": "linear-gradient(135deg, #FFFFFF 0%, #F3E5F5 100%)",
        "text": "#4A148C",
        "button_gradient": "linear-gradient(135deg, #BA68C8 0%, #AB47BC 100%)",
        "button_hover": "linear-gradient(135deg, #AB47BC 0%, #9C27B0 100%)",
        "icon": "💜"
    },
    "Spring Blossom 🌸": {
        "primary": "#F48FB1",
        "secondary": "#EC407A",
        "background": "linear-gradient(to bottom, #FCE4EC 0%, #F8BBD0 50%, #F48FB1 100%)",
        "card_bg": "linear-gradient(135deg, #FFFFFF 0%, #FCE4EC 100%)",
        "text": "#880E4F",
        "button_gradient": "linear-gradient(135deg, #F48FB1 0%, #EC407A 100%)",
        "button_hover": "linear-gradient(135deg, #EC407A 0%, #E91E63 100%)",
        "icon": "🌸"
    }
}

st.sidebar.markdown("# ⚙ Settings")
st.sidebar.markdown("---")

st.sidebar.markdown("### 🎨 Choose Your Theme")
selected_theme_name = st.sidebar.selectbox(
    "Theme",
    list(THEMES.keys()),
    key="theme_selector",
    label_visibility="collapsed"
)
theme = THEMES[selected_theme_name]

st.sidebar.markdown("### 📝 Text Size")
font_size_value = st.sidebar.select_slider(
    "Adjust text size:",
    options=[18, 20, 22, 24],
    value=20,
    key="font_size_selector",
    label_visibility="collapsed"
)

st.sidebar.markdown("### 🔄 App Mode")
app_mode = st.sidebar.radio(
    "Choose Mode:",
    ["🐢 Guided Setup (Step-by-Step)", "⚡ Quick Add (Advanced)"],
    key="app_mode"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Tips")
if "Guided" in app_mode:
    st.sidebar.info("🐢 Follow the step-by-step wizard to set up your medicines slowly and carefully.")
else:
    st.sidebar.info("⚡ Quickly add medicines if you're already familiar with the app.")

selected_font_size = f"{font_size_value}px"

base_size = int(selected_font_size.replace("px", ""))
heading_size = f"{base_size + 8}px"
subheading_size = f"{base_size + 4}px"
label_size = f"{base_size + 2}px"

st.markdown(f"""
  <style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
  
  * {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  }}
  
  body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {{
    background: {theme['background']} !important;
  }}
  
  [data-testid="stSidebar"] {{
    background: {theme['card_bg']} !important;
    border-right: 3px solid {theme['primary']} !important;
    min-width: 320px !important;
    max-width: 320px !important;
  }}
  
  [data-testid="stSidebar"] * {{
    color: {theme['text']} !important;
  }}
  
  [data-testid="stSidebar"] > div:first-child {{
    padding: 2rem 1.5rem !important;
  }}
  
  input[type="text"] {{
    -webkit-autocomplete: off !important;
    autocomplete: off !important;
  }}
  
  input, textarea,
  .stTextInput input, .stTextArea textarea, 
  .stTimeInput input, .stNumberInput input
  {{
    background: {theme['card_bg']} !important;
    color: #000000 !important;
    border-radius: 10px !important;
    border: 2.5px solid {theme['primary']} !important;
    font-weight: 500 !important;
    font-size: {selected_font_size} !important;
    padding: 14px 18px !important;
    height: auto !important;
    min-height: 50px !important;
    line-height: 1.5 !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }}
  
  input::placeholder, textarea::placeholder {{
    color: #666666 !important;
    opacity: 0.8 !important;
    font-weight: 400 !important;
    font-size: {selected_font_size} !important;
  }}
  
  input:focus, textarea:focus {{
    border-color: {theme['secondary']} !important;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.15), 0 0 0 3px rgba(0, 0, 0, 0.05) !important;
    transform: translateY(-1px) !important;
    outline: none !important;
  }}
  
  /* DROPDOWN FIXES */
  .stSelectbox > div {{
    width: 100% !important;
    max-width: 100% !important;
  }}
  
  .stSelectbox > div > div {{
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
  }}
  
  /* Main dropdown container with solid borders on ALL sides */
  div[data-baseweb="select"] {{
    background: {theme['card_bg']} !important;
    border-radius: 10px !important;
    border: 2.5px solid {theme['primary']} !important;
    padding: 0 !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
    transition: all 0.3s ease !important;
  }}
  
  div[data-baseweb="select"]:hover {{
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.15) !important;
    border-color: {theme['secondary']} !important;
  }}
  
  /* Inner dropdown padding */
  div[data-baseweb="select"] > div {{
    background: transparent !important;
    border: none !important;
    padding: 14px 18px !important;
    min-height: 50px !important;
    width: 100% !important;
  }}
  
  div[data-baseweb="select"] > div > div {{
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    width: 100% !important;
  }}
  
  /* NUCLEAR OPTION - Force all dropdown text to be BLACK and VISIBLE */
  div[data-baseweb="select"],
  div[data-baseweb="select"] *,
  div[data-baseweb="select"] span,
  div[data-baseweb="select"] div,
  div[data-baseweb="select"] input,
  div[data-baseweb="select"] [role="button"],
  div[data-baseweb="select"] [role="button"] *,
  div[data-baseweb="select"] [data-baseweb="select-value"],
  div[data-baseweb="select"] [data-baseweb="select-value"] * {{
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    font-weight: 600 !important;
    opacity: 1 !important;
    font-size: {selected_font_size} !important;
  }}
  
  /* Dropdown arrow */
  div[data-baseweb="select"] svg {{
    color: {theme['secondary']} !important;
    fill: {theme['secondary']} !important;
    width: 20px !important;
    height: 20px !important;
  }}
  
  .stTimeInput input {{
    height: auto !important;
    min-height: 50px !important;
    padding: 14px 18px !important;
    font-size: {selected_font_size} !important;
  }}
  
  /* Dropdown menu items */
  ul[role="listbox"] {{
    background: {theme['card_bg']} !important;
    max-height: 320px !important;
    min-width: 100% !important;
    border-radius: 10px !important;
    border: 2.5px solid {theme['primary']} !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2) !important;
    padding: 8px !important;
  }}
  
  ul[role="listbox"] li {{
    background: transparent !important;
    color: #000000 !important;
    padding: 12px 16px !important;
    font-size: {selected_font_size} !important;
    font-weight: 500 !important;
    border-radius: 8px !important;
    margin: 4px 0 !important;
    transition: all 0.25s ease !important;
  }}
  
  ul[role="listbox"] li:hover {{
    background: {theme['button_gradient']} !important;
    color: #FFFFFF !important;
    transform: translateX(4px) !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15) !important;
  }}
  
  label, .stSelectbox label, .stTextInput label, 
  .stTextArea label, .stNumberInput label, 
  .stTimeInput label, .stFileUploader label {{
    color: {theme['text']} !important;
    font-weight: 600 !important;
    font-size: {label_size} !important;
    margin-bottom: 10px !important;
    display: block !important;
    letter-spacing: 0.3px !important;
  }}
  
  div.stButton button, .stDownloadButton button {{
    background: {theme['button_gradient']} !important;
    color: #FFFFFF !important;
    border-radius: 10px !important;
    border: none !important;
    font-weight: 600 !important;
    font-size: {selected_font_size} !important;
    padding: 12px 24px !important;
    transition: all 0.35s ease !important;
    width: 100% !important;
    min-height: 48px !important;
    max-height: 48px !important;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.15) !important;
    letter-spacing: 0.5px !important;
    position: relative !important;
    overflow: hidden !important;
    cursor: pointer !important;
  }}
  
  div.stButton button::after {{
    content: '' !important;
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    width: 0 !important;
    height: 0 !important;
    border-radius: 50% !important;
    background: rgba(255, 255, 255, 0.4) !important;
    transform: translate(-50%, -50%) !important;
    transition: width 0.5s ease, height 0.5s ease !important;
  }}
  
  div.stButton button:hover {{
    background: {theme['button_hover']} !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.25) !important;
  }}
  
  div.stButton button:active::after {{
    width: 300px !important;
    height: 300px !important;
  }}
  
  div.stButton button:active {{
    transform: translateY(0px) scale(0.98) !important;
  }}
  
  h1, h2, h3, h4, h5, h6 {{
    color: {theme['text']} !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    line-height: 1.4 !important;
  }}
  
  h1 {{
    font-size: {heading_size} !important;
    margin-bottom: 0.5rem !important;
  }}
  
  h2 {{
    font-size: {subheading_size} !important;
  }}
  
  h3 {{
    font-size: {label_size} !important;
  }}
  
  .step-indicator {{
    text-align: center;
    font-size: {label_size};
    font-weight: 600;
    color: #FFFFFF;
    background: {theme['button_gradient']};
    padding: 16px 24px;
    border-radius: 10px;
    margin: 20px auto;
    max-width: 600px;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.2);
    border: 2px solid {theme['secondary']};
    animation: gentle-glow 3s ease-in-out infinite alternate;
    letter-spacing: 0.8px;
  }}
  
  @keyframes gentle-glow {{
    from {{
      box-shadow: 0 3px 12px rgba(0, 0, 0, 0.2);
    }}
    to {{
      box-shadow: 0 5px 18px rgba(0, 0, 0, 0.3);
    }}
  }}
  
  .stAlert, div[data-baseweb="notification"] {{
    background: {theme['card_bg']} !important;
    color: {theme['text']} !important;
    border: 2px solid {theme['primary']} !important;
    border-radius: 10px !important;
    padding: 16px 20px !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1) !important;
    font-size: {selected_font_size} !important;
  }}
  
  .element-container div[data-testid="stMarkdownContainer"] p {{
    color: {theme['text']} !important;
    font-size: {selected_font_size} !important;
  }}
  
  .stFileUploader, section[data-testid="stFileUploader"],
  [data-testid="stFileUploader"] > div,
  [data-testid="stFileUploader"] section {{
    background: {theme['card_bg']} !important;
    border: 2.5px solid {theme['primary']} !important;
    border-radius: 10px !important;
    padding: 20px !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1) !important;
  }}
  
  section[data-testid="stFileUploadDropzone"],
  section[data-testid="stFileUploadDropzone"] > div,
  section[data-testid="stFileUploadDropzone"] > div > div,
  [data-testid="stFileUploadDropzone"] div {{
    background: {theme['card_bg']} !important;
    border-radius: 8px !important;
    border: 2.5px dashed {theme['primary']} !important;
    color: {theme['text']} !important;
    padding: 20px !important;
  }}
  
  section[data-testid="stFileUploadDropzone"] small,
  section[data-testid="stFileUploadDropzone"] span,
  [data-testid="stFileUploadDropzone"] small,
  [data-testid="stFileUploadDropzone"] span,
  [data-testid="stFileUploadDropzone"] p,
  section[data-testid="stFileUploadDropzone"] p,
  section[data-testid="stFileUploadDropzone"] div,
  [data-testid="stFileUploadDropzone"] div {{
    color: #000000 !important;
    font-weight: 500 !important;
    font-size: {selected_font_size} !important;
  }}
  
  section[data-testid="stFileUploadDropzone"] button,
  [data-testid="stFileUploadDropzone"] button {{
    background: {theme['button_gradient']} !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 10px 20px !important;
    font-weight: 600 !important;
    font-size: {selected_font_size} !important;
    transition: all 0.3s ease !important;
  }}
  
  section[data-testid="stFileUploadDropzone"] button:hover {{
    transform: scale(1.05) !important;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.2) !important;
  }}
  
  .stTextInput > div, .stSelectbox > div, .stTimeInput > div {{
    border: none !important;
    background: transparent !important;
    border-bottom: none !important;
  }}
  
  .med-card {{
    background: {theme['card_bg']};
    border: 2.5px solid {theme['primary']};
    border-radius: 12px;
    padding: 22px;
    margin: 16px 0;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.12);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
  }}
  
  .med-card::before {{
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.4s ease;
  }}
  
  .med-card:hover::before {{
    opacity: 1;
  }}
  
  .med-card:hover {{
    box-shadow: 0 5px 18px rgba(0, 0, 0, 0.2);
    transform: translateY(-3px);
  }}
  
  .med-card-taken {{
    background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%);
    border: 2.5px solid #66BB6A;
    box-shadow: 0 3px 12px rgba(102, 187, 106, 0.2);
  }}
  
  .med-card-taken:hover {{
    box-shadow: 0 5px 18px rgba(102, 187, 106, 0.3);
  }}
  
  .med-card-missed {{
    background: linear-gradient(135deg, #FFEBEE 0%, #FFCDD2 100%);
    border: 2.5px solid #EF5350;
    box-shadow: 0 3px 12px rgba(239, 83, 80, 0.2);
    animation: gentle-pulse-red 2.5s ease-in-out infinite;
  }}
  
  @keyframes gentle-pulse-red {{
    0%, 100% {{ box-shadow: 0 3px 12px rgba(239, 83, 80, 0.2); }}
    50% {{ box-shadow: 0 5px 16px rgba(239, 83, 80, 0.3); }}
  }}
  
  .med-card-due {{
    background: linear-gradient(135deg, #FFFDE7 0%, #FFF9C4 100%);
    border: 2.5px solid #FFCA28;
    box-shadow: 0 3px 12px rgba(255, 202, 40, 0.2);
    animation: gentle-pulse-yellow 2.5s ease-in-out infinite;
  }}
  
  @keyframes gentle-pulse-yellow {{
    0%, 100% {{ box-shadow: 0 3px 12px rgba(255, 202, 40, 0.2); }}
    50% {{ box-shadow: 0 5px 16px rgba(255, 202, 40, 0.3); }}
  }}
  
  .med-card *, .med-card-taken *, .med-card-missed *, .med-card-due * {{
    font-size: {selected_font_size} !important;
    color: {theme['text']} !important;
  }}
  
  .element-container {{
    animation: gentle-fade-in 0.5s ease-in;
  }}
  
  @keyframes gentle-fade-in {{
    from {{ opacity: 0; transform: translateY(8px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}
  
  p {{
    font-size: {selected_font_size} !important;
    color: {theme['text']} !important;
    line-height: 1.6 !important;
  }}
  
  .stRadio label, .stSlider label {{
    font-size: {selected_font_size} !important;
  }}
  
  hr {{
    border: none !important;
    border-top: 2px solid {theme['primary']} !important;
    margin: 25px 0 !important;
  }}
  
  .theme-icon {{
    font-size: 3rem;
    text-align: center;
    margin: 15px 0;
    animation: float 3s ease-in-out infinite;
  }}
  
  @keyframes float {{
    0%, 100% {{ transform: translateY(0px); }}
    50% {{ transform: translateY(-8px); }}
  }}
  
  .stSlider {{
    padding: 10px 0 !important;
  }}
  
  .stSlider > div > div > div > div {{
    background-color: {theme['primary']} !important;
  }}
  
  .stSlider > div > div > div > div > div {{
    background-color: {theme['secondary']} !important;
  }}
  </style>
""", unsafe_allow_html=True)

COUNTRIES = {
    "India": {"timezones": ["Asia/Kolkata"], "states": ["All India"]},
    "United States": {"timezones": ["America/New_York", "America/Chicago", "America/Denver", "America/Los_Angeles"], 
                      "states": ["Eastern (NY, FL)", "Central (TX, IL)", "Mountain (CO, AZ)", "Pacific (CA, WA)"]},
    "United Kingdom": {"timezones": ["Europe/London"], "states": ["All UK"]},
    "Australia": {"timezones": ["Australia/Sydney", "Australia/Melbourne", "Australia/Brisbane", "Australia/Perth"],
                  "states": ["New South Wales", "Victoria", "Queensland", "Western Australia"]},
    "Canada": {"timezones": ["America/Toronto", "America/Vancouver", "America/Edmonton"],
               "states": ["Ontario/Quebec", "British Columbia", "Alberta"]},
    "Germany": {"timezones": ["Europe/Berlin"], "states": ["All Germany"]},
    "France": {"timezones": ["Europe/Paris"], "states": ["All France"]},
    "Japan": {"timezones": ["Asia/Tokyo"], "states": ["All Japan"]},
    "China": {"timezones": ["Asia/Shanghai"], "states": ["All China"]},
    "Brazil": {"timezones": ["America/Sao_Paulo", "America/Manaus"], "states": ["Southeast", "North"]},
    "Spain": {"timezones": ["Europe/Madrid"], "states": ["All Spain"]},
    "Italy": {"timezones": ["Europe/Rome"], "states": ["All Italy"]},
}

DISEASES = {
    "India": {
        "Hypertension": ["Amlodipine 5mg", "Telmisartan 40mg", "Atenolol 50mg"],
        "Diabetes Type 2": ["Metformin 500mg", "Glimepiride 1mg", "Sitagliptin 50mg"],
        "Hypothyroidism": ["Thyroxine 50mcg", "Levothyroxine 100mcg"],
        "Asthma": ["Salbutamol Inhaler", "Budesonide", "Montelukast"],
        "COPD": ["Tiotropium Inhaler", "Formoterol", "N-Acetylcysteine"],
        "Heart Disease": ["Aspirin 75mg", "Atorvastatin 10mg", "Metoprolol 25mg"],
        "Arthritis": ["Diclofenac 50mg", "Paracetamol 500mg", "Hydroxychloroquine"],
        "Depression": ["Escitalopram 10mg", "Sertraline 50mg"],
        "Anxiety": ["Alprazolam 0.5mg", "Propranolol 20mg"],
        "Migraine": ["Sumatriptan 50mg", "Propranolol 40mg", "Topiramate 25mg"]
    },
    "United States": {
        "Hypertension": ["Lisinopril 10mg", "Amlodipine 5mg", "Losartan 50mg"],
        "Diabetes Type 2": ["Metformin 500mg", "Insulin Glargine", "Sitagliptin 100mg"],
        "Hypothyroidism": ["Levothyroxine 50mcg", "Synthroid 75mcg"],
        "Asthma": ["Albuterol Inhaler", "Fluticasone 250mcg", "Montelukast 10mg"],
        "COPD": ["Tiotropium Respimat", "Albuterol", "Prednisone"],
        "Heart Disease": ["Aspirin 81mg", "Atorvastatin 20mg", "Metoprolol 50mg"],
        "Arthritis": ["Ibuprofen 400mg", "Naproxen 500mg", "Methotrexate"],
        "Depression": ["Sertraline 50mg", "Fluoxetine 20mg", "Bupropion XL"],
        "Anxiety": ["Buspirone 10mg", "Hydroxyzine 25mg"],
        "Migraine": ["Sumatriptan 100mg", "Rizatriptan 10mg", "Topiramate 50mg"]
    }
}

for country in ["United Kingdom", "Germany", "France", "Spain", "Italy"]:
    DISEASES[country] = DISEASES["United States"].copy()
for country in ["Australia", "Canada"]:
    DISEASES[country] = DISEASES["United States"].copy()
for country in ["Japan", "China", "Brazil"]:
    DISEASES[country] = DISEASES["India"].copy()

def load_data():
    try:
        with open("med_data.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open("med_data.json", "w") as f:
        json.dump(data, f, indent=4)

medicine_data = load_data()

if "step" not in st.session_state:
    st.session_state.step = 1
if "meds" not in st.session_state:
    st.session_state.meds = []
if "profile" not in st.session_state:
    st.session_state.profile = {}
if "med_status" not in st.session_state:
    st.session_state.med_status = {}
if "show_balloons" not in st.session_state:
    st.session_state.show_balloons = False

def get_med_status(med_name, med_time):
    current_time = datetime.now().time()
    med_time_obj = datetime.strptime(med_time, "%H:%M").time()
    
    if med_name in st.session_state.med_status:
        return st.session_state.med_status[med_name]
    
    if current_time > med_time_obj:
        return "missed"
    elif current_time.hour == med_time_obj.hour and abs(current_time.minute - med_time_obj.minute) <= 30:
        return "due"
    else:
        return "upcoming"

if st.session_state.show_balloons:
    st.balloons()
    st.session_state.show_balloons = False

st.markdown(f"<div class='theme-icon'>{theme['icon']}</div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;'>🐢 MedTimer</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; font-size:1.2rem; font-weight:500;'>Slow & Steady Wins Your Health Race</p>", unsafe_allow_html=True)
st.write("")

if "Guided" in app_mode:
    
    step_names = ["Name", "Location", "Condition", "Medicines", "Schedule", "Dashboard"]
    current_step = st.session_state.step
    st.markdown(f"<div class='step-indicator'>Step {current_step} of 6: {step_names[current_step-1]}</div>", unsafe_allow_html=True)
    st.write("")

    if st.session_state.step == 1:
        st.markdown("<h2 style='text-align:center;'>🐢 Hi there! What's your name?</h2>", unsafe_allow_html=True)
        st.write("")
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            name = st.text_input("Your Name:", value=st.session_state.profile.get("name", ""), placeholder="Enter your name here", key="name_input")
        st.write("")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Next →", use_container_width=True, key="step1_next"):
                if name.strip():
                    st.session_state.profile["name"] = name
                    st.session_state.step = 2
                    st.rerun()
                else:
                    st.error("Please enter your name!")

    elif st.session_state.step == 2:
        st.markdown(f"<h2 style='text-align:center;'>🐢 Nice to meet you, {st.session_state.profile.get('name', '')}!</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;'>Where are you located?</h3>", unsafe_allow_html=True)
        st.write("")
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            country_list = list(COUNTRIES.keys())
            default_country = st.session_state.profile.get("country", country_list[0])
            if default_country not in country_list:
                default_country = country_list[0]
            country_index = country_list.index(default_country)
            country = st.selectbox("Select Your Country:", country_list, index=country_index, key="country_select")
        st.write("")
        country_data = COUNTRIES[country]
        if len(country_data["timezones"]) == 1:
            timezone = country_data["timezones"][0]
            st.info(f"✅ Timezone automatically set to: *{timezone}*")
        else:
            col1, col2, col3 = st.columns([1, 3, 1])
            with col2:
                st.write("Select your region for accurate timezone:")
                state_idx = st.selectbox("Region/State:", range(len(country_data["states"])), 
                                        format_func=lambda x: country_data["states"][x], key="state_select")
            timezone = country_data["timezones"][state_idx]
            st.info(f"✅ Your timezone: *{timezone}*")
        st.write("")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("← Back", use_container_width=True, key="step2_back"):
                st.session_state.step = 1
                st.rerun()
        with col3:
            if st.button("Next →", use_container_width=True, key="step2_next"):
                st.session_state.profile["country"] = country
                st.session_state.profile["timezone"] = timezone
                st.session_state.step = 3
                st.rerun()

    elif st.session_state.step == 3:
        st.markdown(f"<h2 style='text-align:center;'>🐢 {st.session_state.profile.get('name', '')}, what condition are you managing?</h2>", unsafe_allow_html=True)
        st.write("")
        country = st.session_state.profile.get("country", "India")
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            disease_list = list(DISEASES[country].keys())
            disease = st.selectbox("Select Your Chronic Condition:", disease_list, key="disease_select")
        st.write("")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("← Back", use_container_width=True, key="step3_back"):
                st.session_state.step = 2
                st.rerun()
        with col3:
            if st.button("Next →", use_container_width=True, key="step3_next"):
                st.session_state.profile["disease"] = disease
                suggested_meds = DISEASES[country][disease]
                st.session_state.meds = [{"name": m, "time": "08:00"} for m in suggested_meds]
                st.session_state.step = 4
                st.rerun()

    elif st.session_state.step == 4:
        st.markdown(f"<h2 style='text-align:center;'>💊 Your Medicines for {st.session_state.profile.get('disease', '')}</h2>", unsafe_allow_html=True)
        st.info("✏ You can edit medicine names below. We've suggested common medicines for your condition.")
        st.write("")
        st.markdown("### Current Medicines:")
        st.write("")
        for i, med in enumerate(st.session_state.meds):
            col1, col2 = st.columns([5, 1])
            with col1:
                new_name = st.text_input(f"Medicine {i+1}:", value=med["name"], key=f"med_name_{i}")
                st.session_state.meds[i]["name"] = new_name
            with col2:
                st.write("")
                st.write("")
                if st.button("🗑", key=f"delete_{i}"):
                    st.session_state.meds.pop(i)
                    st.rerun()
            st.write("")
        st.write("")
        st.markdown("### Add Additional Medicine (Optional)")
        st.write("")
        col1, col2 = st.columns([4, 1])
        with col1:
            custom_name = st.text_input("Medicine Name:", key="custom_med", placeholder="Enter medicine name")
        with col2:
            st.write("")
            st.write("")
            if st.button("➕ Add", use_container_width=True, key="add_custom_med"):
                if custom_name.strip():
                    st.session_state.meds.append({"name": custom_name, "time": "08:00"})
                    st.success(f"✅ Added {custom_name}")
                    st.rerun()
        st.write("")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("← Back", use_container_width=True, key="step4_back"):
                st.session_state.step = 3
                st.rerun()
        with col3:
            if st.button("Next →", use_container_width=True, key="step4_next"):
                st.session_state.step = 5
                st.rerun()

    elif st.session_state.step == 5:
        st.markdown("<h2 style='text-align:center;'>⏰ Set Your Medicine Timers</h2>", unsafe_allow_html=True)
        st.info("🐢 Set the time you need to take each medicine")
        st.write("")
        for i, med in enumerate(st.session_state.meds):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown(f"### {med['name']}")
            with col2:
                time_val = st.time_input(f"Time for {med['name']}", 
                                        datetime.strptime(med["time"], "%H:%M").time(), 
                                        key=f"time_{i}", label_visibility="collapsed")
                st.session_state.meds[i]["time"] = time_val.strftime("%H:%M")
            st.write("")
        st.write("")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("← Back", use_container_width=True, key="step5_back"):
                st.session_state.step = 4
                st.rerun()
        with col3:
            if st.button("🐢 Go to Dashboard", use_container_width=True, key="step5_next"):
                st.session_state.step = 6
                st.rerun()

    elif st.session_state.step == 6:
        st.markdown(f"<h2 style='text-align:center;'>🐢 Welcome Back, {st.session_state.profile.get('name', '')}!</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center; font-size:1.1rem;'>Managing: <strong>{st.session_state.profile.get('disease', '')}</strong> | Location: <strong>{st.session_state.profile.get('country', '')}</strong></p>", unsafe_allow_html=True)
        st.write("")
        st.markdown("### 📅 Today's Medicine Schedule")
        st.write("")
        if not st.session_state.meds:
            st.info("No medicines added yet.")
        else:
            for i, med in enumerate(sorted(st.session_state.meds, key=lambda x: x["time"])):
                status = get_med_status(med['name'], med['time'])
                if med['name'] in st.session_state.med_status and st.session_state.med_status[med['name']] == "taken":
                    card_class = "med-card-taken"
                    status_icon = "🟩 Taken"
                    button_disabled = True
                elif status == "missed":
                    card_class = "med-card-missed"
                    status_icon = "🟥 Missed"
                    button_disabled = False
                elif status == "due":
                    card_class = "med-card-due"
                    status_icon = "🔴 Due Now"
                    button_disabled = False
                else:
                    card_class = "med-card"
                    status_icon = "⏰ Upcoming"
                    button_disabled = False
                st.markdown(f"<div class='{card_class}'>", unsafe_allow_html=True)
                col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
                with col1:
                    st.markdown(f"{med['name']}")
                with col2:
                    st.markdown(f"🕐 {med['time']}")
                with col3:
                    st.markdown(f"{status_icon}")
                with col4:
                    if not button_disabled:
                        if st.button(f"✅ Taken", key=f"taken_{med['name']}_{i}"):
                            st.session_state.med_status[med['name']] = "taken"
                            st.session_state.show_balloons = True
                            st.success(f"🎉 Great job! You took {med['name']}")
                            st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)
                st.write("")
        st.write("")
        st.markdown("---")
        st.markdown("### 📄 Upload Prescription")
        st.write("")
        st.markdown(f"""
            <div style='background: {theme['card_bg']}; border: 2.5px solid {theme['primary']}; border-radius: 12px; padding: 20px; margin: 10px 0;'>
                <p style='font-weight: 600; margin: 0;'>📎 Upload your prescription (PDF or Image)</p>
            </div>
        """, unsafe_allow_html=True)
        report = st.file_uploader("prescription_upload", type=["pdf", "jpg", "jpeg", "png"], key="prescription", label_visibility="collapsed")
        if report:
            st.success("✅ Prescription uploaded successfully!")
        st.write("")
        st.markdown("---")
        st.markdown("### 💾 Save or Restore Your Data")
        st.write("")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("*Download Your Data*")
            data_to_save = {"profile": st.session_state.profile, "meds": st.session_state.meds, "med_status": st.session_state.med_status}
            st.download_button(label="💾 Download Data", data=json.dumps(data_to_save, indent=2), 
                             mime="application/json", file_name="medtimer_data.json", use_container_width=True, key="download_data")
        with col2:
            st.markdown("*Restore from File*")
            st.markdown(f"""
                <div style='background: {theme['card_bg']}; border: 2.5px solid {theme['primary']}; border-radius: 12px; padding: 15px; margin-bottom: 10px;'>
                    <p style='font-weight: 600; margin: 0; font-size: 0.9rem;'>📂 Upload saved JSON file</p>
                </div>
            """, unsafe_allow_html=True)
            upload = st.file_uploader("restore_upload", type="json", key="restore", label_visibility="collapsed")
            if upload:
                try:
                    loaded = json.load(upload)
                    st.session_state.profile = loaded["profile"]
                    st.session_state.meds = loaded["meds"]
                    st.session_state.med_status = loaded.get("med_status", {})
                    st.session_state.step = 1
                    st.success("✅ Data restored!")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Could not load data: {str(e)}")
        st.write("")
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("⚙ Edit Settings", use_container_width=True, key="edit_settings"):
                st.session_state.step = 1
                st.rerun()

else:
    st.markdown("## ⚡ Quick Add Medicine")
    st.write("")
    st.markdown("### 📍 Select Location & Condition")
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        country = st.selectbox("Country", list(COUNTRIES.keys()), key="quick_country")
    with col2:
        state_options = COUNTRIES[country]["states"]
        state = st.selectbox("State / Region", state_options, key="quick_state")
    timezone = st.selectbox("Timezone", COUNTRIES[country]["timezones"], key="quick_timezone")
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        disease_list = list(DISEASES[country].keys())
        disease = st.selectbox("Disease / Condition", disease_list, key="quick_disease")
    with col2:
        medicine_list = DISEASES[country][disease]
        medicine = st.selectbox("Select Medicine", medicine_list, key="quick_medicine")
    st.write("")
    st.markdown("---")
    st.markdown("### ⏰ Set Reminder Time")
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        dose_time = st.time_input("Select Reminder Time", key="quick_time")
    with col2:
        notes = st.text_input("Notes (Optional)", placeholder="e.g., Take with food", key="quick_notes")
    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("➕ Add Medicine", use_container_width=True, key="add_medicine_btn"):
            entry = {"country": country, "state": state, "timezone": timezone, "disease": disease, 
                    "medicine": medicine, "time": dose_time.strftime("%H:%M"), "notes": notes, "status": "Due"}
            medicine_data.append(entry)
            save_data(medicine_data)
            st.success(f"✅ {medicine} added successfully!")
            st.balloons()
            st.rerun()
    st.write("")
    st.markdown("---")
    st.write("")
    st.markdown("### 💊 Your Medicines")
    st.write("")
    if len(medicine_data) == 0:
        st.info("🐢 No medicines added yet. Add your first medicine above!")
    else:
        sorted_medicines = sorted(medicine_data, key=lambda x: x['time'])
        for i, med in enumerate(sorted_medicines):
            card_class = "med-card"
            if med["status"] == "Taken":
                card_class = "med-card-taken"
                status_icon = "🟩 Taken"
            elif med["status"] == "Missed":
                card_class = "med-card-missed"
                status_icon = "🟥 Missed"
            elif med["status"] == "Due":
                current_time = datetime.now().time()
                med_time = datetime.strptime(med["time"], "%H:%M").time()
                if current_time.hour == med_time.hour and abs(current_time.minute - med_time.minute) <= 30:
                    card_class = "med-card-due"
                    status_icon = "🔴 Due Now"
                else:
                    status_icon = "⏰ Scheduled"
            st.markdown(f"<div class='{card_class}'>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([3, 2, 2])
            with col1:
                st.markdown(f"💊 {med['medicine']}")
                st.markdown(f"{med['disease']}")
            with col2:
                st.markdown(f"🕐 *{med['time']}*")
                if med['notes']:
                    st.markdown(f"📝 {med['notes']}")
            with col3:
                st.markdown(f"{status_icon}")
                st.markdown(f"📍 {med['state']}")
            st.write("")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                if med["status"] != "Taken":
                    if st.button("✅ Mark Taken", key=f"taken_quick_{i}", use_container_width=True):
                        medicine_data[medicine_data.index(med)]["status"] = "Taken"
                        save_data(medicine_data)
                        st.balloons()
                        st.rerun()
            with col2:
                if med["status"] != "Missed":
                    if st.button("🟥 Mark Missed", key=f"missed_quick_{i}", use_container_width=True):
                        medicine_data[medicine_data.index(med)]["status"] = "Missed"
                        save_data(medicine_data)
                        st.rerun()
            with col3:
                if med["status"] != "Due":
                    if st.button("🔄 Reset", key=f"reset_quick_{i}", use_container_width=True):
                        medicine_data[medicine_data.index(med)]["status"] = "Due"
                        save_data(medicine_data)
                        st.rerun()
            with col4:
                if st.button("🗑 Delete", key=f"delete_quick_{i}", use_container_width=True):
                    medicine_data.pop(medicine_data.index(med))
                    save_data(medicine_data)
                    st.success("Medicine deleted!")
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
            st.write("")
        st.write("")
        st.markdown("---")
        st.markdown("### 📊 Your Statistics")
        st.write("")
        total_meds = len(medicine_data)
        taken_count = sum(1 for m in medicine_data if m["status"] == "Taken")
        missed_count = sum(1 for m in medicine_data if m["status"] == "Missed")
        due_count = sum(1 for m in medicine_data if m["status"] == "Due")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"""
                <div style='background: {theme['card_bg']}; border: 2.5px solid {theme['primary']}; 
                border-radius: 12px; padding: 20px; text-align: center;'>
                    <h2 style='margin: 0;'>{total_meds}</h2>
                    <p style='margin: 5px 0 0 0;'>Total</p>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div style='background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%); 
                border: 2.5px solid #66BB6A; border-radius: 12px; padding: 20px; text-align: center;'>
                    <h2 style='margin: 0; color: #2E7D32;'>{taken_count}</h2>
                    <p style='margin: 5px 0 0 0; color: #2E7D32;'>Taken</p>
                </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
                <div style='background: linear-gradient(135deg, #FFEBEE 0%, #FFCDD2 100%); 
                border: 2.5px solid #EF5350; border-radius: 12px; padding: 20px; text-align: center;'>
                    <h2 style='margin: 0; color: #C62828;'>{missed_count}</h2>
                    <p style='margin: 5px 0 0 0; color: #C62828;'>Missed</p>
                </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
                <div style='background: linear-gradient(135deg, #FFFDE7 0%, #FFF9C4 100%); 
                border: 2.5px solid #FFCA28; border-radius: 12px; padding: 20px; text-align: center;'>
                    <h2 style='margin: 0; color: #F57F17;'>{due_count}</h2>
                    <p style='margin: 5px 0 0 0; color: #F57F17;'>Due</p>
                </div>
            """, unsafe_allow_html=True)
        st.write("")
        st.markdown("### 💾 Backup & Restore")
        st.write("")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("*Download All Data*")
            st.download_button(label="💾 Download JSON", data=json.dumps(medicine_data, indent=2), 
                             mime="application/json", file_name="medtimer_medicines.json", 
                             use_container_width=True, key="download_all_data")
        with col2:
            st.markdown("*Clear All Data*")
            if st.button("🗑 Clear All Medicines", use_container_width=True, key="clear_all"):
                medicine_data.clear()
                save_data(medicine_data)
                st.success("✅ All medicines cleared!")
                st.rerun()

st.write("")
st.write("")
st.markdown("---")
st.markdown(f"<h3 style='text-align:center;'>{theme['icon']} Slow and steady wins the health race! {theme['icon']}</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; opacity: 0.7;'>Made with 💚 for your health journey</p>", unsafe_allow_html=True)