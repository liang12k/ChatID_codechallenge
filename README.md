# ChatID_codechallenge
ChatID code challenge (Q1/2015) - parse, model, store sample JSON data set

Challenge Intro
---------------
Part of our role in the ChatID platform involves turning chat server logs into structured data for other applications like analysis and reporting. Our chat system runs on XMPP, “the Extensible Messaging and Presence Protocol”, “an open technology for real-time communication”  for chat messaging. Chats consist of users exchanging presences ("here I am", "now I'm gone") and messages. These are encoded in XML and have various elements besides the message body that specify interesting things (like the chatstate of "typing"). Chat participants have nicknames (nick) as well. For more on multi user chat, see http://xmpp.org/extensions/xep-0045.html.

Tips:
-----
To grease the wheels of working with XML:

from lxml import etree
stanza = etree.fromstring(event['stanza'])
stanza.find('body')

We use SQLAlchemy to model data and interact with SQL databases. Using a SQLite database would be the quickest way to get started because it doesn’t require running a server. 

Goal:
-----
The goal of the exercise is to see you parse, model, and store some sample event logs in a useful way. Attached is a JSON representation of a collection of log events. Each of these would be correspond to an event occurring in the chat server. The XML of the event is in the stanza field, while the other fields give metadata about the event. One logical way to group these is by the room_id field. Assume that these logs will always be processed as batches, so you needn’t work out a streaming-ready data model.

Expected completion time:
-------------------------
estimate about 2-4 hours invested, with no need to go over 6 hours unless you think it will significantly improve your submission.

Notes:
------
This isn't intended to be more than a couple hours of work, so leaving TODO comments on things you didn't take time to implement is encouraged.
We also encourage you to obey PEP8 and PEP20.

--------------
April 22, 2015

questions asked:
-get distinct count of room_id
-get count of events (id col) in each room_id
- ^ follow up: get average of events (id col)
-do a groupby of room_id

feedback:
-mapping room_id strings is excessive, no need

ideas:
-create table for room_id mappings
 >currently have a dict to map room_id -> int val
 >need to get a reverse of int val -> room_id
  this can use the AUTO_INCREMENT feature in sql
  (see datahandler.mappings.maphandler)
-alternative modeling of data
 >1-to-many relationship of csid to jid
-handling transactions and LOCK the sql tables when
 multiple threads are editing to prevent duplication