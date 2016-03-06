from app import db
from models import BlogPost

db.create_all()
db.session.add(BlogPost("First Post", "Hello, World!"))
db.session.add(BlogPost("Second Post", "Hello again!"))

db.session.commit()
