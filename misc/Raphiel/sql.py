
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    
    __tablename__ = "School"
    
    schoolID =Column("schoolID", Integer, primary_key=True)
    name = Column("name", String)
    address = Column("address", String)
    email = Column("email", String)
    
    
    def __init__(self, schoolID, name, address, email):
        self.schoolID =schoolID
        self.name = name
        self.address = address
        self.email = email
        
    
    def __repr__(self):
        return f"({self.schoolID}, {self.name}, {self.address},{self.email})"
    


####################################################################################

    __tablename__ = "Users"

    userID =Column("userID", Integer, primary_key=True)
    schoolID =Column("schoolID", Integer, foreign_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    email = Column("email", String)
    password = Column("password", String)
    
    
    def __int__(self, userID, schoolID, firstname, lastname, email, password):
        self.userID = userID
        self.schoolID =schoolID
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        
        
    def __repr__(self):
        return f"({self.userID}, {self.schoolID}, ({self.firstname} {self.lastname}), {self.email}, {self.password})"
    
##################################################################################################
    
    __tablename__ = "Cases"

    caseID =Column("caseID", Integer, primary_key=True)
    schoolID =Column("schoolID", Integer, foreign_key=True)
    casename = Column("casename", String)
    
    


    def __int__(self, caseID, schoolID, casename):
        self.caseID = caseID
        self.schoolID =schoolID
        self.casename = casename
        
    
    def __repr__(self):
        return f"({self.caseID}, {self.schoolID}, ({self.casename} ))"
    
    
################################################################################################################################
    
    __tablename__ = "Projections"

    projectionsID =Column("projectionID", Integer, primary_key=True)
    caseID =Column("caseID", Integer, foreign_key=True)
    projection = Column("projection", String)
    riskLevel = Column("riskLevel", String)
    
    
    def __init__(self, projectionID, caseID, projection, riskLevel):
        self.projectionID = projectionID
        self.caseID = caseID
        self.projection = projection
        self.riskLevel = riskLevel

        
    
    def __repr__(self):
        return f"({self.projectionID}, {self.caseID}, {self.prjection}, {self.riskLevel})"
    
    
##################################################################################################################################
    
    
    __tablename__ = "Event Log"

    evetLogID =Column("eventLogID", Integer, primary_key=True)
    caseID =Column("caseID", Integer, foreign_key=True)
    logEntries = Column("LogEntries", String)
    datetime = Column ("datetime", year = '0000', month = '00', day = '00', hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
    location = Column("location", String)
    SubmittedBy = Column("submittedby", String)
    status = Column("status", String )
    
    
    def __int__(self, eventLogID, caseID, logEntries, datetime, location, submittedBy, status):
        self.eventLogID = eventLogID,
        self.caseID = caseID,
        self.logEntries = logEntries,
        self.datetime = datetime,
        self.location = location,
        self.SubmittedBy = submittedBy
        self.status = status
        
    
    def __repr__(self):
        return f"({self.eventLogID}, {self.caseID}, {self.logEntries}, {self.datetime}, {self.location}, {self.submittedby}, {self.status})"


engine = create_engine("sqlite:/// ", echo=True)   
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
session.commit()