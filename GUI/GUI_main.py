import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Malware & Vulnerability Scanner", layout="wide")

# Customizing the header style
st.markdown(
    """
    <style>
        .header {
            font-size: 36px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
        }
        .subheader {
            font-size: 24px;
            font-weight: bold;
            color: #555;
            text-align: center;
        }
        .description {
            font-size: 18px;
            color: #777;
            text-align: center;
        }
        .main-content {
            text-align: center;
            margin-top: 20px;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #aaa;
            padding-top: 20px;
        }
        /* Custom CSS to reduce space between sidebar buttons */
        .css-1lcbmhc {
            padding: 5px 0;  /* Reduce vertical padding */
        }
    </style>
""",
    unsafe_allow_html=True,
)

# ======================================== Header Section ========================================
st.markdown(
    '<div class="header">Welcome to the Malware & Vulnerability Scanner</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subheader">Scan your system for potential threats</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="description">This is a basic Streamlit app to help scan for malware and vulnerabilities.</div>',
    unsafe_allow_html=True,
)

# ======================================== Sidebar Section with Sections and Pages ========================================

# Define Sections and Pages with icons
section_title = "Malware & Vulnerability Scanning"
pages = [
    ("Home", "📖", "home"),
    ("Malware Scan", "🦠", "malware_scan"),
    ("Vulnerability Scan", "🔍", "vulnerability_scan"),
    ("System Health Check", "🔧", "system_health_check"),
]


# Add section title in the sidebar
st.sidebar.markdown(f"### {section_title}")

# Display pages in the sidebar as clickable buttons
page_selection = None
for page_name, icon, page_id in pages:
    if st.sidebar.button(f"{icon} {page_name}"):
        page_selection = page_id

# ======================================== Page Navigation Based on Sidebar Selection ========================================
if page_selection == "home":
    st.markdown(
        '<div class="main-content"><h3>Welcome to the Scanner App</h3></div>',
        unsafe_allow_html=True,
    )
    st.write("Choose an option from the sidebar to begin your scan.")

elif page_selection == "malware_scan":
    st.markdown(
        '<div class="main-content"><h3>Malware Scan</h3></div>', unsafe_allow_html=True
    )
    st.write("Performing malware scan... (this is a placeholder for now)")

elif page_selection == "vulnerability_scan":
    st.markdown(
        '<div class="main-content"><h3>Vulnerability Scan</h3></div>',
        unsafe_allow_html=True,
    )
    st.write("Performing vulnerability scan... (this is a placeholder for now)")

elif page_selection == "system_health_check":
    st.markdown(
        '<div class="main-content"><h3>System Health Check</h3></div>',
        unsafe_allow_html=True,
    )
    st.write("Performing system health check... (this is a placeholder for now)")

# Footer Section
st.markdown(
    '<div class="footer">Built with ❤️ using Streamlit</div>', unsafe_allow_html=True
)
