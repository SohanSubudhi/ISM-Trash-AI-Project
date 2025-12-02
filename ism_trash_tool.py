import sys
import os
from streamlit.web import cli
from src import run_app

if __name__ == '__main__':
    # This ensures the current directory is in the python path
    # so that our local imghdr.py can be found.
    run_app.main()
