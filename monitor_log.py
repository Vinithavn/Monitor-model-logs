
'''
this script is used to create the payload when the user calls the api from their training script. 
The user passes their actuals and predictions to the api call function. Inside the function it creates all the 
metrics and create a payload. This payload is then passed to the main api(app.py file) and the main API will write all the 
info to a json file inside the user sessionS
'''

import requests, json 
from sklearn import metrics

class api():  
    def call(epoch, y_true, y_pred ,username,session):
        files=[]
        headers = {} 
        model_info = dict()
        
        model_info["epoch"]=epoch+1
        
        #accuracy
        model_info["accuracy"] = metrics.accuracy_score(y_true,y_pred)
       
        #precision
        try:
            model_info["precision"] = metrics.precision_score(y_true, y_pred)
        except:
            model_info["precision"] = metrics.precision_score(y_true, y_pred,average = "micro")
        
        #recall
        try:
            model_info["recall"] = metrics.recall_score(y_true, y_pred)
        except:
            model_info["recall"] = metrics.recall_score(y_true, y_pred,average="micro")
                
        #balanced accuracy
        model_info["balanced accuracy"]= metrics.balanced_accuracy_score(y_true,y_pred) 
        
        #confusion matrix
#         model_info["confusion matrix"] = metrics.confusion_matrix(y_true, y_pred)
    
        #f1 score
        try:
            model_info["f1 score"] = metrics.f1_score(y_true,y_pred)
        except:
            model_info["f1 score"] = metrics.f1_score(y_true,y_pred,average="micro")
         
                
        payload= {'data': str(model_info),'username':username,"session":session} 
        
        response = requests.request("POST", "http://127.0.0.1:3000/", headers=headers, data=payload, files=files)
        
        return response