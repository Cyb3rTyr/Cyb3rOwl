!include "MUI2.nsh"  # Include MUI for Modern UI

# ========================== Installer Properties ==========================
Name "Cyb3rOwl"
OutFile "Cyb3rOwlInstaller.exe"
InstallDir "$PROGRAMFILES\Cyb3rOwl"

# ========================== MUI Pages ==========================
!insertmacro MUI_PAGE_WELCOME                # Welcome Page
!insertmacro MUI_PAGE_LICENSE "LICENSE"     # License Page
Page Custom OSSelectionPage OSSelectionPageLeave  # OS Selection Page
Page Custom InstallationInfoPage            # Info Page
Page Custom ShortcutPage ShortcutPageLeave  # Shortcut selection page (checkbox)
!insertmacro MUI_PAGE_DIRECTORY             # Directory Page
!insertmacro MUI_PAGE_INSTFILES             # Installation Progress Page
!insertmacro MUI_PAGE_FINISH                # Finish Page

# ========================== Language ==========================
!insertmacro MUI_LANGUAGE "English"

# ========================== Variables ==========================
Var SelectedOS
Var ShortcutCheckbox   # Variable to hold checkbox handle

# ========================== Custom Pages ==========================

# ---- OS Selection Page ----
Function OSSelectionPage
    nsDialogs::Create 1018
    Pop $0

    ${NSD_CreateLabel} 0 0 100% 12u "Select your operating system:"
    Pop $1

    ${NSD_CreateRadioButton} 0 20u 100% 12u "Windows"
    Pop $2
    ${NSD_CreateRadioButton} 0 34u 100% 12u "Linux"
    Pop $3
    ${NSD_CreateRadioButton} 0 48u 100% 12u "macOS"
    Pop $4

    nsDialogs::Show
FunctionEnd

Function OSSelectionPageLeave
    ${NSD_GetState} $2 $R0
    ${NSD_GetState} $3 $R1
    ${NSD_GetState} $4 $R2

    StrCpy $SelectedOS ""
    ${If} $R0 == ${BST_CHECKED}
        StrCpy $SelectedOS "Windows"
    ${ElseIf} $R1 == ${BST_CHECKED}
        StrCpy $SelectedOS "Linux"
    ${ElseIf} $R2 == ${BST_CHECKED}
        StrCpy $SelectedOS "macOS"
    ${Else}
        MessageBox MB_ICONEXCLAMATION|MB_OK "You must select an OS to continue."
        Abort
    ${EndIf}
FunctionEnd

# ---- Installation Info Page ----
Function InstallationInfoPage
    nsDialogs::Create 1018
    Pop $0

    ${NSD_CreateLabel} 0 0 100% 100% "The following items will be installed:\r\n\r\n- Cyb3rOwl main application\r\n- Dependencies required for the selected OS\r\n- Optional desktop shortcut\r\n\r\nClick Next to continue."
    Pop $1

    nsDialogs::Show
FunctionEnd

# ---- Shortcut Selection Page ----
Function ShortcutPage
    nsDialogs::Create 1018
    Pop $0

    ${NSD_CreateCheckbox} 0 0 100% 12u "Create Desktop Shortcut"
    Pop $ShortcutCheckbox

    nsDialogs::Show
FunctionEnd

Function ShortcutPageLeave
    ${NSD_GetState} $ShortcutCheckbox $R3  # $R3 = 1 if checked, 0 if not
FunctionEnd

# ========================== Installer Section ==========================
Section "Install"
    # Set installation path
    SetOutPath $INSTDIR

    # Clone repository
    ExecWait '"$INSTDIR\git.exe" clone "https://github.com/Cyb3rTyr/Cyb3rOwl.git" "$INSTDIR\Cyb3rOwl"'

    # Download LICENSE file
    NSISdl::download_quiet "https://raw.githubusercontent.com/Cyb3rTyr/Cyb3rOwl/main/LICENSE" "$INSTDIR\LICENSE"

    # Copy application icon
    File "assets\Cyb3rOwl_icon.ico"

    # Create Start Menu shortcut
    CreateDirectory "$SMPROGRAMS\Cyb3rOwl"
    CreateShortcut "$SMPROGRAMS\Cyb3rOwl\Cyb3rOwl.lnk" "$INSTDIR\Cyb3rOwl\main.exe" "" "$INSTDIR\Cyb3rOwl_icon.ico"

    # Conditionally create Desktop shortcut based on checkbox
    ${If} $R3 == 1
        CreateShortcut "$DESKTOP\Cyb3rOwl.lnk" "$INSTDIR\Cyb3rOwl\main.exe" "" "$INSTDIR\Cyb3rOwl_icon.ico"
    ${EndIf}

    # OS-specific handling (just messages here)
    ${If} $SelectedOS == "Windows"
        DetailPrint "Installing Windows-specific dependencies..."
    ${ElseIf} $SelectedOS == "Linux"
        DetailPrint "Installing Linux-specific dependencies..."
    ${ElseIf} $SelectedOS == "macOS"
        DetailPrint "Installing macOS-specific dependencies..."
    ${EndIf}

    # Write uninstaller
    WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

# ========================== Uninstaller Section ==========================
Section "Uninstall"
    # Remove installed files and shortcuts
    Delete "$INSTDIR\Cyb3rOwl\main.exe"
    Delete "$INSTDIR\Cyb3rOwl_icon.ico"
    Delete "$SMPROGRAMS\Cyb3rOwl\Cyb3rOwl.lnk"
    Delete "$DESKTOP\Cyb3rOwl.lnk"

    # Remove the installation directory
    RMDir /r "$INSTDIR\Cyb3rOwl"
    RMDir "$INSTDIR"
    RMDir "$SMPROGRAMS\Cyb3rOwl"

    # Remove uninstaller
    Delete "$INSTDIR\Uninstall.exe"
SectionEnd
