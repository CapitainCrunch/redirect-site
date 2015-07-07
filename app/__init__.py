import os
from flask import Flask, redirect


app = Flask(__name__)

@app.route('/'):
def index():
    return redirect('https://vk.com/volunteer_medic')


