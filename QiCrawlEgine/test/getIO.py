import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Handler.dbClient import MysqlDB

# aa = MysqlDB()
# sql_test = 'select * from spiderinfo where id={}'.format(str(1))
# print(aa.select_(sql_test))

sql_test = 'select * from spiderinfo where id={}'.format(str(1))
print(MysqlDB().select_(sql_test))