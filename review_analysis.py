#Importing Libraries:
import streamlit as st 
import pickle
from PIL import Image
import re
import time
import pandas as pd
from transformers import pipeline

#-------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="App-Streamlit",page_icon="random",layout="wide",
                       menu_items={'Get Help': 'http://www.quickmeme.com/img/54/547621773e22705fcfa0e73bc86c76a05d4c0b33040fcb048375dfe9167d8ffc.jpg',
                                   'Report a bug': "https://w7.pngwing.com/pngs/839/902/png-transparent-ladybird-ladybird-bug-miscellaneous-presentation-insects-thumbnail.png",
                                   'About': "# This is a Sentiment Analyzer App based on Amazon reviews built with Streamlit. Log Regression model is used to train"})
sentiment_pipeline = pipeline("sentiment-analysis")
#@st.cache(allow_output_mutation=True) #For Autoupdate in app.
    

#-------------------------------------------------------------------------------------------------------------------------------
st.write("""
         # SENTIMENT CHECKER
         """)

def upload_df():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
        return dataframe
    else:
        return "None"
def apply_model(dataframe):    
    dataframe['Text'] = dataframe['Text'].astype(str)
    dataframe['review_score'] = dataframe['Text'].map(lambda text: sentiment_pipeline(text))
    return dataframe

def get_label(text): #get labels
    for Dict in text:
        return Dict["label"]


# assign reviews with score > 3 as positive sentiment, score < 3 negative sentiment
# remove score = 3 bcoz it gives no insights on the importance of that review

def check_sentiment(dataframe):
    dataframe = dataframe[dataframe['Star'] != 3]
    dataframe['user_semantics'] = dataframe['Star'].apply(lambda rating : "POSITIVE" if rating > 3 else "NEGATIVE")

    rslt_df = dataframe[dataframe['predicted_semantics'] == "POSITIVE"]
    rslt_df = rslt_df[rslt_df['user_semantics'] != rslt_df["predicted_semantics"]]
    return rslt_df

#-------------------------------------------------------------------------------------------------------------------------------


# Decor Func:    
def decor():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Sentiment Checker for NEXTLABS </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    image = Image.open('C:\\Users\\new\\Deplyment_Streamlit\\sentiment-analysis.jpg')
    st.image(image, caption='')    

#--------------------------------------------------------------------------------------------------------------------------------

def main():

    decor()
    dataframe = upload_df()
    if "dataframe" in locals():
    #if dataframe != "None":
        dataframe = apply_model(dataframe)
        dataframe['predicted_semantics'] = dataframe['review_score'].map(lambda text: get_label(text))
        rslt_df = check_sentiment(dataframe)
    
        st.dataframe(rslt_df)  
                
        st.success("Please notify users regarding this.. ...")

    st.markdown("---")
    
#---------------------------------------------------------------------------------------------------------------------------

# My Details:

    expander=st.expander("My Details",expanded=False)
    with expander:
        st.write("Kasi Vinoth S")
#----------------------------------------------------------------------

# Program Starts:
if __name__=='__main__':
    main()
