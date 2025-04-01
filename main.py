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
)
from PySide6.QtGui import QPixmap, QFont, QPainter, QColor
from PySide6.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cyb3rOwl: Malware & Vulnerability Scanner")
        self.setMinimumSize(1100, 600)
        self.dark_mode = True  # Default mode
        self.initUI()

    def initUI(self):
        self.setStyleSheet(self.app_style())
        main_layout = QHBoxLayout()

        # Sidebar
        self.sidebar = QWidget()
        self.sidebar_layout = QVBoxLayout()
        self.sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.sidebar.setFixedWidth(250)  # Ensure sufficient width for buttons

        # Add the cyb3r.png image at the top of the sidebar
        logo_image = QLabel()
        logo_pixmap = QPixmap("cyb3r.png")

        # Check if the image is loaded successfully
        if not logo_pixmap.isNull():
            # Scale the image proportionally to a larger size (keeping aspect ratio)
            logo_pixmap = logo_pixmap.scaled(
                120,
                120,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            logo_image.setPixmap(logo_pixmap)
            logo_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        else:
            print("Error: Unable to load the image.")

        self.sidebar_layout.addWidget(logo_image)

        # Page Selection Section
        self.page_selection_section = QWidget()
        self.page_selection_layout = QVBoxLayout()
        self.page_selection_layout.setSpacing(5)  # Reduced space between buttons
        self.page_selection_section.setLayout(self.page_selection_layout)
        self.page_selection_section.setStyleSheet(self.page_selection_section_style())

        # Sidebar Buttons (for page navigation)
        self.buttons = {}
        pages = [
            "Home",
            "Malware Scan",
            "Vulnerability Scan",
            "System Health Check",
            "Privacy Settings",
        ]
        for page in pages:
            btn = self.create_sidebar_button(page)
            self.page_selection_layout.addWidget(btn)
            self.buttons[page] = btn

        self.sidebar_layout.addWidget(self.page_selection_section)

        # Add stretch here so buttons stay at the bottom
        self.sidebar_layout.addStretch()

        # Add the special "Update" and "Upgrade" buttons at the bottom of the sidebar
        self.update_button = self.create_special_button(
            "Update", "#36d2cf", smaller=True
        )  # Smaller size
        self.sidebar_layout.addWidget(self.update_button)

        self.upgrade_button = self.create_special_button(
            "Upgrade", "#36d2cf", smaller=True
        )  # Smaller size
        self.sidebar_layout.addWidget(self.upgrade_button)

        self.sidebar.setLayout(self.sidebar_layout)

        # Main content area with the background and layout
        self.stack = QStackedWidget()
        self.pages = {
            "Home": self.create_home_page(),
            "Malware Scan": self.create_coming_soon_page("🦠 Malware Scan"),
            "Vulnerability Scan": self.create_coming_soon_page("🔍 Vulnerability Scan"),
            "System Health Check": self.create_system_health_page(),
            "Privacy Settings": self.create_privacy_page(),
        }
        for page in self.pages.values():
            self.stack.addWidget(page)

        # Add sidebar and main content area to the main layout
        content_layout = QHBoxLayout()
        content_layout.addWidget(self.sidebar)

        # Create the separator and place it after the sidebar content
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setLineWidth(2)  # Set line width to ensure it's visible
        separator.setStyleSheet("background-color: #2a637a;")  # Dark teal for separator
        separator.setFixedWidth(2)  # Ensure the width is fixed for the separator

        content_layout.addWidget(separator)  # Add the separator after sidebar

        # Add main content area (stacked widget) to the layout
        content_layout.addWidget(self.stack, 4)

        # Set the main layout for the central widget
        container = QWidget()
        container.setLayout(content_layout)
        self.setCentralWidget(container)

        self.navigate("Home")

    def create_sidebar_button(self, page_name):
        btn = QPushButton(page_name)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setIconSize(QSize(30, 30))
        btn.setStyleSheet(self.button_style())
        btn.setFont(self.get_bold_font())  # Make button text bold
        btn.setMinimumHeight(50)  # Slightly reduced height for a better fit
        btn.setMinimumWidth(220)  # Set width to ensure uniformity
        btn.clicked.connect(lambda _, name=page_name: self.navigate(name))
        return btn

    def create_special_button(self, text, color, smaller=False):
        btn = QPushButton(text)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setIconSize(QSize(30, 30))
        btn.setStyleSheet(
            f"background-color: {color}; color: white; padding: 12px; border-radius: 15px; border: 2px solid black;"
        )
        btn.setFont(self.get_bold_font())  # Make the special buttons bold
        if smaller:
            btn.setMinimumHeight(40)  # Smaller height
            btn.setMinimumWidth(180)  # Smaller width
        else:
            btn.setMinimumHeight(50)  # Same height as regular buttons
            btn.setMinimumWidth(220)  # Same width as regular buttons
        return btn

    def navigate(self, page_name):
        index = list(self.pages.keys()).index(page_name)
        self.stack.setCurrentIndex(index)
        for btn_name, btn in self.buttons.items():
            btn.setStyleSheet(
                self.selected_button_style()
                if btn_name == page_name
                else self.button_style()
            )

    def create_home_page(self):
        layout = QVBoxLayout()
        title = QLabel("Cyb3rOwl: Malware & Vulnerability Scanner")
        title.setObjectName("header")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Align title to the left
        title.setFont(self.get_large_font())  # Larger font size for title
        layout.addWidget(title)

        description = QLabel(
            "Welcome to Cyb3rOwl, your companion for scanning and protecting your system from malware and vulnerabilities."
        )
        description.setAlignment(Qt.AlignmentFlag.AlignLeft)
        description.setFont(self.get_regular_font())  # Regular font for description
        layout.addWidget(description)

        return self.create_scrollable_page(layout)

    def create_system_health_page(self):
        layout = QVBoxLayout()
        title = QLabel("💻 System Health Check")
        title.setObjectName("header")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Align title to the left
        title.setFont(self.get_large_font())
        layout.addWidget(title)
        return self.create_scrollable_page(layout)

    def create_privacy_page(self):
        layout = QVBoxLayout()
        title = QLabel("🔒 Privacy Settings")
        title.setObjectName("header")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Align title to the left
        title.setFont(self.get_large_font())
        layout.addWidget(title)
        return self.create_scrollable_page(layout)

    def create_coming_soon_page(self, title_text):
        layout = QVBoxLayout()
        title = QLabel(title_text)
        title.setObjectName("header")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Align title to the left
        title.setFont(self.get_large_font())
        layout.addWidget(title)
        return self.create_scrollable_page(layout)

    def create_scrollable_page(self, layout):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_widget.setLayout(layout)
        scroll_area.setWidget(scroll_widget)
        container = QWidget()
        container.setLayout(QVBoxLayout())
        container.layout().addWidget(scroll_area)
        return container

    def button_style(self):
        return "background-color: #0f2334; color: white; padding: 12px; border-radius: 15px;"

    def selected_button_style(self):
        return "background-color: #2a637a; color: #36d2cf; padding: 12px; border-radius: 15px;"

    def page_selection_section_style(self):
        return """
        background: linear-gradient(to bottom, #0f2334, #2a637a);  /* Gradient from dark blue to medium teal */
        border-radius: 10px;
        padding: 15px;
        margin: 10px;
        """

    def app_style(self):
        if self.dark_mode:
            return "* { background-color: #0f2334; color: #c5e2df; font-family: 'Segoe UI'; }"
        else:
            return "* { background-color: #FFFFFF; color: #000000; font-family: 'Segoe UI'; }"

    def get_bold_font(self):
        return QFont("Segoe UI", 12, QFont.Weight.Bold)

    def get_large_font(self):
        return QFont("Segoe UI", 18, QFont.Weight.Bold)

    def get_regular_font(self):
        return QFont("Segoe UI", 14, QFont.Weight.Normal)


class BackgroundImage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("cyb3r.png")
        pixmap = pixmap.scaled(
            self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
        )
        painter.setOpacity(0.2)  # Set 80% transparency
        painter.drawPixmap(0, 0, pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
