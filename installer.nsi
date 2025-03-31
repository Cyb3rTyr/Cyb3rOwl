!include "MUI2.nsh"  # Include MUI for Modern UI

# ========================== Installer Properties ==========================
Name "Cyb3rOwl"
OutFile "Cyb3rOwlInstaller.exe"
InstallDir "$PROGRAMFILES\Cyb3rOwl"

# ========================== MUI Pages ==========================
!insertmacro MUI_PAGE_WELCOME                # Welcome Page
!insertmacro MUI_PAGE_LICENSE "LICENSE"     # License Page
Page Custom InstallationInfoPage            # Info Page
Page Custom ShortcutPage ShortcutPageLeave  # Shortcut selection page (checkbox)
!insertmacro MUI_PAGE_DIRECTORY             # Directory Page
!insertmacro MUI_PAGE_INSTFILES             # Installation Progress Page
!insertmacro MUI_PAGE_FINISH                # Finish Page

# ========================== Language ==========================
!insertmacro MUI_LANGUAGE "English"

# ========================== Variables ==========================
Var ShortcutCheckbox   # Variable to hold checkbox handle

# ========================== Custom Pages ==========================

# ---- Installation Info Page ----
Function InstallationInfoPage
    nsDialogs::Create 1018
    Pop $0

    ${NSD_CreateLabel} 0 0 100% 100% "The following items will be installed:\r\n\r\n- Cyb3rOwl main application\r\n- Optional desktop shortcut\r\n\r\nClick Next to continue."
    Pop $1

    nsDialogs::Show
FunctionEnd

# ---- Shortcut Selection Page ----
Function ShortcutPage
    nsDialogs::Create 1018
    Pop $0

    ${NSD_CreateCheckbox} 0 0 100% 12u "Create Desktop Shortcut"
    Pop $ShortcutCheckbox
    # Check the checkbox by default
    ${NSD_SetState} $ShortcutCheckbox ${BST_CHECKED}

    nsDialogs::Show
FunctionEnd

Function ShortcutPageLeave
    ${NSD_GetState} $ShortcutCheckbox $R3  # $R3 = 1 if checked, 0 if not
FunctionEnd

# ========================== Installer Section ==========================
Section "Install"
    # Set installation path
    SetOutPath $INSTDIR

    # Copy the embedded Python folder (ensure all files from python_embedded are copied)
    SetOutPath "$INSTDIR\python_embedded"
    File /r "python_embedded\*"

    # Copy the Cyb3rOwl files, including main.py
    SetOutPath "$INSTDIR\Cyb3rOwl_client\GUI"
    File "Cyb3rOwl_client\GUI\main.py"

    # Copy the LICENSE file
    NSISdl::download_quiet "https://raw.githubusercontent.com/Cyb3rTyr/Cyb3rOwl/main/LICENSE" "$INSTDIR\LICENSE"

    # Copy the application icon (Cyb3rOwl_icon.ico)
    File "Cyb3rOwl_icon.ico"

    # Create Start Menu shortcut that launches Python with main.py
    CreateDirectory "$SMPROGRAMS\Cyb3rOwl"
    CreateShortcut "$SMPROGRAMS\Cyb3rOwl\Cyb3rOwl.lnk" '"$INSTDIR\python_embedded\python.exe"' '"$INSTDIR\Cyb3rOwl_client\GUI\main.py"' "$INSTDIR\Cyb3rOwl_icon.ico"

    # Conditionally create Desktop shortcut based on checkbox
    ${If} $R3 == 1
        CreateShortcut "$DESKTOP\Cyb3rOwl.lnk" '"$INSTDIR\python_embedded\python.exe"' '"$INSTDIR\Cyb3rOwl_client\GUI\main.py"' "$INSTDIR\Cyb3rOwl_icon.ico"
    ${EndIf}

    # Write uninstaller
    WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

# ========================== Uninstaller Section ==========================
Section "Uninstall"
    # Remove installed files and shortcuts
    Delete "$INSTDIR\Cyb3rOwl_client\GUI\main.py"
    Delete "$INSTDIR\Cyb3rOwl_icon.ico"
    Delete "$SMPROGRAMS\Cyb3rOwl\Cyb3rOwl.lnk"
    Delete "$DESKTOP\Cyb3rOwl.lnk"

    # Remove the installation directory
    RMDir /r "$INSTDIR\Cyb3rOwl_client\GUI"
    RMDir /r "$INSTDIR\python_embedded"
    RMDir "$INSTDIR"
    RMDir "$SMPROGRAMS\Cyb3rOwl"

    # Remove uninstaller
    Delete "$INSTDIR\Uninstall.exe"
SectionEnd
