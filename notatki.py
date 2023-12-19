import random
from faker import Faker
from random import uniform
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

########################################################CREATE/insert

Session=sqlalchemy.orm.sessionmaker(bind=engine)
session=Session()
#
# lista_userow:list=[]
#
# fake = Faker()
#
# for item in range(10_000):
#     lista_userow.append(User(
#     name=fake.name(),
#     location=f'POINT({random.uniform(14,24)} {random.uniform(49,55)})'
# ))
# session.add_all(lista_userow)
# session.commit()
##############################################################################READ/select

users_from_db=session.query(User).all()
# users_from_db=session.query(User).filter(User.name=='')
for user in users_from_db:
    if user.name=="Amy Long":
        user.name="John Weak"
    print(user.name)
# for user in users_from_db:
#     if user.name=="John Weak":
#         user.delete()                      ########delete nie działa trzeeba to zastąpić
#     print(user.name)

session.commit()

session.flush()
connection.close()
engine.dispose()