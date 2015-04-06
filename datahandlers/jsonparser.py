"""
parse the json dataset

approach: 
1. use pandas to parse json data
2. pandas DataFrame to get full aggregated dataset
3. append the row index as an addt'l column of values
   as a point of referral in case dataset gets
   partitioned into multiple dbs
"""

import pandas as pd
from mappings import maphandler
import logging

fulldata=pd.io.json.read_json(
    "../sampledata/sample_chat_events.json"
) # [340 rows x 12 columns]

colsToMap=["room_id","jid"]
for colname in colsToMap:
    mappingsdict=maphandler.setColumnMappings(
        colname,
        fulldata[colname].tolist()
    )
    fulldata[colname]=fulldata.apply(
        lambda row: mappingsdict.get(row[colname]),
        axis=1  
    )
    logging.info(
        "%s:\nvalues:\n%s",
        colname,str(set(fulldata[colname].values))
    )
# set the 'meta' column to dtype str
# **note: when reading extracted data from sqllite,
#         need to do an ast.literal_eval on it to get
#         back the dict object
# fulldata["meta"]=fulldata["meta"].astype(str)
fulldata=maphandler.doSchemaMappings(
    fulldata,
    "events"
)

# set 'room_id' column name as the index column
room_idDf=fulldata.set_index(["room_id"])
room_idDf.index.name="room_id"
