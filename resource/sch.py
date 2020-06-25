from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from db import query
from datetime import time,date,datetime

class Sch(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('faculty_id',type=int,required=True,help='user_id cannot be blank')
        parser.add_argument('sched_id',type=int,required=True,help='sched_id cannot be blank')
        parser.add_argument('day_id',type=int,required=True,help='year cannot be blank')
        parser.add_argument('p_1',type=int,required=True,help='p_1 cannot be blank')
        parser.add_argument('p_2',type=int,required=True,help='p_2 cannot be blank')
        parser.add_argument('p_3',type=int,required=True,help='p_3 cannot be blank')
        parser.add_argument('p_4',type=int,required=True,help='p_4 cannot be blank')
        parser.add_argument('p_5',type=int,required=True,help='p_5 cannot be blank')
        parser.add_argument('p_6',type=int,required=True,help='p_6 cannot be blank')
        data=parser.parse_args()
        try:
            return query(f"""SELECT * FROM timetable.user WHERE user_id={data['user_id']};""")
        except:
            return{"message":"there is an error connecting to user table."},500

    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('faculty_id',type=int,required=True,help='user_id cannot be blank')
        parser.add_argument('sched_id',type=int,required=True,help='sched_id cannot be blank')
        parser.add_argument('day_id',type=int,required=True,help='year cannot be blank')
        parser.add_argument('p_1',type=int,required=True,help='p_1 cannot be blank')
        parser.add_argument('p_2',type=int,required=True,help='p_2 cannot be blank')
        parser.add_argument('p_3',type=int,required=True,help='p_3 cannot be blank')
        parser.add_argument('p_4',type=int,required=True,help='p_4 cannot be blank')
        parser.add_argument('p_5',type=int,required=True,help='p_5 cannot be blank')
        parser.add_argument('p_6',type=int,required=True,help='p_6 cannot be blank')
        data=parser.parse_args()
        try:
            query(f"""INSERT INTO timetable.user VALUES({data['faculty_id']},
                                                        {data['sched_id']},
                                                        {data['day_id']},
                                                        {data['p_1']},
                                                        {data['p_2']},
                                                        {data['p_3']},
                                                        {data['p_4']},
                                                        {data['p_5']},
                                                        {data['p_6']}) """)
        except:
            return{"message":"There is an error connecting to the usertable"},500
        return {"message":"Sucessfully inserted"},201
    

class Sch():
    def __init__(self,faculty_id,sched_id, day_id,p_1,p_2,p_3,p_4,p_5,p_6):
        self.faculty_id=faculty_id
        self.sched_id=sched_id
        self.day_id=day_id
        self.p_1=p_1
        self.p_2=p_2
        self.p_3=p_3
        self.p_4=p_4
        self.p_5=p_5
        self.p_6=p_6
    @classmethod
    def getAvailablity(faculty_id):
        now=datetime.now()
        today=date.today()
        currentHour=a.hour
        currentPeriod=getPerioud(currentHour)
        #currentDay=getDay()
        result=query(f""" SELECT p_{currentPeriod} FROM sch WHERE faculty_id='{faculty_id} and day_id='""",return_json=False)
        #query to give the particular availability
        return None

    def getPeriod(currentHour):
        if currentHour=9:
            return '1'
        elif currentHour=10:
            return '2'
        elif currentHour=11:
            return '3'
        elif currentHour=13:
            return '4'
        elif currentHour=14:
            return '5'
        elif currentHour=15:
            return '6'
       
        