!include "MUI2.nsh"  # Include MUI for Modern UI

# Define installer properties
Name "CyberGuar"
OutFile "CyberGuarInstaller.exe"
InstallDir "$PROGRAMFILES\CyberGuar"

# ========================== MUI Pages ==========================
!insertmacro MUI_PAGE_WELCOME         # Welcome Page
!insertmacro MUI_PAGE_LICENSE "LICENSE"  # License Page (displayed as a text string)
!insertmacro MUI_PAGE_DIRECTORY       # Directory Page
!insertmacro MUI_PAGE_INSTFILES       # Installation Progress Page
!insertmacro MUI_PAGE_FINISH          # Finish Page

# Language
!insertmacro MUI_LANGUAGE "English"  # English language

# ========================== Installer Sections ==========================
Section "Install"
    # Set installation path
    SetOutPath $INSTDIR

    # Clone the repository into the installation directory
    ExecWait 'git clone https://github.com/Cyb3rTyr/Cyb3rOwl.git "$INSTDIR"'

    # Download the LICENSE file from GitHub and save it in the installation directory
    NSISdl::download "https://raw.githubusercontent.com/Cyb3rTyr/Cyb3rOwl/main/LICENSE" "$INSTDIR\LICENSE"

    # Create Start Menu shortcut
    CreateDirectory $SMPROGRAMS\CyberGuar
    CreateShortcut "$SMPROGRAMS\CyberGuar\CyberGuar.lnk" "$INSTDIR\Cyb3rOwl\main.exe"

    # Create Desktop shortcut
    CreateShortcut "$DESKTOP\CyberGuar.lnk" "$INSTDIR\Cyb3rOwl\main.exe" "" "$INSTDIR\Cyb3rOwl_icon.ico"

    # Write Uninstaller
    WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

Section "Uninstall"
    # Remove installed files and shortcuts
    Delete "$INSTDIR\Cyb3rOwl\main.exe"
    Delete "$SMPROGRAMS\CyberGuar\CyberGuar.lnk"
    Delete "$DESKTOP\CyberGuar.lnk"

    # Remove the installation directory
    RMDir $INSTDIR
    RMDir "$SMPROGRAMS\CyberGuar"
    RMDir $DESKTOP

    # Remove uninstaller
    Delete "$INSTDIR\Uninstall.exe"
SectionEnd
