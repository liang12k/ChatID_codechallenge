"""
this module is to handle getting mapping values
for specific key name

currently handling:
room_id
jid
"""

import ast
import pickle
import logging
from events_schema import EVENTS_SCHEMA

def getColumnMappings(colName="",reverseMapping=False):
    """
        :param str colName: column name to map to int value
        :param bool reverseMapping: if True, the mapped values (dict.values) 
                                    become the key as it's unique
                                    default as False to take column's values as keys
                                    this will affect the return dict key-value pairings
        :return dict: the current mapping or blank if column name is unavailable
    """
    mappingdict={}
    try:
        with open("./"+colName+".txt","r") as f:
            mappingdict=pickle.load(f)
    except IOError as excp:
        mappingdict={} # if file doesn't exist, logging.error message will notify
    if not (mappingdict and isinstance(mappingdict,dict)):
        logging.error("\nmapping for column name '%s' is unavailable\n",colName)
    if reverseMapping and mappingdict:
        # perform reverse mapping where values become keys and visa versa
        # all values are unique int values (similar to sql's AUTO_INCREMENT)
        mappingdict=dict((value, key) for key, value in mappingdict.iteritems())
    return mappingdict

def setColumnMappings(colName="",colValsAsList=[]):
    """
        :param str colName: column name to create mapping for in a .txt file
        :param list colValsAsList: the column values as a dict where key
        :return dict: dict of column values number mappings
    """
    if not (colName and colValsAsList):
        logging.warning(
            "\nneed column name and list of its values\nentered: '%s','%s'\n",
            str(colName),str(colValsAsList)
        ); return
    colmappings=getColumnMappings(colName)
    # get set differences, any remaining values will need to be mapped
    colValsAsList=set(colValsAsList)-set(colmappings.keys())
    for colval in colValsAsList:
        # give column value mapping number of len(current_mappings)
        # since the first mapping number is 0
        colmappings[colval]=len(colmappings)
    mappingfile=open("./"+colName+".txt","ab+")
    pickle.dump(colmappings,mappingfile)
    mappingfile.close()
    logging.info(
        "\nsuccessfully created mappings for '%s' in mapping file: '%s.txt'",
        colName,colName
    )
    return colmappings

def doSchemaMappings(dataFrame,typeOfData=""):
    """
        if schema mappings are available, convert schema
    
        :type pandas.DataFrame: dataFrame
        :param str typeOfData: indicates which schema to get, if available
                               (ie: 'events' gets events data schema mappings)
        :return pandas.DataFrame: DataFrame with new mapped schema, if available
    """
    schemamappings={
        "events" : EVENTS_SCHEMA
    }
    schemamaps=schemamappings.get(typeOfData)
    if not schemamaps:
        logging.info(
            "\nno such schema mapping available for '%s'\n",
            typeOfData
        )
    else:
        # find the column names to map to
        # new schema type
        colsToMap=list(
            (set(dataFrame.columns.values).intersection(
                set(schemamaps.keys())))
        )
        for colname in colsToMap:
            newdtype=schemamaps.get(colname)
            dataFrame[colname]=dataFrame[colname].astype(newdtype)
            logging.info(
                "\nconverted '%s' to type '%s'\n",
                colname, newdtype
            )
    return dataFrame
