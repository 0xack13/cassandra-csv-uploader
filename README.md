# cassandra-csv-uploader
Python uploader to Cassandra Keyspace Table

`nodetool enablethrift`

```
CREATE KEYSPAEC inquirykeyspace
   WITH REPLICATION = { 
   'class' : 'SimpleStrategy', 
   'replication_factor' : 1 
};
```

`create table supportticket (id text primary key, name text, class text) with compact storage;`

`use inquirykeyspace`

