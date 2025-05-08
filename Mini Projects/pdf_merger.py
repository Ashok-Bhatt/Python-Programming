from PyPDF2 import PdfMerger
from os import listdir

pdfmerger = PdfMerger()
path = input(r"Enter the path: ")

for file in listdir(path):
    if file.endswith(".pdf"):
        pdfmerger.append(path+"/"+file)

pdfmerger.write(path+"/merged_pdf.pdf")