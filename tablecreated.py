"""
This is a python script to put the csv data in our postgresql table GEO_DAT
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from csv import reader as read
# here i database engine which connect with the database ,and 1st arjunsingh is my username and second arjunsingh is my database username
# and mydb is my postgresql database name which is available in my local computer
# you can put yours link in create_engine whenever you try to run this script

<<<<<<< HEAD
# make sure to give your postgres database link in create_engine 
=======
# here i put my database link 
>>>>>>> branch
engine = create_engine("postgresql://arjunsingh:arjunsingh@localhost/mydb")


db = scoped_session(sessionmaker(bind=engine))

def main():
    IN = open("IN.csv","r")
    IN_read = read(IN)
    for id, place_name, admin_name, latitude, longitude, accuracy in IN_read:

<<<<<<< HEAD
        # geo_data is my table name 
        
=======
        # here geo_data is my table name
>>>>>>> branch
        db.execute("INSERT INTO geo_data VALUES (:id,:place_name,:admin_name,:latitude,:longitude,:accuracy)",
        {"id":id,"place_name":place_name,"admin_name":admin_name,"latitude":latitude,"longitude":longitude,
        "accuracy":accuracy})
        db.commit()

main()