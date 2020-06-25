use timetable;

create table user(
	user_id int primary key,
    username varchar(20) ,
    dept_id int not null,
    yearofstudy varchar(20)
);

insert into user values(1232,'Akber',345,'2nd year MCA');
insert into user values(5652,'Jerin',508,'3nd year IT');
insert into user values(4568,'Deepak',294,'1st  year MECHANICAL');
insert into user values(1093,'Quereshi',430,'4th year BIOTECH.');
insert into user values(5689,'Tarun',508,'2nd year IT');
insert into user values(2017,'Ahmed',123,'3nd year CSE');
insert into user values(8077,'Caesior',654,'1st year CHEMICAL');
insert into user values(6782,'Ravindra',987,'4th year PRODUCTION');
insert into user values(9872,'Rajeev',769,'3nd year EEE');
insert into user values(3421,'Bipinjot',823,'1st year CIVIL');
insert into user values(7612,'Kavya',1092,'2nd year ECE');
insert into user values(12345,'Saket',1895,'1st year MBA');
insert into user values(34526,'Pranav',1362,'PG');



create table coursedetails(
	course_id int not null,
    dept_id  int not null,
    course varchar(20)
);

insert into coursedetails values(91820,345,'MCA');
insert into coursedetails values(11801,508,'B.E');
insert into coursedetails values(11801,294,'B.E');
insert into coursedetails values(11801,430,'B.E');
insert into coursedetails values(11801,508,'B.E');
insert into coursedetails values(11801,123,'B.E');
insert into coursedetails values(11801,654,'B.E');
insert into coursedetails values(11801,987,'B.E');
insert into coursedetails values(11801,769,'B.E');
insert into coursedetails values(11801,823,'B.E');
insert into coursedetails values(11801,1092,'B.E');
insert into coursedetails values(51980,1362,'PG');
insert into coursedetails values(42923,1895,'MBA');

    
