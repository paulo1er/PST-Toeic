CD C:\Users\pro\Documents\Mines\3A\pst\PST-Toeic

DEL dist CORRECTION_TOEIC build /S /Q
RMDIR dist
REM remove recursively empty folders
ROBOCOPY CORRECTION_TOEIC CORRECTION_TOEIC /S /MOVE
ROBOCOPY build build /S /MOVE