"""
model the dataset

approach:
-split full DataFrame into sub DataFrames
 based on 'room_id' and/or 'jid','nick' ?
-keep entire DataFrame whole

"""

from jsonparser import room_idDf

filterBy_room_id=lambda room_id: (
    room_idDf[room_idDf.index==room_id]
             .sort(["datetime","jid","nick"])
)
# split by room_id: in case data is rendered to UI
# easier for getting specific room_id in respect to user(s)
# and sorted by datetime for ascending/descending call
listof_room_idDfs=[
    filterBy_room_id(room_id)
    for room_id in set(room_idDf.index.values)
]
print len(set(room_idDf.index.values)) # 19
print len(listof_room_idDfs) # 19
