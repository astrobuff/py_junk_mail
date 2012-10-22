About 
=====

This is a little python script to prepare latex cover letters.  

To use, just edit 'schoollist.py' and 'template.py' to add the info the schools you are applying to and the cover letter you want to 
use. As you will see in schoollist.py, you can add 'special sauce' sentences to specific cover letters. 

Once you have added your schools, just run 
> python create_cover_letters.py 

Your letters & the latex source will be placed and ./submit/letters and ./submit/source 


Caveats 
=======

In only know that it works on my personal linux machine---I suppose it would probably work on Mac OS X as well. 

the create_cover_letters.py makes some calls using 
> system("command line stuff goes here") 

I know you aren't supposed to do this, but I can't figure out subprocess, so...

For it to work, you need to have pdflatex, jinja2 and python. 
