from decouple import config
from peewee import *

db_config = {
  'user': config('DB_USER'),
  'password': config('DB_PWD'),
  'host': config('DB_HOST'),
  'database': config('DB'),
}

db = MySQLDatabase(**db_config)

class BaseModel(Model):
  class Meta:
    database = db
    
class User(BaseModel):
  id = BigAutoField(unique=True)
  username = CharField(null=True)
  first_name = CharField()
  last_name = CharField(null=True)
  chat_id = BigIntegerField()
  reg_date = DateField()
  
  class Meta: 
    table_name = 'User'

class Test(BaseModel):
  user = ForeignKeyField(User)
  ext_result = FloatField()
  est_result = FloatField()
  agr_result = FloatField()
  csn_result = FloatField()
  opn_result = FloatField()
  date = DateField()
  
  class Meta:
    table_name = 'Test'

# Create Tables
with db:
  db.create_tables([User, Test], safe=True)

db.close()