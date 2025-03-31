!include "MUI2.nsh"  # Include MUI for Modern UI

# ========================== Installer Properties ==========================
Name "Cyb3rOwl"
OutFile "Cyb3rOwl_Installer.exe"
InstallDir "$PROGRAMFILES\Cyb3rOwl"
BrandingText "Cyb3rOwl v1.6 - by Cyb3rTyr"

# ========================== MUI Pages ==========================
!define MUI_ICON "assets\Cyb3rOwl_icon.ico"          # Installer icon
!define MUI_UNICON "assets\Cyb3rOwl_icon.ico"        # Uninstaller icon
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP "assets\header.bmp"      # Path to the banner image for the welcome page
!define MUI_WELCOMEFINISHPAGE_BITMAP "assets\shield.bmp"

!insertmacro MUI_PAGE_WELCOME                # Welcome Page
!insertmacro MUI_PAGE_LICENSE "LICENSE"      # License Page
Page Custom ShortcutPage ShortcutPageLeave   # Shortcut selection page (checkbox)
!insertmacro MUI_PAGE_DIRECTORY             # Directory Page
!insertmacro MUI_PAGE_INSTFILES             # Installation Progress Page
!insertmacro MUI_PAGE_FINISH                # Finish Page

# ========================== Language ==========================
!insertmacro MUI_LANGUAGE "English"

# ========================== Variables ==========================
Var ShortcutCheckbox   # Variable to hold checkbox handle

# ========================== Custom Pages ==========================
Function ShortcutPage
    nsDialogs::Create 1018
    Pop $0

    ${NSD_CreateCheckbox} 0 0 100% 12u "Create Desktop Shortcut"
    Pop $ShortcutCheckbox

    # Check the checkbox by default
    ${NSD_Check} $ShortcutCheckbox

    nsDialogs::Show
FunctionEnd

Function ShortcutPageLeave
    ${NSD_GetState} $ShortcutCheckbox $R0  # $R0 = 1 if checked, 0 if not
FunctionEnd

# ========================== Installer Section ==========================
Section "Install"
    # Set installation path
    SetOutPath $INSTDIR

    # Copy Cyb3rOwl.exe, icon, and shield.bmp from assets folder
    File "Cyb3rOwl.exe"
    File "assets\Cyb3rOwl_icon.ico"
    File "assets\shield.bmp"  # Replaced banner_owl.png with shield.bmp

    # Create the Desktop shortcut if checkbox is checked
    ${If} $R0 == 1
        CreateShortcut "$DESKTOP\Cyb3rOwl.lnk" "$INSTDIR\Cyb3rOwl.exe" "" "$INSTDIR\Cyb3rOwl_icon.ico"
    ${EndIf}

    # Create the Start Menu shortcut
    CreateDirectory "$SMPROGRAMS\Cyb3rOwl"
    CreateShortcut "$SMPROGRAMS\Cyb3rOwl\Cyb3rOwl.lnk" "$INSTDIR\Cyb3rOwl.exe" "" "$INSTDIR\Cyb3rOwl_icon.ico"

    # Write uninstaller
    WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

# ========================== Uninstaller Section ==========================
Section "Uninstall"
    # Remove installed files and shortcuts
    Delete "$INSTDIR\Cyb3rOwl.exe"
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
