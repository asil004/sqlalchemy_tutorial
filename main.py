from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from db.db import engine, Student

Session = sessionmaker(bind=engine)

session = Session()

s1 = Student('Tolibov', 'Asilbek', 19)
s2 = Student('Tolibov', 'Sanjar', 18)

# session.add(s2)
# session.commit()

# students = session.query(Student).all()
# for student in students:
#     print(student)

# student = session.query(Student).first()
# print(student)

# student = session.query(Student).filter(Student.age == 18)
# for i in student:
#     print(i)

student = session.query(Student).from_statement(text('SELECT * FROM students'))
for i in student:
    print(i)