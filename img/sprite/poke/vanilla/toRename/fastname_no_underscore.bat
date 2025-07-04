@echo off
setlocal enabledelayedexpansion

REM Boucle sur tous les fichiers se terminant par "n.gif"
for %%F in (*n.gif) do (
  REM %%~nF = nom du fichier sans extension
  set "name=%%~nF"
  REM on supprime le dernier caractère (le "n")
  set "base=!name:~0,-1!"
  ren "%%F" "!base!_normal.gif"
)

REM Boucle sur tous les fichiers se terminant par "s.gif"
for %%F in (*s.gif) do (
  set "name=%%~nF"
  set "base=!name:~0,-1!"
  ren "%%F" "!base!_shiny.gif"
)

endlocal
echo Renommage finito.
pause
