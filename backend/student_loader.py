import logging 
from numpy import genfromtxt
from time import time
from datetime import datetime
from catering import db, app
from entrack.models.course import StudentModel

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s), 1: lambda s: str(s)})
    return data.tolist()



if __name__ == "__main__":
    t = time()

    try:
        file_name = "students.csv" 
        data = Load_Data(file_name) 

        for i in data:
            logging.debug("....... Adding record {}".format(i))
            record = StudentModel(i[0],i[1])
            db.session.add(record) #Add all the records

        db.session.commit() #Attempt to commit all the records
    except Exception as e:
        db.session.rollback() #Rollback the changes on error
        logging.error("error......rolling back")
        logging.error(e)
    finally:

        logging.info("*-------- Done Adding {0} records in {1} seconds ---------*".format(len(data), str(time()-t)))
    logging.info("Time elapsed: " + str(time() - t) + " s.")