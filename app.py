import os
from flask import Flask, flash, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

from models import *

def allowed_file(filename):
  _, _, ext = filename.rpartition('.')
  return '.' in filename and \
          ext.lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET','POST']) 
def index():
  if request.method == 'POST':
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
      flash('No selected file')
      return redirect(request.url)
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      img = Image(filename)
      try:
        db.session.add(img)
        db.session.commit()
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('image',id=img.id))
      except IntegrityError:
        db.session.rollback()
        flash('File already exists')
        return redirect(request.url)
  return render_template('index.html')

@app.route('/<id>/', methods=['GET','POST'])
def image(id):
  img = Image.query.get(id)
  return render_template('image.html',filename=img.filename)

if __name__ == '__main__':
  app.run()
