from Interface import interface
from p2j import pdf2image
from solve import solve
from export import export


filepath = interface()
n = pdf2image(filepath)

results = []
for i in range(n):
    print(i)
    pathJPG = "temp/out"+str(i)+".jpg"
    results.append(solve(pathJPG))

export(results)
