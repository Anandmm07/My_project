#pip install -r requirements.txt
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
import base64
import uuid
import logging
from datetime import datetime, timedelta
import threading
import time
from typing import Dict, Optional
from dotenv import load_dotenv
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
# Configure Gemini API
api_key = "AIzaSyAj7QePSFe7l4dVBBcfbLD8cYXt-uc2bH0"
