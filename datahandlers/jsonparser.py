"""
parse the json dataset

approach: 
1. use pandas to parse json data
2. pandas DataFrame to get full aggregated dataset

"""

import pandas as pd
from mappings import maphandler
import logging

fulldata=pd.io.json.read_json(
    "../sampledata/sample_chat_events.json"
) # [340 rows x 12 columns]


colsToMap=["room_id","jid"]
for colname in colsToMap:
    mappingsdict=maphandler.setmappings(
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

# set 'room_id' column name as the index column
room_idDf=fulldata.set_index(["room_id"])
room_idDf.index.name="room_id"
