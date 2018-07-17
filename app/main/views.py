from flask import render_template,request,redirect,url_for,abort
from . import main
import json
from ..request_data import get_daily_data
from ..queries import query_area,get_crops

# Views
@main.route('/weather/', methods=["GET"])
def index():
    res=request.args.to_dict()
    town=(float(res['lat']),float(res['long']))
    point="{} {}".format(str(res['long']),str(res['lat']))
    area_data=query_area(point)
    area_final=json.dumps(area_data.__dict__)

    weather_data= get_daily_data(town)

    weather_final=json.dumps(weather_data.__dict__)
    crops_data=get_crops(weather_data.temperature,area_data.ph,area_data.drainage_desc)
    crops_final=json.dumps([i.__dict__ for i in crops_data])

    return crops_final

@main.route('/weather_data/')
def weather():
    res=request.args.to_dict()
    town=(float(res['lat']),float(res['long']))
    weather_data= get_daily_data(town)
    weather_final=json.dumps(weather_data.__dict__)
    return weather_final

@main.route('/area_data/')
def area():
    res=request.args.to_dict()
    point="{} {}".format(str(res['long']),str(res['lat']))
    area_data=query_area(point)
    area_final=json.dumps(area_data.__dict__)
    return area_final

@main.route('/')
def landing():
    return render_template('index.html')

@main.route('/data', methods=['GET','POST'])
def data():
    if request.method == "POST":
        print(request.get_json())
        data2="{} {}".format(request.get_json().get('lat'), request.get_json().get('lng'))
        res=query_area(data2)
        print(res)
    return render_template('index.html')

