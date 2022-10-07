from csv import excel
from flask import render_template, request
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
from io import BytesIO




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
    final_table = clean_table.to_html()

    print(final_table)
    
    # search = False
    # q = request.args.get('q')
    # if q:
    #     search = True

    # page = request.args.get(get_page_parameter(), type=int, default=1)

    # pagination = Pagination(page=page, search=search, record_name='tables')

    return render_template('pedidos.html', final_table=[final_table], titles=[''])


@app.route('/analisis/')
def plot():

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
    total = clean_table.groupby(['NOMBRE', 'Tipo de pedido'])['numero de pedido'].count()

    img = BytesIO()
    # y = [1,2,3,4,5]
    # x = [0,2,1,3,4]

    # plt.plot(total)
    total.plot(kind='bar',figsize=(13,16))
    
    
    plt.show()

    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('plot.html', plot_url=plot_url)

