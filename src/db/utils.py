import datetime
from peewee import *

from src.db.database import *

def create_user(id: int, username: str, first_name: str, last_name: str, chat_id: int) -> None:
  User.create(id=id, username=username, first_name=first_name, last_name=last_name, chat_id=chat_id, reg_date=datetime.datetime.utcnow())

def create_test(user_id: int, ext_result: float, est_result: float, agr_result: float, csn_result: float, opn_result: float) -> None:
  user = User.get(User.id == user_id)
  Test.create(user=user, ext_result=ext_result, est_result=est_result, agr_result=agr_result, csn_result=csn_result, opn_result=opn_result, date=datetime.datetime.utcnow())
  
def user_exists(user_id: int) -> bool:
  try:
    User.get_by_id(user_id)
    return True
  except DoesNotExist:
    return False
