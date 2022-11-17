import base64, time, os
from werkzeug.wrappers import response
from flask import Flask, request
from collections import namedtuple
from dateutil.parser import parse
from bsr_final import bank_statement_read

app = Flask(__name__)

@app.route('/bankstatement',methods=['POST'])

def bankStatement():
    bs = { "file_path": request.json['file_path'], "bank_name":request.json['bank_name']}
    pdf_file = (bs["file_path"])
    res = bytes(pdf_file, 'utf-8')
    value = base64.decodebytes(res)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    f = open('/tmp/'+timestr+".pdf",'wb'); f.write(value); f.close()
    with open('/tmp/'+timestr+".pdf",'rb') as f:
        bank = bank_statement_read(f,bs["bank_name"]) 
    os.remove('/tmp/'+timestr+".pdf")
    return(bank)

@app.route('/bankstatement', methods=['GET'])
def _get_():
    bs = { "file_path": request.json['file_path'], "bank_name":request.json['bank_name']}
    return (bs)

if __name__ == '__main__':
	app.run(debug=True)