from DBUtil import DBUtil

class Service:
  def login(self, uname, password):
    sql = 'select * from t_user where uname=%s and password=%s'
    if DBUtil().queryOne(sql, uname, password):
      return True
    else:
      return False