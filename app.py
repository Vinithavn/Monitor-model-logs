'''
MAIN API. Where all the reading and writing of all info happens
'''

from flask import Flask,request,jsonify,redirect
from werkzeug.utils import secure_filename
from flask_cors import cross_origin
import os
import json
import re
import matplotlib.pyplot as plt
import time

app = Flask(__name__)
app.secret_key = "super secret key" 

file_dir = "data"


@app.route('/',methods =["POST","GET"])
@cross_origin()
def home():
    if request.method == 'POST': 
        input_data = request.form["data"]   
        username = request.form["username"]
        session = request.form["session"] 

        if not os.path.exists("data/"+username):
            os.makedirs("data/"+username)
        a_file = open("data/"+username+"/"+session+".json", "a")
        json.dump(input_data, a_file)
        a_file.close()               
        return input_data
    else:
        username = request.form["username"]
        session = request.form["session"] 
        metric = request.form["metric"] 
        a_file = open("data/"+username+"/"+session+".json", "r")
        output = a_file.read() 
        regex = re.compile(f'\'{metric}\': ([0-9\.]*)') 
        out = regex.findall(output) 
        for img_file in os.listdir("static/images"):
            if img_file.startswith(username+"_"+session):
                os.remove("static/images/"+img_file)
                                   
        for idx in range(len(out)):
            out[idx] = float(out[idx]) 
        time_stamp = time.time()
        plt.clf()
        plt.plot(out) 
        filename = "../static/images/"+username+"_"+session+"_"+str(time_stamp)+".png"
        print(filename)
        plt.savefig("static/images/"+username+"_"+session+"_"+str(time_stamp)+".png")
        return '{} = {}'.format(str(out),filename)
                
if __name__ == '__main__':
    app.run(port=3000,debug = False)
    
    