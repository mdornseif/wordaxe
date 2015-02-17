# -*- coding: utf-8 -*-
from reportlab.platypus import SimpleDocTemplate
#from reportlab.platypus.paragraph import Paragraph
#from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import Color
from reportlab.platypus.flowables import _listWrapOn, _FUZZ
from wordaxe.rl.NewParagraph import Paragraph
from wordaxe.rl.styles import ParagraphStyle, getSampleStyleSheet


def go():
    styles = getSampleStyleSheet()
    style=styles['Normal']
    p1 = Paragraph('This is a paragraph '*1000, style )
    _listWrapOn([p1],500,None)
    print len(p1.split(500,600)),p1._cache['avail']

go()
