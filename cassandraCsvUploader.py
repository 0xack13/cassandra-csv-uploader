# create table supportticket (id text primary key, name text, class text) with compact storage;
# nodetool enablethrift
# use inquirykeyspace
#  create keyspace inquirykeyspace
#  WITH REPLICATION = { 
#   'class' : 'SimpleStrategy', 
#   'replication_factor' : 1 
#  };

import csv
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('inquirykeyspace', ['localhost:9160'])
cf = ColumnFamily(pool, "supportticket")

with open('data.csv', 'rb') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print str(row)
    key = row['id']
    del row['id']
    cf.insert(key, row)

pool.dispose()