import pytesseract
from PIL import Image
import csv

# Path to the tesseract executable
# You need to set this if Tesseract is not in your PATH
# e.g., pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Replace 'image.png' with the path to your PNG image file
image_path = 'C:\\Users\\IGS\\Desktop\\phone-book.png'
csv_path = 'C:\\Users\\IGS\\Desktop\\phone-book.csv'

# Open the image
image = Image.open(image_path)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(image)

# Split text into lines and then create a list of lists (one per line)
lines = text.split('\n')
#lines = text.split('|')
lines = [line.split() for line in lines if line.strip() != '']

# Write the lines of text to a CSV file
with open(csv_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(lines)

print(f"Text extracted and written to {csv_path}")