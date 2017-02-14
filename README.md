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

Now, to the run the python uploader script:
`python cassandraCsvUploader.py`

Another way to upload the CSV file is to use the `copy` command in the CQLSH:

`COPY inquirykeyspace.supportticket (id, name, class) FROM 'data.csv';`
