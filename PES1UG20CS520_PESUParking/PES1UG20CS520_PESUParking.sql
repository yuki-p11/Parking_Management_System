----------------------------------------------CREATE DATABASE pesu_parking_vehicle---------------------------------------------------------
CREATE DATABASE pesu_parking_vehicle;
USE pesu_parking_vehicle;
-------------------------------------------------create tables-------------------------------------------------------------------------------------------
CREATE TABLE  Vehicle_in(Date DATE, Type TEXT NOT NULL, Owner_type TEXT NOT NULL, Vehicle_no varchar(50) NOT NULL, P_id varchar(2) NOT NULL,ID varchar(13) NOT NULL,PRIMARY KEY(ID),FOREIGN KEY(P_id) REFERENCES parking_space(Parking_id));

CREATE TABLE  student(Contact varchar(10) NOT NULL, ID varchar(13) NOT NULL, Name varchar(50) NOT NULL, Semester INT CHECK (Semester>0 AND Semester<9),PRIMARY KEY(ID),UNIQUE(Name));

CREATE TABLE  faculty(Contact varchar(10) NOT NULL, ID varchar(13) NOT NULL, Name varchar(50) NOT NULL,PRIMARY KEY(ID));

CREATE TABLE  parking_space(Parking_id varchar(2) NOT NULL, Status TEXT DEFAULT 'Active',PRIMARY KEY(Parking_id));
---------------------------------------------------Insert values----------------------------------------------------------------------------------

--------------------student
INSERT INTO student(Contact, ID , Name , Semester) VALUES ("9980674593","PES1UG20CS524","Srujana golla","5");
INSERT INTO student(Contact, ID , Name , Semester) VALUES (	"9874562341","PES1UG20CS540","Baddela Divya","5");
INSERT INTO student(Contact, ID , Name , Semester) VALUES ("9632687172","PES1UG20CS520","Yuktha Poral","5");
INSERT INTO student(Contact, ID , Name , Semester) VALUES ("9443215678","PES1UG20CS553","Alwin Joseph","5");
INSERT INTO student(Contact, ID , Name , Semester) VALUES ("9089786756","PES1UG20CS550","Ganesh Revanth","5");

---------------------faculty
INSERT INTO faculty(Contact , ID , Name ) VALUES ("9980764324","PES1EICS100","Nagasundhari");
INSERT INTO faculty(Contact , ID , Name ) VALUES ("9900112233","PES1EICS101","Sivagamasundhari");
INSERT INTO faculty(Contact , ID , Name ) VALUES ("9988776655","PES1EICS102","Arun Vikas");
INSERT INTO faculty(Contact , ID , Name ) VALUES ("9977668855","PES1EICS103","Likitha M");
INSERT INTO faculty(Contact , ID , Name ) VALUES ("9955667744","PES1EICS104","Teja Bhat");

---------------------parking_space
INSERT INTO parking_space(Parking_id, Status) VALUES ('A1', 'Active');
INSERT INTO parking_space(Parking_id, Status) VALUES ('A2', 'Active');
INSERT INTO parking_space(Parking_id, Status) VALUES ('A3', 'Active');
INSERT INTO parking_space(Parking_id, Status) VALUES ('A4', 'Active');
INSERT INTO parking_space(Parking_id, Status) VALUES ('A5', 'Active');
INSERT INTO parking_space(Parking_id, Status) VALUES ('A6', 'Active');
INSERT INTO parking_space(Parking_id, Status) VALUES ('A7', 'Active');
INSERT INTO parking_space(Parking_id, Status) VALUES ('A8', 'Active');


------------------------------------------procedure---------------------------------------------------
DELIMITER //
CREATE PROCEDURE StatusUpdation ( IN parking_id VARCHAR(2))
BEGIN
UPDATE parking_space SET Status="Occupied" where parking_space.Parking_id = parking_id ;
END;
//
Delimiter ;


------------------------------------------Trigger-----------------------------------------------------
DELIMITER //
CREATE TRIGGER SETSTATUS  AFTER INSERT ON Vehicle_in
FOR EACH ROW 
BEGIN
    CALL StatusUpdation(NEW.P_id);
END //
Delimiter ;

-----------------------------------------function-----------------------------------------------------
DELIMITER $$ 
CREATE FUNCTION Amount_calc(Owner_type varchar(20), t varchar(20)) 
RETURNS int
DETERMINISTIC 
BEGIN 
DECLARE VALUE int; 
IF Owner_type='Teacher' then 
set VALUE=0; 
 ELSE
 if t='Two wheeler' then
 set VALUE =10; 
 else 
 set value=30;
 end if; 
 end if;

 return value; 
END;$$ 
DELIMITER ;

------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------aggregate functions
SELECT COUNT(*) AS total_students FROM student; 
SELECT COUNT(*) AS total_faculty FROM faculty; 
SELECT COUNT(*) AS total_vehicles_entered FROM Vehicle_in; 
SELECT COUNT(*) AS total_parking_lots FROM parking_space; 

-------------------------------set operations
SELECT Name FROM faculty  
UNION  
SELECT Name FROM student; 

SELECT Parking_id FROM parking_space  
UNION  
SELECT P_id FROM Vehicle_in; 

SELECT Name FROM student  
UNION  
SELECT owner_type FROM Vehicle_in; 

