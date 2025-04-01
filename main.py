import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QStackedWidget,
    QScrollArea,
    QFrame,
    QSizePolicy,
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cyb3rOwl: Malware & Vulnerability Scanner")
        self.setMinimumSize(1200, 700)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(self.app_style())
        main_layout = QHBoxLayout()

        # Sidebar
        self.sidebar = QWidget()
        self.sidebar_layout = QVBoxLayout()
        self.sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.sidebar.setFixedWidth(270)

        # Logo
        logo_image = QLabel()
        logo_pixmap = QPixmap("cyb3r.png").scaled(
            140,
            140,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        logo_image.setPixmap(logo_pixmap)
        logo_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sidebar_layout.addWidget(logo_image)

        # Navigation Buttons
        self.buttons = {}
        pages = {
            "Home": "🏠 Home: Your dashboard for system security and optimization.",
            "Malware Protection": "🦠 Malware Protection: Detect and remove malware in real-time.",
            "System Cleanup": "🧹 System Cleanup: Free up space and improve system performance.",
            "Malware Scan": "🦠 Malware Scan: Run comprehensive malware scans.",
            "File Encryption": "🔒 File Encryption: Protect sensitive data with encryption.",
            "Privacy Settings": "🕵️‍♂️ Privacy Settings: Enhance your privacy settings.",
        }

        for page, description in pages.items():
            btn = self.create_sidebar_button(page)
            self.sidebar_layout.addWidget(btn)
            self.buttons[page] = btn

        self.sidebar_layout.addStretch()
        self.sidebar.setLayout(self.sidebar_layout)

        # Main Content
        self.stack = QStackedWidget()
        self.pages = {
            "Home": self.create_home_page(),
            "Malware Protection": self.create_feature_page(
                "🦠 Malware Protection", "Detect and remove malware in real-time."
            ),
            "System Cleanup": self.create_feature_page(
                "🧹 System Cleanup", "Free up space and improve system performance."
            ),
            "Malware Scan": self.create_feature_page(
                "🦠 Malware Scan", "Run comprehensive malware scans."
            ),
            "File Encryption": self.create_feature_page(
                "🔒 File Encryption", "Protect sensitive data with encryption."
            ),
            "Privacy Settings": self.create_feature_page(
                "🕵️‍♂️ Privacy Settings", "Enhance your privacy settings."
            ),
        }
        for page in self.pages.values():
            self.stack.addWidget(page)

        content_layout = QHBoxLayout()
        content_layout.addWidget(self.sidebar)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet("background-color: #2a637a;")
        separator.setFixedWidth(2)
        content_layout.addWidget(separator)

        content_layout.addWidget(self.stack, 4)
        container = QWidget()
        container.setLayout(content_layout)
        self.setCentralWidget(container)
        self.navigate("Home")

    def create_sidebar_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet(self.button_style())
        btn.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        btn.setMinimumHeight(40)
        btn.clicked.connect(lambda: self.navigate(text))
        return btn

    def create_home_page(self):
        layout = QVBoxLayout()
        layout.addWidget(
            self.create_title("Welcome to Cyb3rOwl - Your Ultimate Security Companion")
        )
        layout.addWidget(
            self.create_description(
                "🚀 Protect. Optimize. Recover.\n\n"
                "Cyb3rOwl is your all-in-one security toolkit designed to keep your device safe, optimized, and secure. "
                "Whether you're protecting your system from malware, managing files, or ensuring privacy, Cyb3rOwl has you covered.\n\n"
                "Key Features:\n"
                "🦠 Malware Protection - Detect and remove malware in real-time.\n"
                "🧹 System Cleanup - Free up space and improve performance.\n"
                "🦠 Malware Scan - Run comprehensive malware scans.\n"
                "🔒 File Encryption - Protect sensitive data.\n"
                "🕵️‍♂️ Privacy Settings - Clean browser history and manage privacy.\n\n"
                "🌟 Get Started:\n"
                "Run a Quick Malware Scan to check for potential threats.\n"
                "Clean up Junk Files to optimize system performance.\n"
                "Encrypt Files to protect sensitive data.\n"
                "Manage Privacy Settings to enhance your online privacy.\n\n"
                "⚙️ Settings:\n"
                "Personalize Cyb3rOwl with automatic scans, privacy controls, and encryption preferences.\n\n"
                "🔐 Your Security, Our Priority\n"
                "Cyb3rOwl combines simplicity with advanced technology to ensure your device stays secure at all times."
            )
        )
        layout.addWidget(self.create_cta_button("Start Scan"))
        return self.create_scrollable_page(layout)

    def create_feature_page(self, title_text, description_text):
        layout = QVBoxLayout()
        layout.addWidget(self.create_title(title_text))
        layout.addWidget(self.create_description(description_text))
        return self.create_scrollable_page(layout)

    def create_scrollable_page(self, layout):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_widget.setLayout(layout)
        scroll_area.setWidget(scroll_widget)
        return scroll_area

    def create_title(self, text):
        title = QLabel(text)
        title.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        return title

    def create_description(self, text):
        desc = QLabel(text)
        desc.setFont(QFont("Segoe UI", 14))
        desc.setWordWrap(True)
        desc.setAlignment(Qt.AlignmentFlag.AlignLeft)
        return desc

    def create_cta_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet(
            "background-color: #36d2cf; color: white; padding: 15px; border-radius: 10px;"
        )
        btn.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        btn.setMinimumHeight(50)
        return btn

    def button_style(self):
        return "background-color: #0f2334; color: white; padding: 12px; border-radius: 15px;"

    def selected_button_style(self):
        return "background-color: #2a637a; color: #36d2cf; padding: 12px; border-radius: 15px;"

    def app_style(self):
        return (
            "* { background-color: #0f2334; color: #c5e2df; font-family: 'Segoe UI'; }"
        )

    def navigate(self, page_name):
        self.stack.setCurrentWidget(self.pages[page_name])
        for btn_name, btn in self.buttons.items():
            btn.setStyleSheet(
                self.selected_button_style()
                if btn_name == page_name
                else self.button_style()
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
