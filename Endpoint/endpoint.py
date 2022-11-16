from bsr import bank_statement_read
from werkzeug.wrappers import response # Fixing the dates
from flask import Flask, request #import objects from the Flask model
import base64 
import os
import time

app = Flask(__name__) #define app using Flask    

@app.route('/', methods=['POST'])
def bankStatement():
    bs = { "file_path": request.json['file_path'], "bank_name":request.json['bank_name']}
    pdf_file = (bs["file_path"])
    res = bytes(pdf_file, 'utf-8')
    value = base64.decodebytes(res)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    f = open('/tmp/'+timestr+".pdf",'wb')
    f.write(value)
    f.close()
    with open('/tmp/'+timestr+".pdf",'rb') as f:
        bank = bank_statement_read(f,bs["bank_name"]) 
    os.remove('/tmp/'+timestr+".pdf")
    return(bank)

if __name__ == '__main__':
	app.run(debug=True)