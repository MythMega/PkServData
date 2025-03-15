@echo off
setlocal enabledelayedexpansion

echo Traitement des fichiers GIF dans %CD%
echo.

for %%F in (*.gif) do (
    set "oldfile=%%F"
    set "newfile=%%F"
    
    rem Remplacer "-n.gif" par "_normal.gif"
    set "newfile=!newfile:-n.gif=_normal.gif!"
    
    rem Remplacer "-s.gif" par "_shiny.gif"
    set "newfile=!newfile:-s.gif=_shiny.gif!"
    
    if not "!oldfile!"=="!newfile!" (
        ren "!oldfile!" "!newfile!"
        if errorlevel 1 (
            echo ERREUR : Impossible de renommer "!oldfile!"
        ) else (
            echo Succès.
        )
        echo.
    ) else (
        echo Aucun changement pour "%%F"
    )
)

endlocal
echo.
echo Fin du script.
pause
