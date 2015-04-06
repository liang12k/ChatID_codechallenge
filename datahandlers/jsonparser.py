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

def parse_chatevents_jsondata(filePath):
    """
        gets chat events json data and converts it
        into a pandas DataFrame
    
        :param str filePath: path to json data file
        :return: pandas.DataFrame
    """
    fulldata=pd.io.json.read_json(filePath)
    
    # handling the 'sample_chat_events.json' file
    # with 'room_id','jid' columns
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
    # if schema conversion is needed, do so
    fulldata=maphandler.doSchemaMappings(
        fulldata,
        "events"
    )
    return fulldata
