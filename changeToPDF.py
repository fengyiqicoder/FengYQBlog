from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import os

for root, dirs, files in os.walk('.'):
    fileNameArray = files
    break

for fileName in fileNameArray:
    nameWithOutExt = fileName[: -4]
    extenstionName = fileName[-4: ]
    if extenstionName == ".svg":
        drawing = svg2rlg(fileName)
        renderPDF.drawToFile(drawing, "./pdfFiles/" + nameWithOutExt + ".pdf")