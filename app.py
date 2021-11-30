import streamlit as st
import nltk
nltk.download('stopwords')
import os
os.system('python -m spacy download en_core_web_sm')
from pyresparser import ResumeParser
from io import BytesIO


def main():
    st.title("Resume Parser")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Resume Parser</h2>
    </div>
    """

    uploaded_files = st.file_uploader("Add resume", type = ['pdf'], accept_multiple_files = True)
    if uploaded_files is None:
        st.success('Add resume')
    else:
        for file in uploaded_files:
            with open("uploaded_files_copy.pdf", 'wb') as f:
                f.write(file.read())

            # name = (ResumeParser("uploaded_files_copy.pdf").get_extracted_data())['name']
            name = (ResumeParser("uploaded_files_copy.pdf").get_extracted_data()).get('name', 'Name not found')
            st.success(f"This is {name}'s resume and \n file name is {file.name}")
    
if __name__=='__main__':
    main()
    
