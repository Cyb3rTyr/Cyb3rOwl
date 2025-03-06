# sidebar.py
import streamlit as st


def display_sidebar():
    st.sidebar.title("Scan Options")
    scan_type = st.sidebar.selectbox(
        "Choose Scan Type",  # Dropdown label
        (
            "Malware Scan",
            "Vulnerability Scan",
            "System Health Check",
        ),  # Dropdown options
    )
    return scan_type  # Return the selected scan type
