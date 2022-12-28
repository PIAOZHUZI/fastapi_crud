import sqlite3
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def db_instance_connect():
    connect = sqlite3.connect("test.db")
    return connect


def db_instance_disconnect(connect):
    connect.close()


def db_instance_createDB(connect):
    cur = connect.cursor()
    cur.execute("create table test ( "
                "idx INTEGER PRIMARY KEY AUTOINCREMENT,",
                "regdate  TEXT not null DEFAULT (datetime('now', 'localtime')),"
                "title text,"
                "body  text)"
                )
    connect.commit()
