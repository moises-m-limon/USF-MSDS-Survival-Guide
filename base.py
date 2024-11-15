import streamlit as st
import os
import nbformat
from nbconvert import MarkdownExporter

def list_notebooks(folder_path):
    """List all .ipynb files in the specified folder."""
    return [f for f in os.listdir(folder_path) if f.endswith(".ipynb")]

def render_notebook_as_markdown(file_path):
    """Convert a Jupyter Notebook to Markdown and return the content."""
    with open(file_path, "r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Convert notebook to markdown
    exporter = MarkdownExporter()
    markdown_content, _ = exporter.from_notebook_node(notebook)
    return markdown_content

def display_notebook(folder_path, selected_notebook):
    """Render the selected notebook from a folder."""
    file_path = os.path.join(folder_path, selected_notebook)
    try:
        markdown_content = render_notebook_as_markdown(file_path)
        st.markdown(f"### Notebook: `{selected_notebook}`")
        st.markdown(markdown_content)
    except Exception as e:
        st.error(f"Failed to render notebook: {e}")
