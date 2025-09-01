import gradio as gr
import warnings
from urllib3.exceptions import NotOpenSSLWarning
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)
import requests

API_URL = "http://127.0.0.1:8000/query"  # FastAPI backend