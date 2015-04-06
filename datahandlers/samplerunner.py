"""
this is a general module to handle the:
1. json sample data parsed
2. model the parsed json data
3. store fulldata data set into sqllite db
"""

from sqlalchemy import create_engine
from pandas import read_sql_table
from datamodeler import fulldata
from storedata import storedataset

dbname="sqlite:///chatid_sampledb.db"
tablename="sample_chat_events"

storedataset(
    tablename,
    fulldata,
    dbName=dbname,
    # ifExists: this is a sample run, will replace with table for every call
    ifExists="replace" 
)

conn=create_engine(dbname)
samplechatevents_table=read_sql_table(
    tablename,
    conn
)
