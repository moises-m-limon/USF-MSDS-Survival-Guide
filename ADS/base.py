import streamlit as st
import os
from base import list_notebooks, display_notebook  # Import shared logic

def main():
    st.header("Acing the Data Science Interview")
    current_folder = os.path.dirname(__file__)
    
    # List all notebooks in the current folder
    notebooks = list_notebooks(current_folder)
    
    # Sidebar to select a notebook
    selected_notebook = st.sidebar.selectbox("Select a Notebook", notebooks)
    
    if selected_notebook:
        display_notebook(current_folder, selected_notebook)

if __name__ == "__main__":
    main()
