import streamlit as st
import os
import importlib.util

def load_base_py(folder_name):
    """Dynamically load and execute base.py from a folder."""
    base_file = os.path.join(folder_name, "base.py")
    if os.path.exists(base_file):
        spec = importlib.util.spec_from_file_location("base", base_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.main()  # Assumes each `base.py` has a `main()` function.
    else:
        st.error(f"No `base.py` found in {folder_name}")

def load_home_page():
    """Load the home page."""
    home_file = "home.py"
    if os.path.exists(home_file):
        spec = importlib.util.spec_from_file_location("home", home_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.main()  # Assumes `home.py` has a `main()` function.
    else:
        st.error("No `home.py` found. Please add it to the root folder.")

def main():
    st.set_page_config(
        page_title="USF - MSDS Survival Guide",
)
    st.sidebar.title("Courses")
    
    # Include 'Home' in the navigation options
    folders = ["Home"] + [
        d for d in os.listdir() if os.path.isdir(d) and "base.py" in os.listdir(d)
    ]
    
    # Sidebar navigation
    selected_folder = st.sidebar.selectbox("Select a Page", folders)
    
    if selected_folder == "Home":
        load_home_page()
    else:
        load_base_py(selected_folder)

if __name__ == "__main__":
    main()
