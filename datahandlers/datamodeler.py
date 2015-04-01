"""
model the dataset

approach:
-split full DataFrame into sub DataFrames
 based on 'room_id' and/or 'jid','nick' ?
-keep entire DataFrame whole

"""

from jsonparser import room_idDf

listof_room_idDfs=[
    room_idDf[room_idDf.index==room_id]
    for room_id in set(room_idDf.index.values)
]
print len(set(room_idDf.index.values)) # 19
print len(listof_room_idDfs) # 19
