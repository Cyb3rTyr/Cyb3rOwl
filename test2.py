import streamlit as st

# Set the page title and layout
st.set_page_config(
    page_title="CYB3R OWL: Malware & Vulnerability Scanner", layout="wide"
)

# ======================== 🌐 Cyberpunk / Futuristic Style ========================
st.markdown(
    """
    <style>
        /* Global Body Style */
        body {
            background-color: #0d0d0d;
            color: #00ffff;
            font-family: 'Consolas', 'Courier New', monospace;
        }
        /* Glowing Header */
        .header {
            font-size: 42px;
            font-weight: bold;
            color: #00ffff;
            text-shadow: 0 0 15px #00ffff, 0 0 30px #0088ff;
            text-align: center;
            margin-bottom: 20px;
        }
        /* Subheader */
        .subheader {
            font-size: 26px;
            color: #00ccff;
            text-align: center;
            margin-bottom: 15px;
        }
        /* Description */
        .description {
            font-size: 18px;
            color: #cccccc;
            text-align: center;
            margin-bottom: 30px;
        }
        /* Main Content */
        .main-content {
            text-align: center;
            margin: 30px auto;
            padding: 25px;
            background: rgba(0, 0, 0, 0.6);
            border: 2px solid #00ffff;
            border-radius: 15px;
            box-shadow: 0 0 20px #00ffff;
        }
        /* Sidebar */
        .sidebar {
            background-color: #111;
            color: #00ffff;
            padding-top: 30px;
            font-size: 18px;
            border-right: 2px solid #00ffff;
        }
        .sidebar button {
            background: linear-gradient(145deg, #004466, #002233);
            border: 1px solid #00ffff;
            color: #00ffff;
            padding: 15px;
            width: 100%;
            text-align: left;
            border-radius: 8px;
            margin-bottom: 15px;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        .sidebar button:hover {
            background: #00ffff;
            color: #000;
            box-shadow: 0 0 12px #00ffff;
        }
        /* Footer */
        .footer {
            text-align: center;
            font-size: 14px;
            color: #00ffff;
            margin-top: 30px;
            padding: 15px;
            background: rgba(0, 0, 0, 0.8);
            border-radius: 10px;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# ======================== Sidebar Image & Navigation ========================

# Sidebar image (use uploaded file)
st.sidebar.image("mnt/data/owl.png", use_container_width=True)

# Sidebar title
st.sidebar.markdown(
    '<h2 style="color: #00ffff; text-align: center;">CYB3R OWL</h2>',
    unsafe_allow_html=True,
)

# Navigation pages
section_title = "Navigation"
pages = [
    ("Home", "🏠", "home"),
    ("Malware Scan", "🦠", "malware_scan"),
    ("Vulnerability Scan", "🔍", "vulnerability_scan"),
    ("System Health Check", "🛡️", "system_health_check"),
]

st.sidebar.markdown(f"### {section_title}", unsafe_allow_html=True)
page_selection = "home"  # Default page

for page_name, icon, page_id in pages:
    if st.sidebar.button(f"{icon} {page_name}"):
        page_selection = page_id

# ======================== Page Content Based on Selection ========================

if page_selection == "home":
    st.markdown(
        '<div class="header">⚔️ CYB3R OWL: Malware & Vulnerability Scanner ⚔️</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="subheader">Next-Gen Cyber Defense at Your Fingertips</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="description">Welcome to CYB3R OWL. Scan, detect, and secure your system in real-time using this streamlined cybersecurity tool.</div>',
        unsafe_allow_html=True,
    )

    # Features
    st.markdown(
        '<div class="main-content"><h3>🛠️ Features</h3><ul>'
        "<li>💥 Malware Detection & Elimination</li>"
        "<li>🛡️ Vulnerability Assessment</li>"
        "<li>⚙️ System Health Monitoring</li>"
        "</ul></div>",
        unsafe_allow_html=True,
    )

    # Requirements
    st.markdown(
        '<div class="main-content"><h3>📦 Requirements</h3>'
        "<p>Python 3.7+ required. Install dependencies via setup script.</p></div>",
        unsafe_allow_html=True,
    )

    # Setup
    st.markdown(
        '<div class="main-content"><h3>🚀 Setup</h3>'
        "<pre>git clone https://github.com/your-username/CyberGuar.git\ncd CyberGuar\npython setup.py install\nstreamlit run app.py</pre></div>",
        unsafe_allow_html=True,
    )

    # License
    st.markdown(
        '<div class="main-content"><h3>📜 License</h3>'
        "<p>Distributed under MIT License. See LICENSE for details.</p></div>",
        unsafe_allow_html=True,
    )

    # Contact
    st.markdown(
        '<div class="main-content"><h3>📨 Contact</h3>'
        '<p>Find me on <a href="https://www.linkedin.com/in/rodrigo-marques-sa-9589772bb/" target="_blank" style="color:#00ffff;">LinkedIn</a></p></div>',
        unsafe_allow_html=True,
    )

    # GitHub
    st.markdown(
        '<div class="main-content"><h3>💻 GitHub</h3>'
        '<p>Contribute on <a href="https://github.com/Cyb3rTyr" target="_blank" style="color:#00ffff;">GitHub</a></p></div>',
        unsafe_allow_html=True,
    )

elif page_selection == "malware_scan":
    st.markdown(
        '<div class="main-content"><h3>🦠 Malware Scan</h3><p>Scanning for malware threats...</p></div>',
        unsafe_allow_html=True,
    )

elif page_selection == "vulnerability_scan":
    st.markdown(
        '<div class="main-content"><h3>🔍 Vulnerability Scan</h3><p>Checking system for vulnerabilities...</p></div>',
        unsafe_allow_html=True,
    )

elif page_selection == "system_health_check":
    st.markdown(
        '<div class="main-content"><h3>🛡️ System Health Check</h3><p>Analyzing system performance and health...</p></div>',
        unsafe_allow_html=True,
    )

# ======================== Footer ========================
st.markdown(
    """
    <div class="footer">⚔️ Made by Cyb3rTyr | Stay Secure, Stay Anonymous ⚔️</div>
    """,
    unsafe_allow_html=True,
)
