# app-review
- This app is used to identify the reviews where the semantics of review text does not match rating. Particularly positive semantics with negative rating.
- We are using the pretrained _distilbert-base-uncased-finetuned-sst-2-english_ model bcoz it is already focused on sentiment-analyis. link - https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english
- assign reviews with rating > 3 as positive sentiment and < 3 as negative sentiment. While the rating of 3 is rejected as it has less importance and irrelevant to our problem statement.
- We match the predicted and the user semantics, then display a final dataframe for the employees to notify the users regarding this.
- We also have the count of total semantic mismatch and total positive semantic mismatch in review ratings.
- The app is deplyoyed using Streamlit library
- You have the option of downloading the dataframe as a csv file once the training is complete.
- The deployment of the app is done through AWS EC2 Console. I have learned the process of deploying in AWS just to show my learning capability. I hope it is appreciated.
- The deployed link is : https://innerpeas.in/
### Have a good day!
