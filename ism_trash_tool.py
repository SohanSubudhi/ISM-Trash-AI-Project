import sys
import os
from streamlit.web import cli

if __name__ == '__main__':
    # This ensures the current directory is in the python path
    # so that our local imghdr.py can be found.
    sys.path.insert(0, os.getcwd())
    
    sys.argv = ["streamlit", "run", "src/run_app.py"]
    sys.exit(cli.main())
