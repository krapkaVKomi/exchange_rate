from datetime import datetime
from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/exchange_rate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

api = Api()


class UAN(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.date)
    rate_to_usd = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<UAN %r>' % self.rate_to_usd


class UANSchema(ma.Schema):  # десеріалізація
    class Meta:
        fields = ('date', 'rate_to_usd')


class PLN(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.date)
    rate_to_usd = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<PLN %r>' % self.rate_to_usd


class PLNSchema(ma.Schema):
    class Meta:
        fields = ('date', 'rate_to_usd')


class EUR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.date)
    rate_to_usd = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<EUR %r>' % self.rate_to_usd


class EURSchema(ma.Schema):
    class Meta:
        fields = ('date', 'rate_to_usd')


class CAD(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.date)
    rate_to_usd = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<CAD %r>' % self.rate_to_usd


class CADSchema(ma.Schema):
    class Meta:
        fields = ('date', 'rate_to_usd')


UAN_schema = UANSchema()
uan = UAN(id=0, date='2023-01-01', rate_to_usd=0.2456)


class Main(Resource):

    def get(self, exchange, date):
        print(exchange, date)
        if exchange:
            with app.test_request_context():
                res = UAN_schema.dump(uan)
            return res


api.add_resource(Main, "/api/<string:exchange>/<string:date>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")

