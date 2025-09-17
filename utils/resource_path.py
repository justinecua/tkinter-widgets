import os, sys

def resource_path(relative_path: str) -> str:
    """
   absolute path
    """
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:

        base_path = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.dirname(base_path) 
    return os.path.join(base_path, relative_path)
