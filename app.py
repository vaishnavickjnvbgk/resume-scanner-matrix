import streamlit as st
from skills import skills
from resume import scanner
import tkinter as tk
from tkinter import filedialog
import dotenv
import os
from main import preprocess
from experience import total_exp
from degree import degree
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
def main():
                        st.title("Automated recruitment system")
                        # import libraries
                        count=[]

                    # Set up tkinter
                        root = tk.Tk()
                        root.withdraw()

                    # Make folder picker dialog appear on top of other windows
                        root.wm_attributes('-topmost', 1)

                    # Folder picker button
                    #by default
                    #first pick pdf only then text folder
                        pdf_path="./pdf"
                        text_path="./text"
                        st.write('Please select a folder to download pdf file:')
                        clicked = st.button('Folder Picker',key="pdf")
                        if clicked:
                            pdf_path= filedialog.askdirectory(master=root)
                            os.environ["API_PATH_PDF"] = pdf_path
                            st.write(pdf_path)
                        st.write('Please select a folder to store text files:')
                        clicked = st.button('Folder Picker',key="text")
                        if clicked:
                            text_path=filedialog.askdirectory(master=root)
                            os.environ["API_PATH_TXT"] = text_path
                            st.write(text_path)
                            preprocess(pdf_path,text_path)

                    
                    
                            
                        choices =["skills", "total_exp", "degree"]
                        options = st.multiselect("Choose your options", choices)
                    
                        result_dct={}
                        data=[]
                        for i in options:
                
                            data.append(globals()[i]())
                        
                    
                
                    
                        
                        print(data)
                        if not data:
                            st.write("Please enter valid condition")
                        else: 
                            
                            result=scanner(data,options,os.environ["API_PATH_TXT"] +'/')
                            
                            
                        if st.button("Apply",key="apply"):
                            print("result111  ",result)
                            
                            
                            for i in result:
                                    if i=="invalid":
                                        st.warning("Please enter valid condition")
                                    else:
                                        st.write(i+" satisfies the requirement")
                                    

        
if __name__ == '__main__':
    main()

