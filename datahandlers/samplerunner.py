"""
this is a general module to handle the:
1. json sample data parsed
2. model the parsed json data
3. store fulldata data set into sqllite db
"""

from sqlalchemy import create_engine
from pandas import read_sql_table
import jsonparser
import datamodeler
import storedata

dataFrame=jsonparser.parse_chatevents_jsondata(
    "../sampledata/sample_chat_events.json"
)
dataFrame=datamodeler.model_chatevents_data(dataFrame)

dbname="sqlite:///chatid_sampledb.db"
tablename="sample_chat_events"
storedata.storedataset(
    tablename,
    dataFrame,
    dbName=dbname,
    # ifExists: this is a sample run, will replace with table for every call
    ifExists="replace" 
)

# read the above stored DataFrame table
conn=create_engine(dbname)
samplechatevents_table=read_sql_table(
    tablename,
    conn
)
