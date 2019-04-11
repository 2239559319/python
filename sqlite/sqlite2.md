### 数据库操作

------------------

- 创建一个新的数据库 
```bash
sqlite3 DatabaseName.db
```

- .dump 命令
您可以在命令提示符中使用 SQLite .dump 点命令来导出完整的数据库在一个文本文件中，如下所示：
```bash
sqlite3 test.db .dump > test.sql
```

- 您可以通过简单的方式从生成的 testDB.sql 恢复，如下所示：
```bash
sqlite3 testDB.db < testDB.sql
```

- 假设这样一种情况，当在同一时间有多个数据库可用，您想使用其中的任何一个。SQLite 的 ATTACH DATABASE 语句是用来选择一个特定的数据库，使用该命令后，所有的 SQLite 语句将在附加的数据库下执行
```sqlite
attach database 'test.db' as 'tset';
--用.database来查看数据库
```

- SQLite 分离数据库
SQLite的 DETACH DTABASE 语句是用来把命名数据库从一个数据库连接分离和游离出来，连接是之前使用 ATTACH 语句附加的。如果同一个数据库文件已经被附加上多个别名，DETACH 命令将只断开给定名称的连接，而其余的仍然有效。您无法分离 main 或 temp 数据库。
```sqlite
detach database 'test';
```