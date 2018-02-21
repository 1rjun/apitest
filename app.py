from flask import Flask,render_template,request

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

#initialize the application
app = Flask(__name__)

#connect the engine with the database
engine = create_engine("postgresql://arjunsingh:arjunsingh@localhost/mydb")

db = scoped_session(sessionmaker(bind=engine))

@app.route('/')
def home():
    """
    This will be the homepage of our webapplication
    """
    return render_template('homepage.html')


#this will be the post method 
@app.route('/post_location',methods=["POST"])
def post_location():
    if request.method == "POST":
        """
        post lat and long of the location,
        and check if pincode exists or not
        """
        #retreive the value from form after submission
        zipcode = request.form["zipcode"]
        zipcode = "IN/" + zipcode
        print(zipcode)
        #Now its time to run sql query to retrieve the zipcode from table
        #here geo_data is my table name
        check_Zip = db.execute("SELECT * FROM geo_data WHERE id=:zipcode",
        {'zipcode':zipcode}).rowcount

        print(check_Zip)
        if check_Zip>0:
            #now check about the lat and long of the existing zipcode 
            check_lat = db.execute("SELECT * FROM geo_data WHERE id=:zipcode",
            {"zipcode":zipcode}
            ).fetchall()

            for items in check_lat:
                #now we have the latitude and longitude
                latitude = items.latitude
                longitude = items.longitude
                if latitude == '' or longitude == '':
                    return "sorry latitude and longitude values are not here "
                    
                    #here problem exist we have the ids but they dont have the latitude and longitude