import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QStackedWidget,
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CyberGuar: Malware & Vulnerability Scanner")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet(self.app_style())

        # Main Layout
        main_layout = QHBoxLayout()

        # Sidebar
        sidebar = QVBoxLayout()
        sidebar.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Sidebar Buttons
        self.buttons = {
            "Home": QPushButton("Home"),
            "Malware Scan": QPushButton("Malware Scan"),
            "Vulnerability Scan": QPushButton("Vulnerability Scan"),
            "System Health Check": QPushButton("System Health Check"),
        }

        for btn in self.buttons.values():
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            sidebar.addWidget(btn)

        # Main content area
        self.stack = QStackedWidget()

        # Pages
        self.pages = {
            "Home": self.create_home_page(),
            "Malware Scan": self.create_coming_soon_page("🦠 Malware Scan"),
            "Vulnerability Scan": self.create_coming_soon_page("🔍 Vulnerability Scan"),
            "System Health Check": self.create_coming_soon_page(
                "💻 System Health Check"
            ),
        }

        for page in self.pages.values():
            self.stack.addWidget(page)

        # Connect buttons to pages
        for name, btn in self.buttons.items():
            btn.clicked.connect(lambda _, n=name: self.navigate(n))

        # Combine sidebar and main content
        main_layout.addLayout(sidebar, 1)
        main_layout.addWidget(self.stack, 4)

        # Set central widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Default page
        self.navigate("Home")

    def navigate(self, page_name):
        index = list(self.pages.keys()).index(page_name)
        self.stack.setCurrentIndex(index)

    def create_home_page(self):
        layout = QVBoxLayout()

        title = QLabel("CyberGuar: Malware & Vulnerability Scanner")
        title.setObjectName("header")
        subtitle = QLabel("Your Shield Against Malware & Vulnerabilities")
        subtitle.setObjectName("subheader")
        description = QLabel("Scan, Detect, and Protect — all in one place.")
        description.setObjectName("description")

        features = QLabel(
            """
            🚀 <b>Features</b><br><br>
            🛡️ Malware Scan: Detect potential threats in real-time.<br>
            🔎 Vulnerability Scan: Identify system weaknesses.<br>
            💻 System Health Check: Evaluate system performance and health.<br><br>

            ⚙️ <b>Setup</b><br>
            <code>git clone https://github.com/your-username/CyberGuar.git</code><br>
            <code>cd CyberGuar</code><br>
            <code>python setup.py install</code><br>
            <code>streamlit run app.py</code><br><br>

            📦 <b>Dependencies</b><br>
            - streamlit<br>
            - Other security libraries in requirements.txt<br><br>

            📜 <b>License</b>: MIT License<br><br>

            📬 <b>Contact</b>: 
            <a href="https://www.linkedin.com/in/rodrigo-marques-sa-9589772bb/">LinkedIn</a> | 
            <a href="https://github.com/Cyb3rTyr">GitHub</a>
            """
        )
        features.setOpenExternalLinks(True)
        features.setObjectName("content")

        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(description, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(features)

        container = QWidget()
        container.setLayout(layout)
        return container

    def create_coming_soon_page(self, title_text):
        layout = QVBoxLayout()
        title = QLabel(title_text)
        title.setObjectName("header")
        info = QLabel("Feature coming soon!")
        info.setObjectName("description")
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(info, alignment=Qt.AlignmentFlag.AlignCenter)

        container = QWidget()
        container.setLayout(layout)
        return container

    def app_style(self):
        return """
            * {
                background-color: #0D0D14;
                color: #E6E6E6;
                font-family: Inter, sans-serif;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1E2835, stop:1 #2A394D);
                color: #E6E6E6;
                border: 2px solid #38E8FF;
                border-radius: 12px;
                padding: 12px 20px;
                margin: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background: #2A394D;
                color: #38E8FF;
                box-shadow: 0 0 15px rgba(56, 232, 255, 0.8);
            }
            #header {
                font-size: 36px;
                font-weight: bold;
                color: #38E8FF;
                margin: 20px;
            }
            #subheader {
                font-size: 24px;
                color: #8FFF8A;
                margin: 10px;
            }
            #description {
                font-size: 18px;
                margin: 15px;
            }
            #content {
                font-size: 16px;
                margin: 20px;
            }
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
