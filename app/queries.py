from .models import *

from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from geoalchemy2.shape import to_shape
from sqlalchemy.sql import select
from sqlalchemy import create_engine
import json



Base = declarative_base()
metadata = Base.metadata
engine = create_engine("postgresql://postgres:postgres@localhost/mega_project",echo=True)
Session = sessionmaker(bind=engine)
session = Session()
conn = engine.connect()

 
def get_crops(temp,ph,drainage):
    
    temp_comment=["Very High temperature","Very Low Temperature","Suitable Temperature"]
    ph_comment=[", Very High pH",", Very Low pH",", Suitable pH"]
    drainage_comment=[", Unsuitable drainage",", Suitable drainage"]
    results=[]
    for i in session.query(Crop).all():
        score=0
        comment=""
        #temperature
        low_temp,high_temp=i.temperature.split("-")
        if int(temp)>int(high_temp):comment=comment+temp_comment[0]
        elif int(temp) <int(low_temp):comment=comment+temp_comment[1]
        else: comment=comment+ temp_comment[2]
        #ph comment
        low_ph,high_ph=i.ph.split("-")
        if float(ph)>float(high_ph):comment=comment+ph_comment[0]
        elif float(ph) <float(low_ph):comment=comment+ph_comment[1]
        else: comment=comment+ ph_comment[2]
        #drainage comment
        soil_drainage=i.drainage
        if soil_drainage in ["well","medium","slow","very slow"]:comment=comment + drainage_comment[1]
        else: comment=comment + drainage_comment[0]

        obj=Cropjson(i)
        obj.add_comment(comment)
        results.append(obj)
    return results




    # return [Cropjson(i) for i in session.query(Crop).all()]


def query_area(point):
    # point='36.589 -1.25435'

    try:
        data = {}
       
        query1 = select([Soil], func.ST_Contains(Soil.wkb_geometry, func.ST_Transform(func.ST_GeomFromText(f'POINT({point})', 4326), 4326)))
        result = conn.execute(query1)
        
        for row in result:
            data['pH'] =str(row.phaq)
            data['drainage_desc'] = str(row.sdra_descr)
            data['soil drainage'] =str(row.drai) 
            data['soil class'] =str(row.soil) 
            data['relief'] =str(row.lndf_descr)
            data['slope'] =str(row.slop)

        query_2 = session.query(Aez).filter(func.ST_Contains(Aez.wkb_geometry, func.ST_Transform(func.ST_GeomFromText(f'POINT({point})', 4326), 4326)))
        for i in query_2:
            print(f'Aez zone at this point is: ' , i.aezcode)
            data['Aez'] = str(i.aezcode)

        query_3 = session.query(Rain).filter(func.ST_Contains(func.Geometry(Rain.wkb_geometry),
                                   func.Geometry(func.ST_GeographyFromText(f'POINT({point})'))))
        for i in query_3:
            print(f'Rain at this point is: ' , i.dn, 'mm')
            data['rainfall'] = str(i.dn)


        return Area(data)

    except Exception as e:
        return ErrorModel("Area Not Found")
