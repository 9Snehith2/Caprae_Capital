import streamlit as st
import random

def render_enrichment_tab(session_state):
    st.subheader("⚙️ Enrichment")

    if st.button("Enrich All Unprocessed Companies"):
        enriched_count = 0
        for i, row in enumerate(session_state.leads):
            if row["Company"] not in session_state.enriched:
                session_state.leads[i]["Employees"] = random.randint(10, 500)
                session_state.leads[i]["Revenue"] = f"${random.randint(1, 100)}M"
                session_state.leads[i]["Founded"] = random.randint(2000, 2023)
                session_state.leads[i]["Business Type"] = random.choice(["B2B", "B2C"])
                session_state.enriched.add(row["Company"])
                enriched_count += 1

        if enriched_count > 0:
            st.success(f"✅ Enriched {enriched_count} companies.")
        else:
            st.info("All companies are already enriched.")
