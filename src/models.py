from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }"""

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    done = db.Column(db.Boolean, unique=False, nullable=False)

    #def __repr__(self):
     #   return 'La tarea es %r' % self.name

    def serialize(self): # metodo que devuelve la informacion de la clase
        return { #retorno de json 
            "id": self.id,
            "name": self.name,
            "done": self.done,
           
        }
