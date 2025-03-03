import os
import sys

# Add the project root directory to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.langgraph.main import load_app

if __name__=="__main__":
    load_app()