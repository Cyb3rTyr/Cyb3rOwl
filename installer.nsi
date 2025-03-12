# ========================== NSIS Script for CyberOwl Installation ==========================

# Name of the installer
OutFile "CyberGuarInstaller.exe"

# Default installation directory
InstallDir $PROGRAMFILES\CyberGuar

# Request admin privileges for installation
RequestExecutionLevel admin

# ========================== Pages ==========================
Page directory
Page instfiles

# ========================== Sections ==========================

# Installation Section
Section "Install"

    # Create the installation directory
    CreateDirectory $INSTDIR

    # Set the output path to the installation directory
    SetOutPath $INSTDIR

    # Clone the GitHub repository to the installation directory
    ExecWait 'git clone https://github.com/Cyb3rTyr/Cyb3rOwl.git "$INSTDIR"'

    # Create Start Menu shortcut
    CreateDirectory $SMPROGRAMS\CyberGuar
    CreateShortcut "$SMPROGRAMS\CyberGuar\CyberGuar.lnk" "$INSTDIR\Cyb3rOwl\main.exe"

    # ===================== Create Desktop Shortcut Directly ======================
    # Create Desktop shortcut with the new icon (Cyb3rOwl_icon.ico should be in the installation folder)
    CreateShortcut "$DESKTOP\CyberGuar.lnk" "$INSTDIR\Cyb3rOwl\main.exe" "" "$INSTDIR\Cyb3rOwl_icon.ico"

    # Write the uninstaller to the installation directory
    WriteUninstaller "$INSTDIR\Uninstall.exe"

SectionEnd

# Uninstallation Section
Section "Uninstall"

    # Remove installed files and shortcuts
    Delete "$INSTDIR\Cyb3rOwl\main.exe"
    Delete "$SMPROGRAMS\CyberGuar\CyberGuar.lnk"
    Delete "$DESKTOP\CyberGuar.lnk"

    # Remove the installation directory
    RMDir $INSTDIR
    RMDir "$SMPROGRAMS\CyberGuar"
    RMDir $DESKTOP

    # Remove the uninstaller
    Delete "$INSTDIR\Uninstall.exe"

SectionEnd

# ========================== Modern Style Progress Bar ==========================

# Customize the progress bar
Function .onInit
    SetDetailsPrint both
    # Set the progress bar color to green
    SetCtlColors $INSTDIR "#00FF00"  # Green color for the progress bar
FunctionEnd

# ========================== End of Script ==========================
