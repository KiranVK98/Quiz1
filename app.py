from flask import Flask, render_template, request
import pyodbc
import textwrap
from azure.storage.blob import BlobServiceClient, ContentSettings
server = 'kiran98.database.windows.net'
database = 'Assignment12'
username = 'kiran1998'
password = 'Omsrn@062466'
driver = '{ODBC Driver 17 for SQL Server}'

app = Flask(__name__)

sqlconnection = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                               ';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = sqlconnection.cursor()

connection_string = "DefaultEndpointsProtocol=https;AccountName=assigns1;AccountKey=FjfZ2UGw8oZx9cDaz2PJYqCtqMlyAXVuGt5Dq8TTcN1InDs8yUrgc8PIu48Xq8A7zku1SP0G+1hN+AStHhKtsQ==;EndpointSuffix=core.windows.net"
img_container = "uniqcontain"


@app.route('/', methods=["POST", "GET"])
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


@app.route('/upd', methods=["POST", "GET"])
def search():
    link = "https://assigns1.blob.core.windows.net/uniqcontain/"
    fh_name = str(request.form.get("name"))
    upd_key = str(request.form.get("mod"))
    names = "UPDATE [dbo].[peeps] SET Keywords='{}' WHERE Name='{}'".format(
        upd_key, fh_name)
    cursor.execute(names)
    print(upd_key)
    return render_template('index.html')


@app.route('/ch', methods=["POST", "GET"])
def ch():
    link = "https://assigns1.blob.core.windows.net/uniqcontain/"
    m_range = str(request.form.get("min"))
    max_range = str(request.form.get("max"))
    det = "SELECT Name,Keywords,Picture FROM [dbo].[peeps] WHERE Height>'{}' AND Height<'{}' ".format(
        m_range, max_range)
    cursor.execute(det)
    ftch = cursor.fetchall()
    return render_template('range.html', ftch=ftch, link=link)


@app.route('/del', methods=["POST", "GET"])
def dels():
    link = "https://assigns1.blob.core.windows.net/uniqcontain/"
    delt = str(request.form.get("del"))
    det = "DELETE FROM [dbo].[peeps] WHERE Name='{}' ".format(delt)
    cursor.execute(det)
    gt = "SELECT * FROM [dbo].[peeps]"
    cursor.execute(gt)
    ftch = cursor.fetchall()
    return render_template("del.html", link=link, ftch=ftch)


if __name__ == '__main__':  # only run if you run this file, not if you import other main.py file
    #os.environ['PYTHONPATH'] = os.getcwd()
    app.run(debug=True)
