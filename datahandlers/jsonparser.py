"""
parse the json dataset

approach: 
1. use pandas to parse json data
2. pandas DataFrame to get full aggregated dataset

"""

import pandas as pd

fulldata=pd.io.json.read_json(
    "../sampledata/sample_chat_events.json"
) # [340 rows x 12 columns]

# set 'room_id' column name as the index column
room_idDf=fulldata.set_index(["room_id"])
room_idDf.index.name="room_id"
