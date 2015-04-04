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

def getmapper(colName=""):
    """
        :param str colName: column name to map to int value
        :return dict: the current mapping or blank if column name is unavailable
    """
    mappingdict={}
    try:
        with open(colName+".txt","r") as f:
            colmappings=f.read()
            if colmappings:
                mappingdict=ast.literal_eval(colmappings)
    except IOError as excp:
        pass # if file doesn't exist, logging.error message will notify
    if not mappingdict:
        logging.error("\nmapping for column name '%s' is unavailable\n",colName)
    return mappingdict

def setmappings(colName="",colValsAsList=[]):
    """
        :param str colName: column name to create mapping for in a .txt file
        :param list colValsAsList: the column values as a dict where key
    """
    if not (colName and colValsAsList): return
    colmappings=getmapper(colName)
    # get set differences, any remaining values will need to be mapped
    colValsAsList=set(colValsAsList)-set(colmappings.keys())
    for colval in colValsAsList:
        # give column value mapping number of len(current_mappings)
        # since the first mapping number is 0
        colmappings[colval]=len(colmappings)
    mappingfile=open(colName+".txt","ab+")
    pickle.dump(colmappings,mappingfile)
    mappingfile.close()
    logging.info("\nsuccessfully created mappings for '%s' in mapping file: '%s.txt'", colName,colName)
