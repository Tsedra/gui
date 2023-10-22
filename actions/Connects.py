
from pylatex import Document, Section, Command
from pylatex.utils import NoEscape

import subprocess


class Action_for_sol:
    def formulaToWord(lst, ui):
        ui.ready_doc_but.setText("Готово")
        doc = Document()
        for item in lst:
            if (item):  
                doc.append(NoEscape(item))
        doc.generate_tex("ful")
        subprocess.Popen(['pandoc.exe', 'ful.tex', '--bibliography=bib_file.bib', '-o', 'doc.docx'])
        