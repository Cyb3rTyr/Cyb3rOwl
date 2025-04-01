# home_page.py

from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QScrollArea, QWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


def create_home_page():
    # Create the layout for the Home page
    layout = QVBoxLayout()

    layout.addWidget(
        create_title("Welcome to Cyb3rOwl - Your Ultimate Security Companion")
    )
    layout.addWidget(
        create_description(
            "🚀 Protect. Optimize. Recover.\n\n"
            "Cyb3rOwl is your all-in-one security toolkit designed to keep your device safe, optimized, and secure. "
            "Whether you're protecting your system from malware, managing files, or ensuring privacy, Cyb3rOwl has you covered.\n\n"
            "Key Features:\n"
            "🦠 Malware Protection: Detect and remove malware in real-time.\n"
            "🧹 System Cleanup: Free up space and improve system performance.\n"
            "🦠 Malware Scan: Run comprehensive malware scans.\n"
            "🔒 File Encryption: Protect sensitive data with encryption.\n"
            "🕵️‍♂️ Privacy Settings: Enhance your privacy settings.\n\n"
            "Your Security Dashboard:\n"
            "• Real-time malware scan progress.\n"
            "• System performance and optimization stats.\n"
            "• Quick access to all security tools.\n\n"
            "🌟 Get Started:\n"
            "• Run a Quick Malware Scan to check for potential threats.\n"
            "• Clean up Junk Files to optimize system performance.\n"
            "• Encrypt Files to protect sensitive data.\n"
            "• Manage Privacy Settings.\n\n"
            "⚙️ Settings:\n"
            "• Automatic Scan Scheduling.\n"
            "• Privacy Controls.\n"
            "• Encryption Preferences.\n\n"
            "🔐 Your Security, Our Priority."
        )
    )
    layout.addWidget(create_cta_button("Start Scan"))

    # Make the layout scrollable
    return create_scrollable_page(layout)


def create_title(text):
    title = QLabel(text)
    title.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
    title.setAlignment(Qt.AlignmentFlag.AlignLeft)
    return title


def create_description(text):
    desc = QLabel(text)
    desc.setFont(QFont("Segoe UI", 14))
    desc.setWordWrap(True)
    desc.setAlignment(Qt.AlignmentFlag.AlignLeft)
    return desc


def create_cta_button(text):
    btn = QPushButton(text)
    btn.setStyleSheet(
        "background-color: #36d2cf; color: white; padding: 15px; border-radius: 10px;"
    )
    btn.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
    btn.setMinimumHeight(50)
    return btn


def create_scrollable_page(layout):
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_widget = QWidget()
    scroll_widget.setLayout(layout)
    scroll_area.setWidget(scroll_widget)
    return scroll_area
