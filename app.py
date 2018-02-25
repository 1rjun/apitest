from flask import Flask, request
from flask_restful import Api, Resource

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# initialize the application
app = Flask(__name__)

# connect the engine with the database
engine = create_engine("postgresql://arjunsingh:arjunsingh@localhost/mydb")

db = scoped_session(sessionmaker(bind=engine))

api = Api(app)

data = {}

# lets retrieve the data first

dataInGeoData = db.execute("SELECT * FROM geo_data").fetchall()

for values in dataInGeoData:
    id = values.id
    place_name = values.place_name
    admin_name = values.admin_name
    latitude = values.latitude
    longitude = values.longitude
    data[id] = {
        "place_name":place_name,
        "admin_name":admin_name,
        "latitude":latitude,
        "longitude":longitude
    }


class Data(Resource):

    @staticmethod
    def get():
        return {
            "data": data
        }


class GetData(Resource):

    @staticmethod
    def get(id):
        return {
            data[id]
        }


class PostLocation(Resource):


    def post(self,message):

        pincodeid1 = request.form["pincode"]
        pincodeid = 'IN/' + pincodeid1
        city = request.form["city"]
        address = request.form["address"]
        try:
            if len(data[pincodeid])>0:

                # the address exists in the api ,so we are not returning anything and pass the function
                pass
        
        except:
            """Here is the key error means the  pincode not exists,we need to put the data inside the api """





class GetUsingPostgres(Resource):

    def get(self,location):
        try:
            location = "IN/" + location
            return{
                "result":data[location]
            }
        except:
            pass


class Getlocation

api.add_resource(Data,'/')
api.add_resource(GetData,'/id/<int:id>')
api.add_resource(PostLocation,'/post_location/<string:message>')
api.add_resource(GetUsingPostgres,'/getusing_postgres/<string:location>')

if __name__ == '__main__':
    app.run(debug=True)