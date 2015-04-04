"""
this module is to handle getting mapping values
for specific key name

currently handling:
room_id
jid
"""

import ast
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
