# app-review
- This app is used to identify the reviews where the semantics of review text does not match rating. Particularly positive semantics with negative rating.
- We are using the pretrained DistilBert model bcoz it is already focused on sentiment-analyis.
- assign reviews with rating > 3 as positive sentiment and < 3 as negative sentiment. While the rating of 3 is rejected as it has less importance and irrelevant to our problem statement.
- We match the predicted and the user semantics, then display a final dataframe for the employees to notify the users regarding this.
- We also have the count of total semantic mismatch and total positive semantic mismatch in review ratings.
- The app is deplyoyed using Streamlit library
### Have a good day!
