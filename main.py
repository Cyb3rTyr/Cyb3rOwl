import sys
import subprocess
import os
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
    QTextEdit,
    QMessageBox,
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt, QProcess


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cyb3rOwl: Malware & Vulnerability Scanner")
        self.setMinimumSize(1200, 700)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(self.app_style())
        main_layout = QHBoxLayout()

        # Create a terminal-like border frame for the window content
        border_frame = QFrame(self)
        border_frame.setStyleSheet("border: 5px solid #1c1c1c; border-radius: 15px;")
        border_layout = QHBoxLayout(border_frame)

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
            "System Health": "⚙️ System Health: Update and optimize your system.",
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
            "Malware Scan": self.create_malware_scan_page(),
            "File Encryption": self.create_feature_page(
                "🔒 File Encryption", "Protect sensitive data with encryption."
            ),
            "Privacy Settings": self.create_feature_page(
                "🕵️‍♂️ Privacy Settings", "Enhance your privacy settings."
            ),
            "System Health": self.create_system_health_page(),
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

        # Add border_frame around the layout
        border_layout.addLayout(content_layout)
        border_frame.setLayout(border_layout)

        container = QWidget()
        container.setLayout(border_layout)
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
        return self.create_scrollable_page(layout)

    def create_malware_scan_page(self):
        layout = QVBoxLayout()
        layout.addWidget(self.create_title("🦠 Malware Scan"))
        layout.addWidget(
            self.create_description(
                "Run a comprehensive malware scan to detect and remove threats from your system.\n\n"
                "This feature will help ensure that your system remains secure from known and emerging malware."
            )
        )

        # Create the "Start Scan" button at the bottom-left of the Malware Scan page
        scan_btn = self.create_cta_button("Start Scan")
        scan_btn.setStyleSheet(
            "background-color: #36d2cf; color: white; padding: 10px; border-radius: 10px;"
        )
        scan_btn.setMinimumHeight(40)
        scan_btn.setMaximumWidth(120)
        scan_btn.clicked.connect(self.start_scan)

        # Add to layout with bottom alignment
        layout.addWidget(
            scan_btn,
            alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft,
        )

        return self.create_scrollable_page(layout)

    def create_system_health_page(self):
        layout = QVBoxLayout()
        layout.addWidget(self.create_title("⚙️ System Health"))
        layout.addWidget(
            self.create_description(
                "Keep your system in top condition by performing updates and optimizations.\n\n"
                "Click below to update your system using the Windows Package Manager (winget)."
            )
        )

        # Create the "Update" button at the bottom-left of the System Health page
        update_btn = self.create_cta_button("Update")
        update_btn.setStyleSheet(
            "background-color: #36d2cf; color: white; padding: 10px; border-radius: 10px;"
        )
        update_btn.setMinimumHeight(40)
        update_btn.setMaximumWidth(120)
        update_btn.clicked.connect(self.check_terms_and_update)

        # Create the "Upgrade" button near the Update button
        upgrade_btn = self.create_cta_button("Upgrade")
        upgrade_btn.setStyleSheet(
            "background-color: #36d2cf; color: white; padding: 10px; border-radius: 10px;"
        )
        upgrade_btn.setMinimumHeight(40)
        upgrade_btn.setMaximumWidth(120)
        upgrade_btn.clicked.connect(self.upgrade_system)

        # Add both buttons to layout with bottom-left alignment
        layout.addWidget(
            update_btn,
            alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft,
        )
        layout.addWidget(
            upgrade_btn,
            alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft,
        )

        # Add terminal-like output area
        self.terminal_output = QTextEdit()
        self.terminal_output.setReadOnly(True)  # Make the terminal output read-only
        layout.addWidget(self.terminal_output)

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

    def start_scan(self):
        # Add the scan logic here
        print("Scan started!")

    def check_terms_and_update(self):
        # Check if terms have been accepted before
        if not self.terms_accepted():
            self.show_terms_dialog()
        else:
            self.update_system()

    def show_terms_dialog(self):
        # Show a dialog box asking the user to accept the terms
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Accept Terms and Conditions")
        msg_box.setText(
            "By updating your system using winget, you agree to the terms and conditions."
        )
        msg_box.setStandardButtons(
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        )
        msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)

        # Connect the accepted signal
        if msg_box.exec() == QMessageBox.StandardButton.Ok:
            self.store_terms_acceptance()
            self.update_system()

    def store_terms_acceptance(self):
        # Store a file that indicates terms were accepted
        with open("terms_accepted.txt", "w") as f:
            f.write("Accepted")

    def terms_accepted(self):
        # Check if the terms acceptance file exists
        return os.path.exists("terms_accepted.txt")

    def update_system(self):
        self.terminal_output.append("Updating system using winget...\n")
        process = QProcess(self)
        process.start("winget", ["update"])
        process.readyReadStandardOutput.connect(self.handle_output)
        process.readyReadStandardError.connect(self.handle_error)

    def upgrade_system(self):
        self.terminal_output.append("Running upgrade script...\n")

        # Path to the upgrade script (ensure the path is correct)
        script_path = (
            "C:/path/to/your/upgrade_script.bat"  # Update with the correct path
        )

        # Start the process to run the batch script
        process = QProcess(self)

        # Ensure the script path is correct and escape spaces if needed
        process.start(f"cmd.exe /c {script_path}")

        # Connect the process to handle the output and error streams
        process.readyReadStandardOutput.connect(self.handle_output)
        process.readyReadStandardError.connect(self.handle_error)

    def handle_output(self):
        output = self.sender().readAllStandardOutput().data().decode()
        self.terminal_output.append(output)

    def handle_error(self):
        error = self.sender().readAllStandardError().data().decode()
        self.terminal_output.append(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
