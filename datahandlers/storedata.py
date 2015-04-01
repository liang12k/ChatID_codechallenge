"""
store the data set(s)

approach:
-use sqlite db to store into local dir
-pandas to put datasets into db
 http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.to_sql.html
"""

import pandas as pd
from datamodeler import * ### # IMPROVE this
import sqlite3

conn=sqlite3.connect("chatid_sampledb.db")
conn.close()
