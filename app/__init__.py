from flask import Flask, render_template, request, redirect
from .Backend import Backend

app = Flask(__name__)
from app import views