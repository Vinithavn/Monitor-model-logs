# Monitor-model-logs
Monitor the metrics of a model remotely, while training the model 


Please follow the below steps:

  1. Login to our website or Create a new account here:
  2. Call the API from your training script by following these steps
 
      a. Install the monitor-logs package using
      
      ![install](https://github.com/Vinithavn/Monitor-model-logs/blob/master/utils/carbon%20(4).png)
      
      b. Import the package
      
      ![import](https://github.com/Vinithavn/Monitor-model-logs/blob/master/utils/carbon%20(5).png)
      
      c. Call the api from the training script using
      
      ![call](https://github.com/Vinithavn/Monitor-model-logs/blob/master/utils/carbon%20(3).png)
      
        Epoch_num - Epoch num from the training
        
        Actual - Ground truth labels
        
        Preds - Predicted labels
        
        Username - username of the user
        
        Session_name - Name of the session(can be defined inside the training script)

  3. Once the model starts training, go to this website 
  4. Select your session name, and metric to view the model logs



