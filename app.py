from flask import Flask, render_template, request
import pyodbc
import textwrap
server = 'kiran98.database.windows.net'
database = 'Assignment12'
username = 'kiran1998'
password = 'Omsrn@062466'
driver = '{ODBC Driver 17 for SQL Server}'

app = Flask(__name__)

sqlconnection = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                               ';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = sqlconnection.cursor()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/displayimg')
def disp():
    return render_template('display.html')


@app.route('/disp')
def display():
    ds = "SELECT * from [dbo].[peeps]"
    cursor.execute(ds)
    ftch = cursor.fetchall()
    print(ftch)
    return render_template('disp.html', dsp=ftch)


if __name__ == '__main__':  # only run if you run this file, not if you import other main.py file
    #os.environ['PYTHONPATH'] = os.getcwd()
    app.run(debug=True)
