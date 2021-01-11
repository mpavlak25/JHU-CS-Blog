# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.blogpost import Blogpost

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
exams = session.query(Blogpost).all()

if len(exams) == 0:
    # create and persist mock exam
    python_post = Blogpost("SQLAlchemy Exam", "Test your knowledge about SQLAlchemy.", "script")
    session.add(python_post)
    session.commit()
    session.close()

    # reload exams
    posts = session.query(Blogpost).all()

# show existing exams
print('### Blogposts:')
for bp in posts:
    print(f'({bp.id}) {bp.title} - {bp.description}')
