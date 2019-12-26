from pdf2image import convert_from_path
import os

for root, dir, files in os.walk("/home/lakshay/PycharmProjects/ocrmyPDF/Med Legal"):
    for file in files:

        pages = convert_from_path(root + "/" + file, 300)
        count = 1
        for page in pages:
            page.save(root + "/image/" + file.replace(".pdf", "_" + str(count) + ".jpeg"), "JPEG")
            count = count + 1

        print (file)