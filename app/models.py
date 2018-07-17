# coding: utf-8
from sqlalchemy import ARRAY, Boolean, CheckConstraint, Column, Float, Integer, Numeric, String, Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class Aez(Base):
    __tablename__ = 'aez'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('aez_ogc_fid_seq'::regclass)"))
    kenaez_ = Column(Numeric(11, 0))
    kenaez_id = Column(Numeric(11, 0))
    aezcode = Column(String(14))
    aez_1 = Column(Numeric(11, 1))
    wkb_geometry = Column(Geometry('POLYGON', 4326), index=True)


class Carbon(Base):
    __tablename__ = 'carbon'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('carbon_ogc_fid_seq'::regclass)"))
    prid = Column(String(15))
    totc = Column(Numeric(19, 6))
    x_coord = Column(Numeric(19, 6))
    y_coord = Column(Numeric(19, 6))
    wkb_geometry = Column(Geometry('POLYGON', 32737), index=True)





class Drainage(Base):
    __tablename__ = 'drainage'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('drainage_ogc_fid_seq'::regclass)"))
    area = Column(Numeric(19, 6))
    perimeter = Column(Numeric(19, 6))
    ken2_ = Column(Numeric(11, 0))
    suid = Column(Numeric(11, 0))
    tcdc = Column(String(9))
    scdl = Column(Numeric(5, 0))
    scfm = Column(String(1))
    text = Column(String(1))
    bedr = Column(Numeric(6, 2))
    sdra = Column(String(1))
    tcid = Column(Numeric(1, 0))
    scid = Column(Numeric(1, 0))
    prop = Column(Numeric(3, 0))
    prid = Column(String(12))
    phaq = Column(Numeric(5, 1))
    phkc = Column(Numeric(5, 1))
    exmg = Column(Numeric(5, 1))
    exna = Column(Numeric(5, 1))
    exck = Column(Numeric(5, 1))
    cecs = Column(Numeric(6, 1))
    clay = Column(String(2))
    pdid = Column(String(5))
    drai = Column(String(1))
    drarate = Column(Numeric(1, 0))
    rksc = Column(String(1))
    erty = Column(String(1))
    eraa = Column(String(1))
    erde = Column(String(1))
    scap = Column(String(1))
    rdep = Column(String(1))
    deprate = Column(Numeric(1, 0))
    slop = Column(Numeric(2, 0))
    reli = Column(Numeric(4, 0))
    lndf = Column(String(2))
    rslo = Column(String(2))
    lith = Column(String(3))
    soil = Column(String(16))
    luse = Column(String(3))
    sid = Column(Numeric(4, 0))
    phase = Column(String(6))
    soclss = Column(String(4))
    slope = Column(String(12))
    fert = Column(Numeric(2, 0))
    soilclss = Column(String(24))
    sloprate = Column(Numeric(16, 0))
    acres = Column(Numeric(19, 3))
    hectares = Column(Numeric(19, 3))
    depth = Column(String(254))
    wkb_geometry = Column(Geometry('POLYGON', 32737), index=True)


t_geography_columns = Table(
    'geography_columns', metadata,
    Column('f_table_catalog', String),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geography_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', Text)
)


t_geometry_columns = Table(
    'geometry_columns', metadata,
    Column('f_table_catalog', String(256)),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geometry_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', String(30))
)


class Rain(Base):
    __tablename__ = 'rain'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('rain_ogc_fid_seq'::regclass)"))
    dn = Column(Numeric(9, 0))
    wkb_geometry = Column(Geometry('POLYGON', 4326), index=True)


t_raster_columns = Table(
    'raster_columns', metadata,
    Column('r_table_catalog', String),
    Column('r_table_schema', String),
    Column('r_table_name', String),
    Column('r_raster_column', String),
    Column('srid', Integer),
    Column('scale_x', Float(53)),
    Column('scale_y', Float(53)),
    Column('blocksize_x', Integer),
    Column('blocksize_y', Integer),
    Column('same_alignment', Boolean),
    Column('regular_blocking', Boolean),
    Column('num_bands', Integer),
    Column('pixel_types', ARRAY(Text())),
    Column('nodata_values', ARRAY(Float(precision=53))),
    Column('out_db', Boolean),
    Column('extent', Geometry),
    Column('spatial_index', Boolean)
)


t_raster_overviews = Table(
    'raster_overviews', metadata,
    Column('o_table_catalog', String),
    Column('o_table_schema', String),
    Column('o_table_name', String),
    Column('o_raster_column', String),
    Column('r_table_catalog', String),
    Column('r_table_schema', String),
    Column('r_table_name', String),
    Column('r_raster_column', String),
    Column('overview_factor', Integer)
)


class SoilDepth(Base):
    __tablename__ = 'soil_depth'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('soil_depth_ogc_fid_seq'::regclass)"))
    prid = Column(String(12))
    phkc = Column(Numeric(5, 1))
    drai = Column(String(1))
    soilclss = Column(String(24))
    depth = Column(String(254))
    drainage = Column(Numeric(10, 0))
    drainage_1 = Column(Numeric(3, 0))
    depth_1 = Column(Numeric(11, 1))
    wkb_geometry = Column(Geometry('POLYGON', 32737), index=True)


class SoilPh(Base):
    __tablename__ = 'soil_ph'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('soil_ph_ogc_fid_seq'::regclass)"))
    area = Column(Numeric(13, 6))
    perimeter = Column(Numeric(13, 6))
    ken2_ = Column(Numeric(11, 0))
    suid = Column(Numeric(11, 0))
    phaq = Column(Numeric(4, 1))
    phkc = Column(Numeric(4, 1))
    ph = Column(Numeric(11, 2))
    wkb_geometry = Column(Geometry('POLYGON', 4326), index=True)


class Soil(Base):
    __tablename__ = 'soils'

    ogc_fid = Column(Integer, primary_key=True, server_default=text("nextval('soils_ogc_fid_seq'::regclass)"))
    area = Column(Numeric(33, 31))
    perimeter = Column(Numeric(33, 31))
    ilrifnl_ = Column(Float(53))
    suid = Column(Float(53))
    bedr = Column(Numeric(33, 31))
    sdra = Column(String(254))
    sdra_descr = Column(String(254))
    prop = Column(Numeric(9, 0))
    prid = Column(String(254))
    phaq = Column(Numeric(33, 31))
    phkc = Column(Numeric(33, 31))
    exna = Column(Numeric(33, 31))
    exck = Column(Numeric(33, 31))
    drai = Column(String(254))
    drai_descr = Column(String(254))
    rdep = Column(String(254))
    rdep_descr = Column(String(254))
    lith = Column(String(254))
    slop = Column(Numeric(9, 0))
    reli = Column(Numeric(9, 0))
    soil = Column(String(254))
    sid = Column(Numeric(9, 0))
    clay = Column(String(254))
    clay_descr = Column(String(254))
    text = Column(String(254))
    text_descr = Column(String(254))
    rslo = Column(String(254))
    rslo_descr = Column(String(254))
    lndf = Column(String(254))
    lndf_descr = Column(String(254))
    wkb_geometry = Column(Geometry('POLYGON', 4326), index=True)


class SpatialRefSy(Base):
    __tablename__ = 'spatial_ref_sys'
    __table_args__ = (
        CheckConstraint('(srid > 0) AND (srid <= 998999)'),
    )

    srid = Column(Integer, primary_key=True)
    auth_name = Column(String(256))
    auth_srid = Column(Integer)
    srtext = Column(String(2048))
    proj4text = Column(String(2048))


class Current:
    def __init__(self,data):
        self.time = data.time
        self.summary = data.summary
        self.precipIntensity = data.precipIntensity
        self.precipProbability =  data.precipProbability
        self.temperature = data.temperature
        self.humidity = data.humidity
        self.pressure = data.pressure
        self.windspeed=data.windSpeed
        self.windgust=data.windGust
        self.windbearing = data.windBearing
        self.cloudcover = data.cloudCover



class Area:
    def __init__(self, data):
        self.ph = data['pH']
        self.drainage_desc = data['drainage_desc']
        self.soil_drainage = data['soil drainage']
        self.soil_class = data['soil class']
        self.relief = data['relief']
        self.slope = data['slope']
        self.Aez = data['Aez']
        self.rainfall = data['rainfall']

class ErrorModel:
    def __init__(self,e):
        self.error=e

class Crop(Base):
    __tablename__ = 'crops'

    id = Column(Integer, primary_key=True)
    ph = Column(String)
    temperature = Column(String)
    rainfall = Column(String)
    drainage = Column(String)
    composition = Column(String)
    name = Column(String)

class Cropjson():
    def __init__(self,data):
        self.name=data.name
        self.ph=data.ph
        self.temperature=data.temperature
        self.drainage=data.drainage
        self.composition=data.composition
        self.rainfall=data.rainfall
    def add_comment(self,comment):
        self.comment=comment


