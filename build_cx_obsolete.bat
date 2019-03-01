CD C:\Users\pro\Documents\Mines\3A\pst\PST-Toeic

DEL dist CORRECTION_TOEIC build /S /Q


C:\Users\Guillaume\Anaconda2\envs\pst25\python.exe setup_cx_freeze.py

REN  build CORRECTION_TOEIC
REN CORRECTION_TOEIC\exe.win-amd64-2.7 Programme

MKDIR CORRECTION_TOEIC\Programme\Dev


REM robocopy dist CORRECTION_TOEIC\Programme /E 
REM /move
robocopy Dev CORRECTION_TOEIC\Programme\Dev /E

COPY exec.bat CORRECTION_TOEIC

REM DEL build /S /Q

REM PAUSE