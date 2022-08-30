# Monitor-model-logs
Monitor the metrics of a model remotely, while training the model 


Please follow the below steps:

  1. Login to our website or Create a new account here:
  2. Call the API from your training script by following these steps
 
      a. Install the monitor-logs package using
      !(C:\Users\Vinitha\Downloads\carbon (3).png)
      b. Import the package
      c. Call the api from the training script using 
        Epoch_num - Epoch num from the training
        Actual - Ground truth labels
        Preds - Predicted labels
        Username - username of the user
        Session_name - Name of the session(can be defined inside the training script)

  3. Once the model starts training, go to this website 
  4. Select your session name, and metric to view the model logs



