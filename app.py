#pip install -r requirements.txt
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
import base64
import uuid
