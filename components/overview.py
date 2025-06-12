import streamlit as st

def render_overview_tab(leads, enriched):
    st.subheader("\U0001F4CA Dashboard Summary")
    total_leads = len(leads)
    enriched_count = len(enriched)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Leads", total_leads)
    col2.metric("Enriched", enriched_count)
    col3.metric("Search Status", "Loaded" if leads else "Waiting")
