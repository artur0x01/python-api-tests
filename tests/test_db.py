import structlog
from generic.helpers.dm_db import DmDatabase
from sqlalchemy import create_engine, text, Column, String, Boolean, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    UserId = Column(UUID, primary_key=True)
    Login = Column(String(100))
    Email = Column(String(100))
    Name = Column(String(100))
    Activated = Column(Boolean, nullable=False)


def test_orm():
    user = 'postgres'
    password = 'admin'
    host = '5.63.153.31'
    database = 'dm3.5'
    connection_string = f"postgresql://{user}:{password}@{host}/{database}"
    isolation_level = 'AUTOCOMMIT'
    db = create_engine(connection_string, isolation_level=isolation_level)
    connect = db.connect()
    query = select([User]).where(
        User.Login == 'here_2075'
    )
    print()
    print(query)
    dataset = connect.execute(query)
    for row in dataset:
        print(dict(row))
    # dataset = connect.execute(text('select * from "public"."Users"'))
    # for i in dataset:
    #     print(dict(i))

# def test_db():
# db = DmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
# db.get_all_users()
