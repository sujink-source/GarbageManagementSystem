import streamlit as st
import pandas as pd
import datetime

# Initialize session state for storing reports
if 'reports' not in st.session_state:
    st.session_state.reports = []

# App Title
st.title("Garbage Management System")

# Sidebar Navigation
menu = st.sidebar.radio("Menu", ["Report Issue", "View Reports", "Track Collection"])

# Report Issue Section
if menu == "Report Issue":
    st.header("Report a Garbage Issue")
    location = st.text_input("Location")
    issue_description = st.text_area("Issue Description")
    urgency = st.selectbox("Urgency Level", ["Low", "Medium", "High"])
    report_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if st.button("Submit Report"):
        if location and issue_description:
            st.session_state.reports.append({
                "Location": location,
                "Description": issue_description,
                "Urgency": urgency,
                "Date Reported": report_date,
                "Status": "Pending"
            })
            st.success("Report submitted successfully!")
        else:
            st.error("Please fill all fields before submitting.")

# View Reports Section
elif menu == "View Reports":
    st.header("Reported Issues")
    if st.session_state.reports:
        df = pd.DataFrame(st.session_state.reports)
        st.dataframe(df)
    else:
        st.info("No reports available.")

# Track Collection Section
elif menu == "Track Collection":
    st.header("Track Garbage Collection Status")
    if st.session_state.reports:
        for i, report in enumerate(st.session_state.reports):
            st.subheader(f"Report {i+1}")
            st.text(f"Location: {report['Location']}")
            st.text(f"Issue: {report['Description']}")
            st.text(f"Urgency: {report['Urgency']}")
            st.text(f"Status: {report['Status']}")
            if st.button(f"Mark as Collected", key=i):
                st.session_state.reports[i]["Status"] = "Collected"
                st.experimental_rerun()
    else:
        st.info("No reports available to track.")
