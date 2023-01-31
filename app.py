from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_apscheduler import APScheduler
import datetime
import requests
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/rate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
api = Api()
scheduler = APScheduler()


class UAN(db.Model):  # UAH (гривня)
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d"))
    rate_to_usd = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<UAN %r>' % self.rate_to_usd


class UANSchema(ma.Schema):  # десеріалізація
    class Meta:
        fields = ('date', 'rate_to_usd')


class PLN(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d"))
    rate_to_usd = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<PLN %r>' % self.rate_to_usd


class PLNSchema(ma.Schema):
    class Meta:
        fields = ('date', 'rate_to_usd')


class EUR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d"))
    rate_to_usd = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<EUR %r>' % self.rate_to_usd


class EURSchema(ma.Schema):
    class Meta:
        fields = ('date', 'rate_to_usd')


class CAD(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d"))
    rate_to_usd = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<CAD %r>' % self.rate_to_usd


class CADSchema(ma.Schema):
    class Meta:
        fields = ('date', 'rate_to_usd')


def funk(exchange):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={exchange}&from=USD&amount=1"

    payload = {}
    headers = {"apikey": "kx4ivlz0zmOuRSz53WqiIoHyAF1cNbeF"}
    response = requests.request("GET", url, headers=headers, data=payload)

    result = response.text
    result = json.loads(result)['info']
    return result['rate']


UAN_schema = UANSchema()
PLN_schema = PLNSchema()
EUR_schema = EURSchema()
CAD_schema = CADSchema()


class Main(Resource):

    def get(self, exchange, date):
        print(exchange, date)
        if exchange and date:
            if exchange == 'UAH':
                rates = UAN.query.filter_by(date=date).all()
                rate = funk(exchange=exchange)
                item = UAN(rate_to_usd=rate)
                if len(rates) == 0:
                    try:
                        db.session.add(item)
                        db.session.commit()
                    except:
                        return "ERROR WRITING TO DB"
                    rate = item

                elif rates[-1] != item:
                    try:
                        db.session.add(item)
                        db.session.commit()
                    except:
                        return "ERROR WRITING TO DB"
                    rate = item

                else:
                    rate = rates[-1]
                with app.test_request_context():
                    res = UAN_schema.dump(rate)
                return res

            if exchange == 'PLN':
                rates = PLN.query.filter_by(date=date).all()
                rate = funk(exchange=exchange)
                item = PLN(rate_to_usd=rate)
                if len(rates) == 0:
                    try:
                        db.session.add(item)
                        db.session.commit()
                    except:
                        return "ERROR WRITING TO DB"
                    rate = item
                elif rates[-1] != item:
                    try:
                        db.session.add(item)
                        db.session.commit()
                    except:
                        return "ERROR WRITING TO DB"
                    rate = item

                else:
                    rate = rates[-1]
                with app.test_request_context():
                    res = PLN_schema.dump(rate)
                return res

            if exchange == 'CAD':
                rates = CAD.query.filter_by(date=date).all()
                rate = funk(exchange=exchange)
                item = CAD(rate_to_usd=rate)
                if len(rates) == 0:
                    try:
                        db.session.add(item)
                        db.session.commit()
                    except:
                        return "ERROR WRITING TO DB"
                    rate = item

                elif rates[-1] != item:
                    try:
                        db.session.add(item)
                        db.session.commit()
                    except:
                        return "ERROR WRITING TO DB"
                    rate = item

                else:
                    rate = rates[-1]
                with app.test_request_context():
                    res = CAD_schema.dump(rate)
                return res

            if exchange == 'EUR':
                rates = EUR.query.filter_by(date=date).all()
                rate = funk(exchange=exchange)
                item = EUR(rate_to_usd=rate)
                if len(rates) == 0:
                    try:
                        db.session.add(item)
                        db.session.commit()
                    except:
                        return "ERROR WRITING TO DB"
                    rate = item

                elif rates[-1] != item:
                    try:
                        db.session.add(item)
                        db.session.commit()
                    except:
                        return "ERROR WRITING TO DB"
                    rate = item

                else:
                    rate = rates[-1]
                with app.test_request_context():
                    res = EUR_schema.dump(rate)
                return res


api.add_resource(Main, "/api/<string:exchange>/<string:date>")
api.init_app(app)


def upload_data():
    print('scheduler upload data')


if __name__ == "__main__":
    scheduler.add_job(id='Scheduled task', func=upload_data, trigger='interval', seconds=3)
    scheduler.start()
    app.run(debug=True, port=3000, host="127.0.0.1")

