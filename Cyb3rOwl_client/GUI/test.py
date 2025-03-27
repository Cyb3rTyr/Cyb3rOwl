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
    QFrame,
    QCheckBox,
    QScrollArea,
    QSizePolicy,
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cyb3rOwl: Malware & Vulnerability Scanner")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet(self.app_style())  # Set background style here

        # Main Layout
        main_layout = QHBoxLayout()

        # Sidebar
        sidebar = QVBoxLayout()
        sidebar.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Sidebar Image (Icon at the top)
        sidebar_image = QLabel()
        sidebar_image.setPixmap(
            QPixmap("assets/Cyb3rOwl_icon.ico").scaled(
                60, 60, Qt.AspectRatioMode.KeepAspectRatio
            )
        )
        sidebar_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sidebar.addWidget(sidebar_image)

        # Sidebar Buttons with icons
        self.buttons = {
            "Home": QPushButton("Home"),
            "Malware Scan": QPushButton("Malware Scan"),
            "Vulnerability Scan": QPushButton("Vulnerability Scan"),
            "System Health Check": QPushButton("System Health Check"),
            "Privacy Settings": QPushButton("Privacy Settings"),
        }

        self.icons = {
            "Home": QIcon("icons/home_icon.png"),
            "Malware Scan": QIcon("icons/malware_icon.png"),
            "Vulnerability Scan": QIcon("icons/vulnerability_icon.png"),
            "System Health Check": QIcon("icons/health_icon.png"),
            "Privacy Settings": QIcon("icons/privacy_icon.png"),
        }

        for btn_name, btn in self.buttons.items():
            btn.setIcon(self.icons.get(btn_name, QIcon()))
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setIconSize(QSize(30, 30))
            btn.setStyleSheet(self.button_style())
            sidebar.addWidget(btn)

        # Sidebar frame for clean separation
        sidebar_frame = QFrame()
        sidebar_frame.setFrameShape(QFrame.Shape.StyledPanel)
        sidebar_frame.setLayout(sidebar)

        # Main content area
        self.stack = QStackedWidget()

        # Pages
        self.pages = {
            "Home": self.create_home_page(),
            "Malware Scan": self.create_coming_soon_page("🦠 Malware Scan"),
            "Vulnerability Scan": self.create_coming_soon_page("🔍 Vulnerability Scan"),
            "System Health Check": self.create_system_health_page(),
            "Privacy Settings": self.create_privacy_page(),
        }

        for page in self.pages.values():
            self.stack.addWidget(page)

        # Connect buttons to pages
        for name, btn in self.buttons.items():
            btn.clicked.connect(lambda _, n=name: self.navigate(n))

        # Combine sidebar and main content
        main_layout.addWidget(sidebar_frame, 1)
        main_layout.addWidget(self.stack, 4)

        # Set central widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Default page
        self.navigate("Home")

    def navigate(self, page_name):
        # Update button style on selection
        for btn_name, btn in self.buttons.items():
            if btn_name == page_name:
                btn.setStyleSheet(self.selected_button_style())
            else:
                btn.setStyleSheet(self.button_style())

        index = list(self.pages.keys()).index(page_name)
        self.stack.setCurrentIndex(index)

    def create_home_page(self):
        layout = QVBoxLayout()

        title = QLabel("Cyb3rOwl: Malware & Vulnerability Scanner")
        title.setObjectName("header")
        subtitle = QLabel("Your Shield Against Malware & Vulnerabilities")
        subtitle.setObjectName("subheader")
        description = QLabel("Scan, Detect, and Protect — all in one place.")
        description.setObjectName("description")

        # Add owl image
        owl_image = QLabel()
        owl_image.setPixmap(
            QPixmap("assets/owl.png").scaled(
                300, 300, Qt.AspectRatioMode.KeepAspectRatio
            )
        )
        owl_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        features = QLabel(
            """
            🚀 <b>Features</b><br><br>
            🛡️ Malware Scan: Detect potential threats in real-time.<br>
            🔎 Vulnerability Scan: Identify system weaknesses.<br>
            💻 System Health Check: Evaluate system performance and health.<br><br>

            ⚙️ <b>Setup</b><br>
            <code>git clone https://github.com/your-username/Cyb3rOwl.git</code><br>
            <code>cd Cyb3rOwl</code><br>
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
        layout.addWidget(owl_image)
        layout.addWidget(subtitle, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(description, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(features)

        # Add a scroll area for the page
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )  # Disable horizontal scrollbar
        scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )  # Vertical scrollbar when necessary

        scroll_widget = QWidget()
        scroll_widget.setLayout(layout)
        scroll_area.setWidget(scroll_widget)

        container = QWidget()
        container.setLayout(QVBoxLayout())
        container.layout().addWidget(scroll_area)
        return container

    def create_system_health_page(self):
        layout = QVBoxLayout()

        title = QLabel("💻 System Health Check")
        title.setObjectName("header")

        health_status = QLabel("System Health: Good")
        health_status.setObjectName("subheader")

        layout.addWidget(title)
        layout.addWidget(health_status)

        # Add scroll area for this page as well
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )  # Disable horizontal scrollbar
        scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )  # Vertical scrollbar when necessary

        scroll_widget = QWidget()
        scroll_widget.setLayout(layout)
        scroll_area.setWidget(scroll_widget)

        container = QWidget()
        container.setLayout(QVBoxLayout())
        container.layout().addWidget(scroll_area)
        return container

    def create_privacy_page(self):
        layout = QVBoxLayout()

        title = QLabel("🔒 Privacy Settings")
        title.setObjectName("header")

        encryption_checkbox = QCheckBox("Enable Data Encryption")
        encryption_checkbox.setChecked(True)

        layout.addWidget(title)
        layout.addWidget(encryption_checkbox)

        # Add scroll area for this page as well
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )  # Disable horizontal scrollbar
        scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )  # Vertical scrollbar when necessary

        scroll_widget = QWidget()
        scroll_widget.setLayout(layout)
        scroll_area.setWidget(scroll_widget)

        container = QWidget()
        container.setLayout(QVBoxLayout())
        container.layout().addWidget(scroll_area)
        return container

    def create_coming_soon_page(self, title_text):
        layout = QVBoxLayout()
        title = QLabel(title_text)
        title.setObjectName("header")
        info = QLabel("Feature coming soon!")
        info.setObjectName("description")
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(info, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add scroll area for this page as well
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )  # Disable horizontal scrollbar
        scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )  # Vertical scrollbar when necessary

        scroll_widget = QWidget()
        scroll_widget.setLayout(layout)
        scroll_area.setWidget(scroll_widget)

        container = QWidget()
        container.setLayout(QVBoxLayout())
        container.layout().addWidget(scroll_area)
        return container

    def button_style(self):
        return """
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 12px 20px;
            margin: 10px;
            border: none;
            border-radius: 20px;
            text-align: left;
        """

    def selected_button_style(self):
        return """
            background-color: #2A394D;
            color: #38E8FF;
            font-size: 16px;
            padding: 12px 20px;
            margin: 10px;
            border: none;
            border-radius: 20px;
            text-align: left;
        """

    def app_style(self):
        return """
            * {
                background-color: #20232A;  /* Set the desired dark background color */
                color: #FFFFFF;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            QWidget {
                background-color: #20232A; /* Set the desired dark background color */
            }
            QPushButton, QCheckBox {
                background: transparent;
                color: #FFFFFF;
                font-size: 16px;
                padding: 12px;
                margin: 10px;
                border: none;
                border-radius: 20px;
            }
            QPushButton:hover, QCheckBox:hover {
                background-color: #A5D6A7;
                color: #4CAF50;
                box-shadow: 0 0 10px rgba(76, 175, 80, 0.8);
            }
            #header {
                font-size: 36px;
                font-weight: bold;
                color: #4CAF50;
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
