import streamlit as st
from utils.ai_tools import summarize_text, categorize_company, score_lead

def render_ai_tab(leads):
    st.subheader("\U0001F9E0 AI-Powered Insights")

    if leads:
        selected_company = st.selectbox("Choose a company to analyze:", [row["Company"] for row in leads])
        company = next((row for row in leads if row["Company"] == selected_company), None)

        if company:
            st.markdown(f"**\U0001F50E Original Description:**")
            st.info(company.get("Description", "No description available."))

            if st.button("\U0001F9E0 Summarize Description"):
                summary = summarize_text(company.get("Description", ""))
                st.success(f"**Summary:** {summary}")

            if st.button("\U0001F3F7\ufe0f Categorize Company"):
                category = categorize_company(company.get("Description", ""))
                st.info(f"**Predicted Category:** `{category}`")

            if st.button("\U0001F4CA Score Lead Quality"):
                score, reason = score_lead(company)
                st.markdown(f"### Score: {score}")
                st.caption(f"{reason}")
