"""
this is a general module to handle the:
1. json sample data parsed
2. model the parsed json data
3. store fulldata data set into sqllite db
"""

from datamodeler import fulldata
from storedata import storedataset

storedataset(
    "sample_chat_events",
    fulldata,
    dbName="chatid_sampledb"
)
