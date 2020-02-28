from app import db

class IMC(db.Model):

    id = db.Column(db.INTEGER(), primary_key=True)
    peso = db.Column(db.DECIMAL())
    altura = db.Column(db.DECIMAL())

    def __repr__(self):
        return "<IMC peso:{} altura:{}>".format(self.peso, self.altura)