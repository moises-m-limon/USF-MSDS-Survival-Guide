import streamlit as st

def main():
    st.title("USF - MSDS Survival Guide")
    st.markdown("""
    This is the home page. Use the sidebar to navigate through the app.

    ### Features:
    - Dynamic navigation based on folders.
    - Display `.ipynb` files in markdown.
    - Modular and reusable structure.

    **Select a folder from the sidebar to get started.**
    """)

if __name__ == "__main__":
    main()
