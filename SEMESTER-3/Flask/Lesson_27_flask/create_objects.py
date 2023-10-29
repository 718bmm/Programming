# This is a separate Python script in which we practice creating database objects 
# You can also perform these operations in command-line terminal
from app27 import app, db, Reader, Book, Review

app_ctx = app.app_context()
app_ctx.push()
# with app.app_context():
b1 = Book(id=123, title="Demian", author_name="Hermann", author_surname="Hesse") 
b2 = Book(id=533, title="The stranger", author_name="Albert", author_surname="Camus") 
r1 = Reader(id=342, name="Ann", surname="Adams", email="ann.adams@example.com") 
r2 = Reader(id=312, name="Sam", surname="Adams", email="sam.adams@example.com")

rev1 = Review(
    id=435, text="This book is amazing...", stars=5, book_id=b1.id
)
rev2 = Review(
    id=450, text="This book is difficult!", stars=2, reviewer_id=r2.id, book_id=b2.id
)

print(rev1)
print(rev1.text)
print(rev1.book_id) 
print(len(rev2.text.split()))
# db.session.add(b1) 
#db.session.add(b2)
db.session.add_all([b1, b2, r1, r2, rev1, rev2])
db.session.commit()
# print(Review.query.all())

app_ctx.pop()
