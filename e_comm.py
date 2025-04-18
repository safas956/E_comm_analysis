import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns


def main():
    st.title("This is an app for ecomm")
    st.sidebar.title("You can upload your file here")

    upload_file= st.sidebar.file_uploader("Upload your file",type=['csv','xlsx'])

    if upload_file is not None:
        try:
            if upload_file.name.endswith('.csv'):
                df=pd.read_csv(upload_file)
            else:
                df=pd.read_excel(upload_file)
            st.sidebar.success("File has been uploaded")

            st.subheader("Please find the explored data")
            st.dataframe(df.head())

            st.subheader("Lets explore the data")
            st.write("Shape of the data is:", df.shape)
            st.write("The column names in the data are:", df.columns)
            st.write("The missing values in the data are:", df.isnull().sum())
            
            st.subheader("Please find the statistical details below")
            st.write("The statistical analysis of data is:",df.describe())

        except Exception as e:
            print(e)
        

if __name__ == "__main__":
    main()