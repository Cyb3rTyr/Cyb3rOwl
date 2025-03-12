import streamlit as st

# ========================== Page Config ==========================
st.set_page_config(
    page_title="CyberGuar: Malware & Vulnerability Scanner", layout="wide"
)


# ========================== Custom CSS ==========================
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

        /* ====== Global Style ====== */
        body {
            background-color: #0D0D14;
            color: #E6E6E6;
            font-family: 'Inter', sans-serif;
        }

        /* ====== Headers ====== */
        .header {
            font-size: 42px;
            font-weight: 700;
            color: #38E8FF;
            text-align: center;
            margin-bottom: 20px;
        }
        .subheader {
            font-size: 26px;
            font-weight: 600;
            color: #8FFF8A;
            text-align: center;
            margin-bottom: 15px;
        }
        .description {
            font-size: 18px;
            font-weight: 400;
            color: #E6E6E6;
            text-align: center;
            margin-bottom: 30px;
        }

        /* ====== Main Content Card ====== */
        .main-content {
            text-align: center;
            margin: 20px auto;
            padding: 30px;
            background: #1E2835;
            border-radius: 16px;
            border: 2px solid #38E8FF;
            box-shadow: 0 0 15px rgba(56, 232, 255, 0.4);
            width: 90%;
        }

        /* ====== Sidebar ====== */
        .css-1d391kg, .css-1lcbmhc {  
            background-color: #1E2835;
            color: #E6E6E6;
            padding-top: 30px;
            font-family: 'Inter', sans-serif;
        }

        /* ====== Sidebar Buttons ====== */
        .stButton button {
            background: linear-gradient(145deg, #1E2835, #2A394D);
            color: #E6E6E6;
            border: 2px solid #38E8FF;
            border-radius: 12px;
            padding: 12px 20px;
            width: 100%;
            font-size: 16px;
            margin-bottom: 12px;
            transition: all 0.3s ease;
            box-shadow: 0 0 10px rgba(56, 232, 255, 0.3);
            font-family: 'Inter', sans-serif;
        }

        .stButton button:hover {
            background: #2A394D;
            color: #38E8FF;
            box-shadow: 0 0 15px rgba(56, 232, 255, 0.8);
        }

        /* ====== Footer ====== */
        .hacker-footer {
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            color: #8FFF8A;
            text-align: center;
            padding: 15px;
            margin-top: 20px;
            background: rgba(14, 14, 20, 0.8);
            border-radius: 8px;
        }

        /* ====== Scrollbar ====== */
        ::-webkit-scrollbar { width: 10px; }
        ::-webkit-scrollbar-track { background: #1E2835; }
        ::-webkit-scrollbar-thumb { background: #38E8FF; border-radius: 5px; }

    </style>
    """,
    unsafe_allow_html=True,
)

# ========================== Sidebar Navigation ==========================
st.sidebar.image("assets/owl.png", use_container_width=True)

st.sidebar.markdown("## Malware & Vulnerability Scanning")

pages = {
    "Home": "home",
    "Malware Scan": "malware_scan",
    "Vulnerability Scan": "vulnerability_scan",
    "System Health Check": "system_health_check",
}

# Sidebar buttons
page_selection = "home"
for name, page_id in pages.items():
    if st.sidebar.button(name):
        page_selection = page_id


# ========================== Page Routing ==========================
def home():
    st.markdown(
        '<div class="header">CyberGuar: Malware & Vulnerability Scanner</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="subheader">Your Shield Against Malware & Vulnerabilities</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="description">Scan, Detect, and Protect — all in one place.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.markdown("### 🚀 **Features**")
    st.markdown(
        """
        - 🛡️ **Malware Scan**: Detect potential threats in real-time.
        - 🔎 **Vulnerability Scan**: Identify system weaknesses.
        - 💻 **System Health Check**: Evaluate system performance and health.
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### ⚙️ **Setup**")
    st.markdown(
        """
        ```bash
        git clone https://github.com/your-username/CyberGuar.git
        cd CyberGuar
        python setup.py install
        streamlit run app.py
        ```
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📦 **Dependencies Installed**")
    st.markdown(
        """
        - `streamlit`
        - Other security libraries defined in `requirements.txt`.
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📜 **License**")
    st.markdown("Distributed under the MIT License. See `LICENSE` for more info.")

    st.markdown("### 📬 **Contact**")
    st.markdown(
        "[LinkedIn](https://www.linkedin.com/in/rodrigo-marques-sa-9589772bb/) | [GitHub](https://github.com/Cyb3rTyr)",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)


def malware_scan():
    st.markdown(
        '<div class="main-content"><h3>🦠 Malware Scan</h3></div>',
        unsafe_allow_html=True,
    )
    st.write("Performing malware scan... (Feature coming soon!)")


def vulnerability_scan():
    st.markdown(
        '<div class="main-content"><h3>🔍 Vulnerability Scan</h3></div>',
        unsafe_allow_html=True,
    )
    st.write("Performing vulnerability scan... (Feature coming soon!)")


def system_health_check():
    st.markdown(
        '<div class="main-content"><h3>� System Health Check</h3></div>',
        unsafe_allow_html=True,
    )
    st.write("Checking system health... (Feature coming soon!)")


# ========================== Page Handling ==========================
if page_selection == "home":
    home()
elif page_selection == "malware_scan":
    malware_scan()
elif page_selection == "vulnerability_scan":
    vulnerability_scan()
elif page_selection == "system_health_check":
    system_health_check()


# ========================== Footer ==========================
st.markdown(
    '<div class="hacker-footer">Made by Cyb3rTyr ⚔️ | Stay Secure, Stay Anonymous</div>',
    unsafe_allow_html=True,
)
