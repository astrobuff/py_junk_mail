import jinja2 
import os 
import sys
sys.path.append(os.getcwd())

import schoollist
import template 

template = jinja2.Template(template.latex_template)

for d in schoollist.SCHOOLS: 
    f = open("./submit/source/%s.tex" % d["knickname"], "w")
    f.writelines(template.render(d))
    f.close() 
    os.system('pdflatex -interaction batchmode -output-directory ./submit/letters/ ./submit/source/%s.tex ' % d["knickname"])
    os.system('rm ./submit/letters/*.log ./submit/letters/*.out ./submit/letters/*.aux')


