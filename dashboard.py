import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Create tabs
tab1, tab2 = st.tabs(["💼 Corporate Task Reporting", "🍽️ Restaurant KPIs"])

# --------------------------
# Tab 1 (already exists) – Keep your corporate dashboard code here
with tab1:
    st.header("Corporate Task Reporting Dashboard")
    # Your original corporate dashboard logic goes here...

# --------------------------
# Tab 2 – Restaurant KPI Dashboard
with tab2:
    st.header("Restaurant KPI Dashboard")

    # Mock restaurant data
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

    # RYG status logic
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
                    return '🔴'
            else:
                if val > tgt * 1.1:
                    return '🔴'
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

    # Display
    st.dataframe(restaurant_scorecard_df, use_container_width=True)
