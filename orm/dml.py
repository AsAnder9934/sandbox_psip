import os
import sqlalchemy, sqlalchemy.orm, sqlalchemy.orm.session
from dotenv import load_dotenv
import geoalchemy2
load_dotenv()

db_params=sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    database=os.getenv('POSTGRES_DB'),
    port=os.getenv('POSTGRES_PORT')
)

engine=sqlalchemy.create_engine(db_params)
connection=engine.connect()
base=sqlalchemy.orm.declarative_base()

class User(base):
    __tablename__='mm_table'

    id=sqlalchemy.Column(sqlalchemy.Integer(),primary_key=True) #typ serial (sam będzie odliczał)
    name=sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    location=sqlalchemy.Column('geom', geoalchemy2.Geometry(geometry_type='POINT',srid=4326),nullable=True)

base.metadata.create_all(engine)

connection.close()
engine.dispose()