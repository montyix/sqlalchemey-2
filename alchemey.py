from sqlalchemy import create_engine,Foreignkey, column, string, integer,char
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemey.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'

    ssn = column("ssn", integer, Primary_key = True)
    firstname = column("firstname", string)
    lastname = column("lastname", string)
    gender = column("gender", char)
    age = column("age", string)

    def __int__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname=first
        self.lastname=last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender},{self.age})"

class Thing(Base):
    __tablename__ = "things"

    tid = column("tid", integer, primary_key=True)
    description  = column("description", string)
    owner = column(integer, Foreignkey("people.ssn "))


engine = create_engine("postgresql:///mydb.db", echo =True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person =Person(12312, "Mike", "smith", "m",35)
session.add(person)
session.add(person)
session.commit()

results = session.query(Person).filter(Person.lastname == "Blue")
for r in results:
    print(r)


















conn = psycopg2.connect(host="localhost", dbname = "postgres", user="postgres", password="1234", port="5432")

cur = conn.cursor()

cur.excute(""" CREATE TABLE IF NOT EXISTS person (id INT PRIMARY KEY, name varchar(50) NOT NULL, 
AGE INT, GENDER VARCAHR(50) NOT NULL);""")

cur.excute("""INSERT INTO person (id, name, age, gender) VALUES (1,2,3,4)""")


conn.commit()
cur.close()
conn.close()
