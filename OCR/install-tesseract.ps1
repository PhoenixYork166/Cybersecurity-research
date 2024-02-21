# winget install --id=UB-Mannheim.TesseractOCR  -e;
$url = 'https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe';
$path = 'C:\Users\IGS\Desktop\tesseractOCR.exe';
Invoke-WebRequest -Uri $url -OutFile $path;
Start-Process -FilePath $path -ArgumentList '/S' -Wait;