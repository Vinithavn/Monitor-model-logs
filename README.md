# Monitor-model-logs
Monitor the metrics of a model remotely, while training the model 

Please follow the below steps:

  1. Login to our website or Create a new account ![here] (http://139.162.6.184:5000/)
  
  ![app](https://github.com/Vinithavn/Monitor-model-logs/blob/master/Screenshot_2022-08-30-15-59-19-17_40deb401b9ffe8e1df2f1cc5ba480b12.jpg)
  
  2. Call the API from your training script by following these steps
 
      a. Install the monitor-logs package using
      
      ```pip install monitor-logs```
      
      
      b. Import the package
      
      ```from monitor_logs import api```
      
      c. Call the api from the training script using
      
      ```api.call(epoch_num,actual,preds,username,session_name```
      
      ```
      
        Epoch_num - Epoch num from the training
        
        Actual - 1-d array of ground truth labels
        
        Preds - 1-d array of predicted labels
        
        Username - username of the user
        
        Session_name -  Name of the session (User Defined).
        
          - Since you need the session name to read the logs, make sure to give unique and readable name.
          - Please make sure to follow naming convention standard.
          - Special characters such as underscore, hash, dollar, asterisk can be used.
          - session_name shouldn't start with special characters.
       ```

  3. Once the model starts training, go to this website: http://139.162.6.184:5000/
  4. Select your session name, and metric to view the model logs



