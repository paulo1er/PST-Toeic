from distutils.core import setup
import py2exe




# http://py2exe.org/index.cgi/ListOfOptions
setup(windows=['main.py'],
			options={
                'py2exe': { 
				'compressed': True,
                
                "dll_excludes": ["MSVFW32.dll",
                                 "AVIFIL32.dll",
                                 "AVICAP32.dll",
                                 "ADVAPI32.dll",
                                 "CRYPT32.dll",
                                 "WLDAP32.dll"]
				}
            }, ) 
	
	
	
"""
conda install -c anaconda pil 
pip install pdf2image
conda install -c conda-forge/label/cf201901 opencv
conda install -c sasview py2exe 

cd C:\Users\pro\Documents\Mines\3A\pst\PST-Toeic

C:\Users\Guillaume\Anaconda2\envs\pst3\python.exe setup.py py2exe

puis copier le dossier Dev dans dist


"""