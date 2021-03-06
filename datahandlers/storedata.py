"""
store the data set(s)

approach:
-use sqlite db to store into local dir
-pandas to put datasets into db
 http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.to_sql.html
"""

import pandas as pd
from sqlalchemy import create_engine

def storedataset(
        tableName,
        dataFrame,
        dbName="",
        createNewDb=False,
        ifExists="fail",
        chunkSize=None,
    ):
    """
        store dataset into sqllite db based on dbName

        :param str tableName: table name to write dataset into db
        :param pandas.DataFrame dataFrame: dataset as DataFrame
        :param str dbName: database name str recognizable by sqlalchemy.create_engine
        :param bool createNewDb: bool to create new db
        :param str ifExists: (same as pandas.DataFrame.to_sql arg)
                             {'fail', 'replace', 'append'}
                             fail: If table exists, do nothing.
                             replace: If table exists, drop it, recreate it, and insert data.
                             append: If table exists, insert data. Create if does not exist.
        :param int chunkSize: (same as pandas.DataFrame.to_sql arg) 
                              If not None, then rows will be written in batches of this size at a time. 
                              If None, all rows will be written at once.
    """
    conn=create_engine(dbName)
    dataFrame.to_sql(
        tableName,
        conn,
        if_exists=ifExists,
        chunksize=chunkSize,
    )
