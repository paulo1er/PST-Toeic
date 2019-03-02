# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable


if len(sys.argv) == 1:
    sys.argv.append("build")



base = None
if sys.platform == "win32":
    base = "Win32GUI"




build_exe_options = {"packages": ["numpy"],
					"excludes": [ "PyQt4", "sqlite3", 
                                  "scipy.lib.lapack.flapack",
                                  "PyQt4.QtNetwork",
                                  "PyQt4.QtScript",
                                  "PyQt5"],
                     "optimize": 2}


setup(
    name = "CORRECTION_TOEIC",
    version = "0.1",
    description = "CORRECTION_TOEIC",
	
	
	options = {"build_exe": build_exe_options},
    executables = [Executable("CORRECTION_TOEIC.py", base = base, icon= "Dev\logo.ico")])