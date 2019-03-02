CD C:\Users\pro\Documents\Mines\3A\pst\PST-Toeic

REM remove the previous uild
DEL CORRECTION_TOEIC build /S /Q
DEL Programme /Q

REM remove recursively empty folders
ROBOCOPY dist dist /S /MOVE
ROBOCOPY CORRECTION_TOEIC CORRECTION_TOEIC /S /MOVE
ROBOCOPY build build /S /MOVE



REM build the application
C:\Users\Guillaume\Anaconda2\envs\pst25\python.exe setup_py2exe.py

REM Move the necessary folders
MKDIR dist\Dev
ROBOCOPY Dev dist\Dev /E
MKDIR dist\poppler-0.68.0
ROBOCOPY poppler-0.68.0 dist\poppler-0.68.0 /E


REM Rename and organize the folder
MKDIR CORRECTION_TOEIC
MKDIR Programme
ROBOCOPY dist CORRECTION_TOEIC\Programme /E /move
REM COPY Correction_TOEIC.bat CORRECTION_TOEIC\Correction_TOEIC.bat
RMDIR Programme

PAUSE

