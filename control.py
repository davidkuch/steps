from american_test import AmericanTest
from db_manager import DbManager as db

reader = db()
# reader.make_db()
path = r'C:\Users\david\Desktop\input\test.docx'
test1 = AmericanTest(path)

test1.run()
reader.read_db()
