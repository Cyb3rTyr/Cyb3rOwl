# ========================== Installer Properties ==========================
Name "Cyb3rOwl"
OutFile "Cyb3rOwl_Installer.exe"
InstallDir "$PROGRAMFILES\Cyb3rOwl"
BrandingText "Cyb3rOwl v1.6 - by Cyb3rTyr"

# ========================== MUI Pages ==========================
!define MUI_ICON "Cyb3rOwl_icon.ico"          # Installer icon
!define MUI_UNICON "Cyb3rOwl_icon.ico"        # Uninstaller icon
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP "header.bmp"      # Path to the banner image for the welcome page
!define MUI_WELCOMEFINISHPAGE_BITMAP "shield.bmp"

# Include the Modern UI macros for standard installer pages
!include "MUI2.nsh"

!insertmacro MUI_PAGE_WELCOME                # Welcome Page
!insertmacro MUI_PAGE_LICENSE "LICENSE"      # License Page
Page Custom ShortcutPage ShortcutPageLeave   # Shortcut selection page (checkbox) comes before the directory page
!insertmacro MUI_PAGE_DIRECTORY             # Directory Page (for user to select where to install)
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

    # Create a group box for the shortcut options
    ${NSD_CreateGroupBox} 0 0 100% 60u "Shortcut Options"
    Pop $1

    # Add a label for the title
    ${NSD_CreateLabel} 0 10u 100% 12u "Shortcut Options:"
    Pop $2

    # Add a description text
    ${NSD_CreateLabel} 0 24u 100% 24u "Would you like to create a desktop shortcut for Cyb3rOwl?"
    Pop $3

    # Create the checkbox
    ${NSD_CreateCheckbox} 0 48u 100% 12u "Create Desktop Shortcut"
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
    # Set installation path based on user selection (from the directory page)
    SetOutPath $INSTDIR

    # Copy Cyb3rOwl.exe, icon, and banner
    File "Cyb3rOwl.exe"
    File "Cyb3rOwl_icon.ico"
    File "shield.bmp"  # Ensure banner_owl.png is in the same directory as this script or provide the correct path

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
