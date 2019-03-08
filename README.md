# PST-Toeic


Ce programme corrige les copies de TOEIC blanc automatiquement.



Pour installer les modules sous anaconda : 
    conda install -c anaconda pil 
    pip install pdf2image
    conda install -c conda-forge/label/cf201901 opencv

	installer cx_Freeze via pip (notre version était cx_Freeze-5.1.1)




Pour le transformer en executable windows : 
	- Remplacer le fichier pdf2image.py par celui fourni. Celui-ci correspond a la version pdf2image-1.4.1. 
		Si il a changé, voir le diff avec le fichier pdf2image_original.py.
		Chez moi, ce fichier est dans C:\Users\moi\Anaconda2\envs\mon-environnement\Lib\site-packages\pdf2image
	
	- Dans build_cx_freeze.bat, remplacer a la ligne 12 mon chemin vers python par le votre.
    
	- lancer build_cx_freeze.bat
	
	
	
	

