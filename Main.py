import os
import datetime
import ocrmypdf
import pandas as pd
from flask import jsonify
from flask import Flask, flash, request, redirect, render_template
import base64



app = Flask(__name__)

GET_URL = "/"
GET_URL_INDEX = "/index"
GET_URL_PDF = "/pdf"
root = "/home/lakshay/PycharmProjects/ocrmyPDF/PDF/"

# @app.route("/", methods=["GET", "POST"])
# def home():
#
#     return render_template("home.html")

# @app.route(GET_URL_INDEX, methods=["GET", "POST"])
# def index():
#
#     # return jsonify(string = "it's Working")
#     # return render_template("home.html", value = jsonify(string = "It's working"))
#     return render_template('home.html', value = jsonify("It's Working"))


# @app.route(GET_URL_PDF, methods=["GET", "POST"])
# def get_test_file():
#     with open(root + "Ameritech Equipment Purchase Agreement_1227_1995.PDF", "rb") as data_file:
#         data = data_file.read()
#     encoded_data = base64.b64encode(data).decode('utf-8')
#     return render_template("test.html", encoded_data=encoded_data)

@app.route(GET_URL, methods=["GET", "POST"])
def main():

    # /home/lakshay/PycharmProjects/ocrmyPDF/PDF

    location = request.args.get("path")

    df = pd.DataFrame(columns=["Path", "File Name", "Exception"])
    count = (df["Path"].count())

    # print (Path)

    count1 = 0

    if os.path.exists(location):

        try:

            os.makedirs(str(location) + "/OCR")
            os.makedirs(str(location) + "/LOG")

        except Exception:
            pass

        for root, dir, files in os.walk(location):
            for singFile in files:

                # if str(singFile).endswith(".pdf"):
                if singFile == "MW Complete Pain Solutions.pdf":

                    count1 = count1 + 1

                    input_loc = location + "/" + singFile
                    output_loc = location + "/OCR/" + singFile

                    try:

                        ocrmypdf.ocr(input_file=input_loc, output_file=output_loc,
                                 deskew=True, force_ocr=True)

                    except Exception as e:

                        print (e)

                        if "pdf is encrypted" in str(e).lower():
                            count = count + 1
                            df.loc[count] = [root, singFile, "Encrypted PDF"]
                        else:
                            df.loc[count] = [root, singFile, str(e)]

                    print ("File " + str(count1) + ":" + " " + singFile + " has been OCR'd")
                    break

            df.to_csv(location + "/LOG/Failed_Log.csv")

            data = jsonify(string = "The OCR is complete!\nThe OCR'd files has been place on " + root + "/OCR\n"
                                    "The list of Error Files has been placed on " + root + "/LOG")

            return render_template("home.html", value= data)

    else:

        return jsonify(string= "Path does not exist.")

        # return "<h1>The OCR is complete!</h1>" \
        #        "<ul>" \
        #        "<li>The OCR'd files has been place on <b>" + root + "/OCR</b>" \
        #         "<li>The list of Error Files has been placed on <b>" + root + "/LOG</b>" \
        #         "</ul>"
#


if __name__ == '__main__':

    app.run(host="192.168.1.59", port="3", debug=True, ssl_context=('/home/lakshay/PycharmProjects/ocrmyPDF/certs/cert.pem',
                                        '/home/lakshay/PycharmProjects/ocrmyPDF/certs/key.pem'))
    # app.run()

    lis = []

    # Start Time
    start_time = datetime.datetime.now()
    lis.append(start_time)

    # Main Function
    main()

    # End Time
    end_time = datetime.datetime.now()
    lis.append(end_time)

    print ("Start Time: " + str(lis[0]))
    print ("End Time: " + str(lis[1]))
