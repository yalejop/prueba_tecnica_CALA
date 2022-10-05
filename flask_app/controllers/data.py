from csv import excel
from flask import render_template, request, redirect
import pandas as pd
import matplotlib.pyplot as plt


from flask_app import app

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/pedidos/')
def pedidos():
    
    textFile = './flask_app/files/ejercicio1_b2.txt'
    text = pd.read_csv(textFile, sep="\t")
    excelFile = './flask_app/files/ejercicio1_b1.xlsx'
    excel = pd.read_excel(excelFile)
    del excel['\como\lidiar\con\este\campo']
    table_complete = text.merge(excel, left_on='CEDULA', right_on='cc_cliente')
    table = table_complete.dropna()
    table['Nombre_Completo'] = table['NOMBRE'].str.capitalize() + ' ' + table['APELLIDO'].str.capitalize()
    table['Tipo de pedido'] = table['Tipo de pedido'].str.upper()
    table['Fecha'] = '25/11/2014'
    table['Fecha'] = pd.to_datetime(table['Fecha'])
    table['NACIMIENTO'] = pd.to_datetime(table['NACIMIENTO'])
    table['Edad'] = (((table['Fecha'] - table['NACIMIENTO']).dt.days)/ 365.2425).astype(int)
    cols_to_subset = ['NOMBRE', 'APELLIDO', 'CEDULA', 'NACIMIENTO', 'Nombre_Completo', 'Edad', 'Tipo de pedido', 'numero de pedido']
    clean_table = table[cols_to_subset]
    
    print(clean_table)
    
    return render_template('pedidos.html', clean_table=clean_table)


@app.route('/analisis')
def analisis():
    
    return render_template('analisis.html')

