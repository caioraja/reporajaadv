from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def edicao_texto(doc, dic):
    for par in doc.paragraphs:
        run = par.runs[0]
        print(run.text)

