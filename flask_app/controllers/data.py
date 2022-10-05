from csv import excel
from flask import render_template, request, redirect
import pandas as pd
import matplotlib.pyplot as plt


from flask_app import app

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/pedidos')
def pedidos():
    
    return render_template('pedidos.html')


@app.route('/analisis')
def analisis():
    
    return render_template('analisis.html')

