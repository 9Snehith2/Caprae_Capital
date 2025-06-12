import streamlit as st
from components.overview import render_overview_tab
from components.leads import render_leads_tab
from components.enrichment import render_enrichment_tab
from components.ai_insights import render_ai_tab

from data.dummy_data import INITIAL_RESULTS, EXTENDED_RESULTS

st.set_page_config(page_title="SaaSquatch AI LeadGen", layout="wide")
st.title("🧠 SaaSquatch-Inspired Lead Generation Assistant")

# ---------- Sidebar Filters ----------
st.sidebar.header("🔍 Search Filters")
industry = st.sidebar.text_input("Industry", value="Software Development")
location = st.sidebar.text_input("Location", value="Chicago")
if st.sidebar.button("Search Leads"):
    st.session_state.leads = INITIAL_RESULTS
    st.session_state.page = 0
    st.session_state.enriched = set()
    st.sidebar.success("Results loaded!")

# ---------- Session State ----------
if "leads" not in st.session_state:
    st.session_state.leads = []
if "page" not in st.session_state:
    st.session_state.page = 0
if "enriched" not in st.session_state:
    st.session_state.enriched = set()

# ---------- Tabs Layout ----------
tabs = st.tabs(["\U0001F4CA Overview", "\U0001F4CB Leads", "\u2699\ufe0f Enrichment", "\U0001F9E0 AI Insights"])

with tabs[0]:
    render_overview_tab(st.session_state.leads, st.session_state.enriched)

with tabs[1]:
    render_leads_tab(st.session_state)

with tabs[2]:
    render_enrichment_tab(st.session_state)

with tabs[3]:
    render_ai_tab(st.session_state.leads)
