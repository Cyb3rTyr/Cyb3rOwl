import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Malware & Vulnerability Scanner", layout="wide")

# Customizing the header and body style for a more hacker aesthetic
st.markdown(
    """
    <style>
        /* Global Body Style */
        body {
            background-color: #121212;
            color: #00FF00;
            font-family: 'Courier New', Courier, monospace;
        }
        /* Header Style */
        .header {
            font-size: 36px;
            font-weight: bold;
            color: #00FF00;
            text-align: center;
            margin-bottom: 10px;
        }
        /* Subheader Style */
        .subheader {
            font-size: 24px;
            font-weight: bold;
            color: #00FF00;
            text-align: center;
            margin-bottom: 5px;
        }
        /* Description Text Style */
        .description {
            font-size: 18px;
            color: #00FF00;
            text-align: center;
            margin-bottom: 20px;
        }
        /* Main Content Container Style */
        .main-content {
            text-align: center;
            margin-top: 20px;
            padding: 20px;
            background-color: #1A1A1A;
            border-radius: 10px;
        }
        /* Sidebar Styling for a Dark, Compact Look */
        .sidebar {
            background-color: #222;
            color: #00FF00;
            padding-top: 20px;
            font-size: 18px;
            font-family: 'Courier New', Courier, monospace;
        }
        .sidebar button {
            background-color: #333;
            border: 1px solid #00FF00;
            color: #00FF00;
            padding: 12px;
            width: 100%;
            text-align: left;
            border-radius: 5px;
            margin-bottom: 10px;
            font-size: 16px;
        }
        .sidebar button:hover {
            background-color: #444;
            color: #FFF;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #00FF00;
            background-color: #000000;
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

# ======================================== Sidebar Section with Sections and Pages ========================================

# Sidebar image (using your image path)
st.sidebar.image(
    r"assets\owl.png", use_container_width=True
)  # Updated to use_container_width

# Define Sections and Pages with icons
section_title = "Malware & Vulnerability Scanning"
pages = [
    ("Home", "📖", "home"),
    ("Malware Scan", "🦠", "malware_scan"),
    ("Vulnerability Scan", "🔍", "vulnerability_scan"),
    ("System Health Check", "🔧", "system_health_check"),
]

# Add section title in the sidebar
st.sidebar.markdown(f"### {section_title}", unsafe_allow_html=True)

# Set default page selection to "home"
page_selection = "home"  # Default to home page

# Display pages in the sidebar as clickable buttons
for page_name, icon, page_id in pages:
    if st.sidebar.button(f"{icon} {page_name}"):
        page_selection = page_id

# ======================================== Page Navigation Based on Sidebar Selection ========================================
if page_selection == "home":
    # Display intro text only on the home page
    st.markdown(
        '<div class="header">Welcome to the CyberGuar: Malware & Vulnerability Scanner</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="subheader">A Simple Cybersecurity Tool to Protect Your System</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="description">CyberGuar is a simple and interactive cybersecurity tool built with Streamlit. '
        "It helps scan your system for potential malware and vulnerabilities and provides basic system health checks.</div>",
        unsafe_allow_html=True,
    )

    # Features Section
    st.markdown("### Features", unsafe_allow_html=True)
    st.markdown(
        """
        - **Malware Scan**: Detects potential malware on your system.
        - **Vulnerability Scan**: Identifies known vulnerabilities in your system.
        - **System Health Check**: Evaluates the general health of your system and provides feedback.
        """,
        unsafe_allow_html=True,
    )

    # Requirements Section
    st.markdown("### Requirements", unsafe_allow_html=True)
    st.markdown(
        "To run this project, ensure you have Python 3.7 or higher installed.",
        unsafe_allow_html=True,
    )

    # Setup Instructions Section
    st.markdown("### Setup", unsafe_allow_html=True)
    st.markdown(
        """
        1. Clone the repository:
        ```bash
        git clone https://github.com/your-username/CyberGuar.git
        cd CyberGuar
        ```
        2. Run the setup script:
        ```bash
        python setup.py install
        ```
        3. Once the setup is complete, run the Streamlit app with:
        ```bash
        streamlit run app.py
        ```
        4. Open the browser to view the application (Streamlit will display the URL in the terminal).
        """,
        unsafe_allow_html=True,
    )

    # What will be installed Section
    st.markdown("### What will be installed", unsafe_allow_html=True)
    st.markdown(
        """
        The `setup.py` script will automatically install the following dependencies:
        - **Streamlit**: A library used for building the interactive web app interface.
        - **Other Dependencies**: Any other dependencies defined in `requirements.txt` (if additional libraries are required).
        """,
        unsafe_allow_html=True,
    )

    # License Section
    st.markdown("### License", unsafe_allow_html=True)
    st.markdown(
        "Distributed under the MIT License. See `LICENSE` for more information.",
        unsafe_allow_html=True,
    )

    # Contact Section
    st.markdown("### Contact", unsafe_allow_html=True)
    st.markdown(
        "For inquiries or feedback, please contact me on [LinkedIn](https://www.linkedin.com/in/rodrigo-marques-sa-9589772bb/).",
        unsafe_allow_html=True,
    )

    # GitHub Section (Added at the end)
    st.markdown("### GitHub", unsafe_allow_html=True)
    st.markdown(
        "Visit the project's source code and contribute on [GitHub](https://github.com/Cyb3rTyr).",
        unsafe_allow_html=True,
    )

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

# Footer Section with hacker-style font and color
st.markdown(
    """
    <style>
        .hacker-footer {
            font-family: 'Courier New', Courier, monospace;
            font-size: 16px;
            color: #00FF00;
            text-align: center;
            background-color: #000000;
            padding: 10px;
            border-radius: 5px;
            letter-spacing: 1px;
        }
    </style>
    <div class="hacker-footer">Made by Cyb3rTyr ⚔️ | Stay Secure, Stay Anonymous</div>
    """,
    unsafe_allow_html=True,
)
