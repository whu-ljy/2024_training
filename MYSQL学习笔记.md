# MySQL
由于MySQL我有系统的学习过 这里只是简单复习了一下 没有进行过多的练习
![image](https://user-images.githubusercontent.com/71172395/125794610-c70f39a3-dc19-41b8-b1a1-01523df03ff2.png)
| 作用 | 命令 | 备注 |
| ---- | ---- | ---- |
| 连接到MySQL数据库 | `mysql -u 用户名 -p` | |
| 选择数据库 | `USE 数据库名;` | |
| 显示所有数据库 | `SHOW DATABASES;` | |
| 创建数据库 | `CREATE DATABASE 数据库名;` | |
| 删除数据库 | `DROP DATABASE 数据库名;` | |
| 显示所有表 | `SHOW TABLES;` | |
| 创建表 | `CREATE TABLE 表名 (列名1 数据类型, 列名2 数据类型, ...);` | |
| 删除表 | `DROP TABLE 表名;` | |
| 查看表结构 | `DESCRIBE 表名;` | |
| 插入数据 | `INSERT INTO 表名 (列1, 列2, ...) VALUES (值1, 值2, ...);` | |
| 查询数据 | `SELECT 列名 FROM 表名 WHERE 条件;` | |
| 更新数据 | `UPDATE 表名 SET 列名 = 新值 WHERE 条件;` | |
| 删除数据 | `DELETE FROM 表名 WHERE 条件;` | |
| 添加列 | `ALTER TABLE 表名 ADD 列名 数据类型;` | |
| 删除列 | `ALTER TABLE 表名 DROP 列名;` | |
| 修改列类型 | `ALTER TABLE 表名 MODIFY 列名 新数据类型;` | |
| 重命名表 | `ALTER TABLE 表名 RENAME TO 新表名;` | |
| 创建索引 | `CREATE INDEX 索引名 ON 表名 (列名);` | |
| 删除索引 | `DROP INDEX 索引名 ON 表名;` | |
