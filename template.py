latex_template = """
\\documentclass[11pt]{letter} 
% \\usepackage{newcent}
\\usepackage{hyperref} 
\\usepackage{graphicx}
\\topmargin=-1in
\\textheight=8.5in 
\\oddsidemargin=-10pt 
\\textwidth=6.5in
\\let\\raggedleft\\raggedright 

\\begin{document}
\\begin{letter}{  {{address_block}}   } 

\\begin{center}
 \\large\\bf FRANK GRIMES \\\\ % Your name
 %\\vspace{20pt} \\hrule height 1pt % If you would like a horizontal line separating the name from the address, uncomment the line to the left of this text
  23 Spooner Street \\\\ Cambridge MA 02138 \\\\ (555) 555-5555 \\\\ \\small \\href{http://www.yourwebsite.com}{yourwebsite.com} % Your address and phone number
 \\end{center} 
\\vfill

\\opening{Dear {{poc}},} 


I am writing to express my interest in the position: {{ position }} 

{{special_sauce}}
 
I will be attending the January CLOWN-FORMS meeting in San Diego and will be available for interviews. 
Thank you for your consideration. 

% \\closing{Sincerely, \\\\[0.0in]
% \\fromsig{\\includegraphics[scale=.08]{../../Signature.pdf}} \\\\
% \\fromname{} \\\\

\\closing{Sincerely, \\\\[0.0in]
\\fromname{Frank Grimes} \\\\
}

\\end{letter}
\\end{document}
"""

