import PyPDF2

# https://docs.trendmicro.com/all/ent/ddi/v6.5/en-us/docs/ddi_6.5_ag.pdf
# DDI Administrator's Guide
pdffileobj = open('localdata/test.pdf', 'rb')

# create reader variable that will read the pdffileobj
pdfreader = PyPDF2.PdfReader(pdffileobj)

# This will store the number of pages of this pdf file
x = len(pdfreader.pages)

# create a variable that will select the selected number of pages
with open('localdata/Paper.txt', 'w') as f:
    for i in range(x):
        pageobj = pdfreader.pages[i]
        text = pageobj.extract_text()
        tab_text = text.replace("\n", "\t")
        f.write(tab_text)
        f.write("\n")
