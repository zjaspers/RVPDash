import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📊 Store Performance Powered by PowerBI")

# WorkJam Task Link
task_link = "https://app-next.workjamdemo.com/tasks/calendar?name=&progressStatuses=NOT_STARTED&progressStatuses=IN_PROGRESS&progressStatuses=READY_TO_COMPLETE&progressStatuses=IN_REVIEW&progressStatuses=REDO&projectId=&sort=availability&startKey=&base=2025-06-13&offset=0&moreFilters=false&projectDescription=&onlyOverdue=false"

# --------------------------
# TAB SETUP
tab1, tab2 = st.tabs(["WorkJam Action Report", "Location KPIs"])

# --------------------------
# TAB 1 – Corporate Task Reporting
with tab1:
    st.subheader("Corporate Task Reporting")

    # Sample KPI data
    kpi_data = {
        "Avg Task Completion Time": {"value": "3.8m", "change": "+1.2m", "status": "🔴"},
        "On-Time Task Completion %": {"value": "82.4%", "change": "", "status": "🟡"},
        "Overdue Tasks": {"value": "142", "change": "+12%", "status": "🟢"},
        "Compliance Audits Passed": {"value": "91.3%", "change": "+5.4%", "status": "🟢"}
    }

    # Display KPI cards
    kpi_cols = st.columns(4)
    for idx, (kpi, data) in enumerate(kpi_data.items()):
        with kpi_cols[idx]:
            st.metric(label=kpi, value=data["value"], delta=data["change"])

    # Scorecard DataFrame
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

    def render_scorecard(df):
        html = "<table><tr>"
        for col in df.columns:
            html += f"<th style='padding:8px; text-align:left'>{col}</th>"
        html += "</tr>"

        for _, row in df.iterrows():
            html += "<tr>"
            for col in df.columns:
                val = row[col]
                if col == "Status" and "🔴" in val:
                    val = f"<a href='{task_link}' target='_blank'>🔴</a>"
                html += f"<td style='padding:8px'>{val}</td>"
            html += "</tr>"
        html += "</table>"

        st.markdown(html, unsafe_allow_html=True)

    st.subheader("📋 KPI Scorecard")
    render_scorecard(scorecard_df)

    # Additional Metrics
    st.subheader("📈 Health Gauges")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Last Week’s Task Completion %", "76%")
    with col2:
        st.metric("Training Completion by Deadline", "84%")

# --------------------------
# TAB 2 – Restaurant KPIs
with tab2:
    st.subheader("Restaurant KPI Dashboard")

    restaurant_scorecard_df = pd.DataFrame({
        "Location": [
            "Easton Town Center", "Polaris Fashion Place", "Short North",
            "Kenwood Towne Centre", "Dayton Mall", "Liberty Center"
        ],
        "Food Waste %": ["2.9%", "4.2%", "3.1%", "5.5%", "3.0%", "3.7%"],
        "Target Waste %": ["3.0%"] * 6,
        "Labor Cost %": ["28%", "32%", "29%", "35%", "27%", "31%"],
        "Target Labor %": ["30%"] * 6,
        "WorkJam Task Completion %": ["97%", "88%", "94%", "75%", "99%", "91%"],
        "Task Target %": ["95%"] * 6
    })

    def status_color(value, target, reverse=False):
        try:
            val = float(value.strip('%'))
            tgt = float(target.strip('%'))
            if reverse:
                if val < tgt * 0.9:
                    return '🟢'
                elif val <= tgt:
                    return '🟡'
                else:
                    return f"<a href='{task_link}' target='_blank'>🔴</a>"
            else:
                if val > tgt * 1.1:
                    return f"<a href='{task_link}' target='_blank'>🔴</a>"
                elif val > tgt:
                    return '🟡'
                else:
                    return '🟢'
        except:
            return ''

    restaurant_scorecard_df["Food Waste Status"] = restaurant_scorecard_df.apply(
        lambda row: status_color(row["Food Waste %"], row["Target Waste %"]), axis=1
    )
    restaurant_scorecard_df["Labor Cost Status"] = restaurant_scorecard_df.apply(
        lambda row: status_color(row["Labor Cost %"], row["Target Labor %"]), axis=1
    )
    restaurant_scorecard_df["Task Completion Status"] = restaurant_scorecard_df.apply(
        lambda row: status_color(row["WorkJam Task Completion %"], row["Task Target %"], reverse=True), axis=1
    )

    def render_restaurant_table(df):
        html = "<table><tr>"
        for col in df.columns:
            html += f"<th style='padding:8px; text-align:left'>{col}</th>"
        html += "</tr>"

        for _, row in df.iterrows():
            html += "<tr>"
            for col in df.columns:
                val = row[col]
                html += f"<td style='padding:8px'>{val}</td>"
            html += "</tr>"
        html += "</table>"

        st.markdown(html, unsafe_allow_html=True)

    render_restaurant_table(restaurant_scorecard_df)
