from PyPDF2 import PdfWriter
import os 

merger = PdfWriter()

files = [os.path.join("mergePdf", file) for file in os.listdir("mergePdf") if file.endswith(".pdf")]
print(files)

if not files:
    print("There are no PDF files to merge.")
else:
    for pdf in files:
        with open(pdf, "rb") as file:
            merger.append(file)

    if merger.write("mergePdf/merged-pdf.pdf"):
        print("PDF files merged successfully.")
        merger.close()
    else:
        print("Something went wrong during merging.")
