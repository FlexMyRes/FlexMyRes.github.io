import os
from flask import Flask, render_template, request, redirect, url_for, make_response, flash, abort, Response
from werkzeug.utils import secure_filename
from parser import*
import random
#import StringIO


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.txt', '.doc', '.pdf']
app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('index'))

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/portfolio", methods = ['POST'])
def portfolio():
            #fname = request.form['firstname']
            #lname = request.form['lastname']
            text=read_pdf(filename)
            name=extract_name(text)
            hard,soft = extract_skills2(text)
            hard_set,soft_set=graph_hardsoft(hard,soft)
            hard_plot = hard_skills[0].value_counts().plot.pie
            soft_plot = soft_skills[0].value_counts().plot(kind='bar')
            return render_template("index.html",  name=name, hard_plot=hard_plot, soft_plot=soft_plot)

@app.route("/portfolio", methods = ['POST'])
def projects():
            proj1 = request.form['project1name']
            desc1 = request.form['project1description']
            proj2 = request.form['project2name']
            desc2 = request.form['project2description']
            proj3 = request.form['project3name']
            desc3 = request.form['project3description']
            return render_template("index.html", project1name = proj1, 
            project1description = desc1, project2name = proj2, 
            project2description = desc2, project3name = proj3, 
            project3description = desc3)

@app.route("/portfolio", methods = ['POST'])
def social():
            soc1 = request.form['social1']
            soc2 = request.form['social2']
            soc3 = request.form['social3']
            return render_template("index.html", social1 = soc1,
            social2 = soc2, social3 = soc3)
        
if __name__ == "__main__":
    app.run(debug=True)   

