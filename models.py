from app import db

class Image(db.Model):
  __tablename__ = 'images'
  id = db.Column(db.Integer(), primary_key=True)
  filename = db.Column(db.String(), unique=True)

  def __init__(self, filename):
    self.filename = filename

  def __repr__(self):
    return '<Image {}>'.format(self.filename)
