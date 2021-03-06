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
            text=read_pdf(filename)
            name=extract_name(text)
            hard,soft = extract_skills2(text)
            hard_set,soft_set=graph_hardsoft(hard,soft)
            hard_plot = hard_skills[0].value_counts().plot.pie
            soft_plot = soft_skills[0].value_counts().plot(kind='bar')
            return render_template("index.html", name=name, soft_plot=soft_plot, hard_plot=hard_plot)

@app.route("/portfolio", methods = ['POST'])
def projects():
            proj1 = request.form['project1name']
            desc1 = request.form['project1description']
            proj2 = request.form['project2name']
            desc2 = request.form['project2description']
            proj3 = request.form['project3name']
            desc3 = request.form['project3description']
            proj4 = request.form['project4name']
            desc4 = request.form['project4description']
            return render_template("index.html", project1name = proj1, 
            project1description = desc1, project2name = proj2, 
            project2description = desc2, project3name = proj3, 
            project3description = desc3, project3name = proj4, 
            project3description = desc4)

@app.route("/portfolio", methods = ['POST'])
def social():
            soc1 = request.form['linkedin']
            soc2 = request.form['github']
            #soc3 = request.form['social3']
            get_repo(url)
            repo = get_repo(url)
            return render_template("index.html", linkedin = soc1,
            github = soc2, repo=repo)
        
if __name__ == "__main__":
    app.run(debug=True)   

