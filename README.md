# ocrmypdf-flask-example
A simple implementation of ocrmypdf and tesseract with flask for hosting to a server as an API. This code works on linux only as ocrmypdf library does not have support on windows because of missing leptonica dll. 

**For windows consider** https://github.com/lakshay1296/OCR_Conversion_JPEG2PDF. This is image to ocr pdf conversion

## Requirements

Make sure to install libraries in the same manner

- libjpeg : libpng : libtiff : zlib : libwebp : libopenjp2
- leptonica (v1.78) (you can use any version but you would need to change the location of liblept.so location in the code)
- Tesseract (any version)
- Tesseract Language Data (big tessdata)
- ocrmypdf library
- Flask

**You can also use the following URL for installing Tesseract on CentOS 7:**
https://groups.google.com/forum/#!topic/tesseract-ocr/u-PZaakaKs0

## For changing liblept dll location

**In leptonica.py**

lept = ffi.dlopen(find_library('**_Insert your location here_**'))

## Workflow

- The project can be hosted on a server using Flask library
- Project can work only if the pdf files are present on the local system
- Path can be provided through a GET request (or you can change in the code accordingly)
- An OCR and LOG folder is created in the root path
- OCR'd PDF's are stored in the OCR folder and PDF's which were not able to OCR along with their exceptions are stored in LOG.
