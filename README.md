# Monitor-model-logs
Monitor the metrics of a model remotely, while training the model 


Please follow the below steps:

  1. Login to our website or Create a new account here: http://139.162.6.184:5000/
  ![app](https://github.com/Vinithavn/Monitor-model-logs/blob/master/utils/Screenshot_2022-08-30-15-59-19-17_40deb401b9ffe8e1df2f1cc5ba480b12.jpg)
  
  2. Call the API from your training script by following these steps
 
      a. Install the monitor-logs package using
      
      ![install](https://github.com/Vinithavn/Monitor-model-logs/blob/master/utils/carbon%20(4).png)
      
      b. Import the package
      
      ![import](https://github.com/Vinithavn/Monitor-model-logs/blob/master/utils/carbon%20(5).png)
      
      c. Call the api from the training script using
      
      ![call](https://github.com/Vinithavn/Monitor-model-logs/blob/master/utils/carbon%20(3).png)
      
        Epoch_num - Epoch num from the training
        
        Actual - 1-d array of ground truth labels
        
        Preds - 1-d array of predicted labels
        
        Username - username of the user
        
        Session_name - Name of the session(can be defined inside the training script)

  3. Once the model starts training, go to this website: http://139.162.6.184:5000/
  4. Select your session name, and metric to view the model logs



