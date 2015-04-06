"""
model the dataset

approach:
-split full DataFrame into sub DataFrames
 based on 'room_id' and/or 'jid','nick' ?
-keep entire DataFrame whole

"""

def model_chatevents_data(dataFrame):
    """
        models the dataFrame (currently for chat events)
        
        :type dataFrame: pandas.DataFrame
        :return: modeled DataFrame
    """
    # create 'row_index' column to log the current index
    # value of read data; goal is to have a 'track' of
    # dataset if it gets partitioned into multiple dbs
    dataFrame["row_index"]=dataFrame.index.values
    return dataFrame

    '''
    ### # TODO ?
    normalize the dataframe by 'room_id' column
    returning a list of dataframes groupedby 'room_id' unique value
    -this is primarily for UI related
     ex: user wants to see 1 specific room_id value, this individual dataframe
         can be easily grabbed
    
    ### # not sure if this is needed
    # # set 'room_id' column name as the index column
    room_idDf=fulldata.set_index(["room_id"])
    room_idDf.index.name="room_id"
    
    # **note:
    # room_idDf 'room_id','jid' column values
    # are replaced by number mappings
    # not sure if the below splitting in 'room_id'
    # normalization is needed ??
    
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
    '''