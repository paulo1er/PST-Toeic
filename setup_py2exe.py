from distutils.core import setup
import py2exe	
import struct
import sys


if len(sys.argv) == 1:
    sys.argv.append("py2exe")


dll_excludes=["MSVFW32.dll",
			 "AVIFIL32.dll",
			 "AVICAP32.dll",
			 "ADVAPI32.dll",
			 "CRYPT32.dll",
			 "WLDAP32.dll"]

# si python est en 32 bits, on peut faire un executable tout seul
if struct.calcsize("P") * 8 == 32:
        setup(
    	windows=['CORRECTION_TOEIC.py'],
    	options=
    	{
    		'py2exe': 
    		{ 
    			'compressed': True,
    			'bundle_files':3,
    			"dll_excludes": dll_excludes
    		}
    	},
    	zipfile = None
    )     
# si python est en 64 bits, on a plein de fichiers en plus de l'executable 
else:
    # http://py2exe.org/index.cgi/ListOfOptions
    setup(
		name = "CORRECTION_TOEIC",
		version = "0.1",
		description = "CORRECTION_TOEIC",
    	windows=['CORRECTION_TOEIC.py'],
    	options=
    	{
    		'py2exe': 
    		{ 
				'includes': ['pdf2image'],
    			'compressed': True,
    			"dll_excludes": dll_excludes
    		}
    	},
		zipfile = None
    ) 
	
	
	
"""
cd C:\Users\pro\Documents\Mines\3A\pst\PST-Toeic

C:\Users\Guillaume\Anaconda2\envs\pst25\python.exe setup.py py2exe

puis copier le dossier Dev dans dist

https://py2app.readthedocs.io/en/latest/tutorial.html
"""