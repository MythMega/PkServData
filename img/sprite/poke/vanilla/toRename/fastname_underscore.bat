@echo off
REM Script de renommage pour les .gif : _n → _normal et _s → _shiny

REM Renomme tous les fichiers se terminant par _n.gif en _normal.gif
ren "*_n.gif" "*_normal.gif"

REM Renomme tous les fichiers se terminant par _s.gif en _shiny.gif
ren "*_s.gif" "*_shiny.gif"

echo Renommage terminé.
pause
