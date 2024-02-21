import fitz  # pymupdf
import pytesseract # tesseract
from openpyxl import Workbook
from PIL import Image
import io

# You need to specify the path to tesseract executable if it's not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # For Windows
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # For Linux/Mac
pdfPath = 'C:\\Users\\IGS\\Desktop\\phone-book.pdf'
xlsxPath = 'C:\\Users\\IGS\Desktop\\phone-book.xlsx'

def pdf_to_xlsx(pdf_path, xlsx_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Create a new Excel workbook and select the active worksheet
    workbook = Workbook()
    worksheet = workbook.active
    
    for page_num in range(len(pdf_document)):
        # Get the page
        page = pdf_document[page_num]
        
        # Get the image of the page
        pix = page.get_pixmap()
        image_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(image_bytes))
        
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(image, lang='eng')
        
        # Split the text into lines and write each line to a cell
        #for row_num, line in enumerate(text.split('\n'), 1):
        for row_num, line in enumerate(text.split('|'), 1):
            worksheet.cell(row=row_num, column=page_num + 1, value=line)
    
    # Save the workbook
    workbook.save(xlsx_path)
    
    # Close the PDF file
    pdf_document.close()

# Usage
#pdf_to_xlsx('example.pdf', 'output.xlsx')
pdf_to_xlsx(pdfPath,xlsxPath)