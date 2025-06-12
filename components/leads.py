import streamlit as st
import pandas as pd
import math
from data.dummy_data import EXTENDED_RESULTS
from utils.pagination import paginate

def render_leads_tab(session_state):
    st.subheader("\U0001F4CB Lead List")

    if session_state.leads:
        selected = st.multiselect(
            "Select companies to enrich or export:",
            options=[row["Company"] for row in session_state.leads],
            default=[]
        )

        paginated, start_index = paginate(session_state.leads, session_state.page, 10)
        df_paginated = pd.DataFrame(paginated)
        df_paginated.insert(0, "S.No", range(start_index + 1, start_index + 1 + len(df_paginated)))
        df_paginated = df_paginated.reset_index(drop=True)
        st.dataframe(df_paginated.set_index("S.No"), use_container_width=True)

        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            if session_state.page > 0:
                if st.button("⬅️ Previous"):
                    session_state.page -= 1
        with col2:
            if session_state.page < math.ceil(len(session_state.leads) / 10) - 1:
                if st.button("Next ➡️"):
                    session_state.page += 1

        if selected:
            df_export = pd.DataFrame([row for row in session_state.leads if row["Company"] in selected])
            csv = df_export.to_csv(index=False).encode('utf-8')
            st.download_button("⬇️ Export Selected as CSV", csv, "selected_leads.csv", "text/csv")

        if st.button("Scrape More Leads"):
            session_state.leads = EXTENDED_RESULTS
            session_state.page = 0
            st.success(f"Scraped {len(session_state.leads)} total leads.")
