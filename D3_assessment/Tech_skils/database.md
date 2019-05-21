# Database

## Expectation
The Developer knows how to optimize database queries using indexes, partitioning, striping and clustering.

## Justification

### Database index
A database index is a data structure that improves the speed of data retrieval operations on a database table at the cost of additional writes and storage space to maintain the index data structure.  Indexes are used to quickly locate data without having to search every row in a database table every time a database table is accessed. An index column can be created using one or more columns in a database table.

An index table consist of two fields:
- Search key (any column from the DB table)
- Low-level disk block address or direct link to the complete row of data it was copied from.

### Database partitioning
Database partitioning is the process where very large tables are divided into multiple smaller parts. By splitting a large table into smaller, individual tables, queries that access only a fraction of the data can run faster because there are fewer data to scan. The goal of partitioning is to aid in the maintenance of large tables and to reduce the overall response time to read and load data for particular SQL operations.

Two types of partitioning are:
- Horizontal partitioning (sharding): It involves putting different rows into different tables.
- Vertical partitioning involves creating tables with fewer columns and using additional tables to store the remaining columns

### Data striping
Data striping is a technique for spreading data over multiple disk drives. Data striping can speed up operations that retrieve data from disk storage. The computer system breaks a body of data into units and spreads these units across the available disks.
Striping is useful when a processing device requests data more quickly than a single storage device can provide it. By spreading segments across multiple devices which can be accessed concurrently, total data throughput is increased. It is also a useful method for balancing I/O load across an array of disks. 
The con here is, because different segments of data are kept on different storage devices, the failure of one device causes the corruption of the full data sequence.

### Database clustering
A database cluster basically means more than one database working together. They cluster together to provide a service. There are a few standard setups based on your needs:

#### Master/slave replication.
The antiquated term aside, it basically means that you have one server with the truth, the master, and the slaves just copies anything the master does. This means that in setups that have many read requests and not so many write requests, you can read data from any of the slaves and if you want to write then you do it to the master. Any changes are then propagated to the slaves. This is a good setup for heavy read traffic.

#### Master/master replication
Sometimes clustering is more about data security. That means that data need to exists on more than one server, to be reasonably sure that it won't disappear by way of a server crash. So a master/master replication means that two or more servers mirror each other.

#### Distributed data
Sometimes there's simply too much data for it to fit on one server. Then you have to distribute the data to many different servers, that each holds a portion of the data and a map on where to find the other data. This is the paradigm that many NoSQL databases uses. Divide and conquer.


Clustering offers two major advantages:

- Fault tolerance: Because there is more than one server or instance for users to connect to, clustering offers an alternative, in the event of individual server failure.
- Load balancing: The clustering feature is usually set up to allow users to be automatically allocated to the server with the least load
