from flask import Flask,render_template,request, Response
from datetime import datetime
import sys, csv, json
import pandas as pd
import pymysql
from werkzeug.utils import secure_filename
credentials to connect database

# hostname = 'harshinedb.mysql.database.azure.com'
# username = 'harshine@harshinedb'
# password = 'RadheKrishna1'
# database = 'cloud'
# myConnection = pymysql.connect(host=hostname, user=username, passwd=password, db=database, autocommit=True,cursorclass=pymysql.cursors.DictCursor, local_infile=True)
# print "Database Connected"

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('harshine.html')

@app.route('/val', methods=['POST'])
def val():
    name = request.form['net']
    verify = "Select * from equake where net='hv'"
    
    
    cursor.execute(verify)
    myConnection.commit()
    cursor.close()
    output = cursor.fetchall()
    
	return render_template("in.html", data=text)


@app.route('/next', methods=['GET','POST'])
def next():
    c1 = request.form['c1']
    c2 = request.form['c2']
    k = int(request.form['k'])
    data = pd.read_csv("/C:/Users/harsh/Desktop/harshine/flaskapp/equake.csv")
    x1 = []
    
	y1 = []
    x = data[c1].tolist()
    
	
	y = data[c2].tolist()
    data1 = np.column_stack((x,y))
   
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data1)
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    
	
	y_kmeans = kmeans.predict(data1)
    plt.scatter(data1[:,0], data1[:,1], c = y_kmeans)
    plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
    plt.savefig("/C:/Users/harsh/Desktop/harshine/flaskapp/graph.png")
    unique, counts = np.unique(labels, return_counts=True)
    df = pd.DataFrame({"clusters": unique, "count": counts})
    df.to_csv("/C:/Users/harsh/Desktop/harshine/flaskapp/equake.csv", index=False)
    c_no = [1, 2, 3]
    return render_template('visual.html', data = counts, c = centroids)

@app.route('/submit', methods=['GET','POST'])
def submit():
    c1 = str(request.form['c1'])
    c2 = str(request.form['c2'])
    k = str(request.form['k'])
    df1 = pd.DataFrame({"latitude": c1, "longitude": c2, "depth":k})
    df1.to_csv("/C:/Users/harsh/Desktop/harshine/flaskapp/equake.csv", index=True)
    data12 = enrolled
    return render_template('choice.html', data12 = data12)

@app.route('/bar', methods=['POST'])
def bar():
    return render_template('barchart.html')


@app.route('/pie', methods=['POST'])
def pie():
    return render_template('piechart.html')


if __name__ == "__main__":
    app.run(debug=True,port=5000)