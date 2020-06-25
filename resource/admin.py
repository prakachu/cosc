from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from db import query

class Admin(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('user_id',type=int,required=True,help='user_id cannot be blank')
        data=parser.parse_args()
        try:
            return query(f"""SELECT * FROM timetable.user WHERE user_id={data['user_id']};""")
        except:
            return{"message":"there is an error connecting to user table."},500

class Admins():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    @classmethod
    def getAdmin(cls,username):
        result=query(f""" SELECT username,password FROM user WHERE username='{username}'""",return_json=False)
        if len(result)>0: return Admins(result[0]['username'],result[0]['password'])
        return None
    #@classmethod
    #def getAdminByUsername(cls,username):
     #   result=query(f""" SELECT user_id,username,password FROM user WHERE user_id='{user_id}'""",return_json=False)
      #  if len(result)>0: return Users(result[0]['user_id'],result[0]['username'],result[0]['password'])
       # return None


class Adminlogin(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('username',type=str,required=True,help="username cannot be left blank")
        parser.add_argument('password',type=str,required=True,help="password cannot be left blank")
        data=parser.parse_args()
        admins=Admins.getAdmin(data['username'])
        if Admins and safe_str_cmp(admins.password,data['password']):
            access_token=create_access_token(identity=users.username,expires_delta=False)
            return {'access_token':access_token},200
        return {"message":"Invalid Credentials"},401

