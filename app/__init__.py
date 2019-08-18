from flask import Flask, render_template, request, redirect
from .Backend import Backend
from .configs import IP_ADDRESS, DOWNLOAD_DIR, AXEL, CONNECTION

app = Flask(__name__)
from app import views