"""
approach: 
1. use pandas to parse json data
2. pandas DataFrame to get full aggregated dataset
3. split full DataFrame into sub DataFrames based on 'room_id'

ideas (?):
-also split by user ('jid') and/or name ('nick')
"""

import pandas as pd

fulldata=pd.io.json.read_json(
    "../sampledata/sample_chat_events.json"
) # [340 rows x 12 columns]

# set 'room_id' column name as the index column
room_idDf=fulldata.set_index(["room_id"])
room_idDf.index.name="room_id"
listof_room_idDfs=[
    room_idDf[room_idDf.index==room_id]
    for room_id in set(room_idDf.index.values)
]
print len(set(room_idDf.index.values)) # 19
print len(listof_room_idDfs) # 19
