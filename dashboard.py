import streamlit as st
import pandas as pd

# Set page layout
st.set_page_config(layout="wide")
st.title("📊 Task Reporting Dashboard")

# Sample KPI data
kpi_data = {
    "Avg Task Completion Time": {"value": "3.8m", "change": "+1.2m", "color": "🔴"},
    "On-Time Task Completion %": {"value": "82.4%", "change": "", "color": "🟡"},
    "Overdue Tasks": {"value": "142", "change": "+12%", "color": "🟢"},
    "Compliance Audits Passed": {"value": "91.3%", "change": "+5.4%", "color": "🟢"}
}

# Display KPI cards in 4 columns
kpi_cols = st.columns(4)
for idx, (kpi, data) in enumerate(kpi_data.items()):
    with kpi_cols[idx]:
        st.metric(label=kpi, value=f"{data['value']}", delta=data['change'])

# Sample Scorecard Data
scorecard_df = pd.DataFrame({
    "KPI": [
        "Avg Completion Time",
        "Tasks Completed This Month",
        "Audits Passed",
        "Tasks Overdue",
        "Locations Above 90% Execution"
    ],
    "Actual": [
        "3.8m",
        "12,580",
        "91.3%",
        "142",
        "58%"
    ],
    "Target": [
        "2.5m",
        "15,000",
        "90%",
        "100",
        "75%"
    ],
    "Status": [
        "🔴",
        "🟢",
        "🟢",
        "🔴",
        "🔴"
    ]
})

st.subheader("📋 KPI Scorecard")
st.dataframe(scorecard_df, use_container_width=True)

# Additional Metrics Section
st.subheader("📈 Health Gauges")
col1, col2 = st.columns(2)
with col1:
    st.metric("Last Week’s Task Completion %", "76%")
with col2:
    st.metric("Training Completion by Deadline", "84%")
