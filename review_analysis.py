#Importing Libraries:
import streamlit as st 
from PIL import Image
import pandas as pd
from transformers import pipeline

#-------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="App-Sentiment-Checker",page_icon="random",layout="wide",
                       menu_items={'Get Help': 'https://www.linkedin.com/in/vinoth24',
                                   'Report a bug': "https://github.com/Vinoth-24/app-review",
                                   'About': "# This is a Sentiment Checker App based on distil-Bert Pretrained model built with Streamlit."})

@st.cache(show_spinner=False, suppress_st_warning=True, allow_output_mutation=True) #For storing the model, saving time purpose.
def load_model():
    #Load pretrained model
    sentiment_pipeline = pipeline("sentiment-analysis")
    return sentiment_pipeline
    
with st.spinner('Loading model..'):
            model_pipeline = load_model()
    
def upload_df():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
        return dataframe
    else:
        return None
    
def apply_model(dataframe):    
    dataframe['Text'] = dataframe['Text'].astype(str) #to avoid dataype as not string problem
    dataframe['review_score'] = dataframe['Text'].map(lambda text: model_pipeline(text))
    return dataframe

def get_label(text): #get labels
    for Dict in text:
        return Dict["label"]

def mismatched_sentiment(dataframe):
    count = 0
    for i,j in zip(dataframe["user_semantics"],dataframe["predicted_semantics"]):
        if i != j:
            count+=1 
        else:
            pass
    return count

def check_sentiment(dataframe):
    dataframe = dataframe[dataframe['Star'] != 3]
    dataframe['user_semantics'] = dataframe['Star'].apply(lambda rating : "POSITIVE" if rating > 3 else "NEGATIVE")
    # going for wrongly classified as negative rows
    total_mismatch_count = mismatched_sentiment(dataframe)
    rslt_df = dataframe[dataframe['predicted_semantics'] == "POSITIVE"]
    rslt_df = rslt_df[rslt_df['user_semantics'] != rslt_df["predicted_semantics"]]
    positive_mismatch_count = rslt_df.shape[0]
    return rslt_df, total_mismatch_count, positive_mismatch_count



def convert_df(df):

    return df.to_csv().encode('utf-8')

# Decor Func:    
def decor():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Sentiment Checker for NEXTLABS </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    image = Image.open('customer_sentiment.png')
    st.image(image, caption='')    

#--------------------------------------------------------------------------------------------------------------------------------

def main():

    decor()
    dataframe = upload_df()
    #if "dataframe" in locals():
    if dataframe is not None:
        with st.spinner('applying model to dataset..'):
            dataframe = apply_model(dataframe)
            dataframe['predicted_semantics'] = dataframe['review_score'].map(lambda text: get_label(text))
            rslt_df, total_senti_mismatch, pos_senti_mismatch = check_sentiment(dataframe)
        st.write("# Required dataframe to notify users.")
        st.dataframe(rslt_df)  
        csv = convert_df(rslt_df)   
        st.download_button(
                    label="Download data as CSV",
                    data=csv,
                    file_name='sentiment-mismatched-data.csv',
                    mime='text/csv',
                    )
        st.write("Total number of mismatched sentiments in reviews :",total_senti_mismatch)
        st.write("Total number of mismatched positive sentiments in reviews :",pos_senti_mismatch)      
        st.success("Please notify users regarding this.. ...")

    st.markdown("---")
    


# My Details:

    expander=st.expander("My Details",expanded=False)
    with expander:
        st.write("Kasi Vinoth S")
        st.write("LinkedIn [link](https://www.linkedin.com/in/vinoth24)")
        st.write("Github repo for this app [link](https://github.com/Vinoth-24/Grammer_checker)")
        st.write("Medium [link](https://medium.com/@vino24995)")
#----------------------------------------------------------------------

# Program Starts:
if __name__=='__main__':
    main()
