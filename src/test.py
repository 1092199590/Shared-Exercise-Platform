import users
from question import *
import uploads

users.register('1', '1000', 'l', "y")
qid = "61"
qid1 = "60"
"""
uploads.upload_question_by_file("questions/12.txt")
uploads.upload_single_choice("test2", ["OO"], ["A", "B"], "1", "mytest2", ["1", "2"])
"""

print(uploads.make_file_to_question("./questions/" + qid + ".txt"))
print(uploads.make_file_to_question("./questions/" + qid1 + ".txt"))
uploads.change_single_attribute("./questions/" + qid + ".txt", "change test1", "question_stem")
uploads.add_single_attribute("./questions/" + qid + ".txt", "change test1 tags", "tags")
uploads.add_single_attribute("./questions/" + qid1 + ".txt", "change test2 answer", "answer")
print(uploads.make_file_to_question("./questions/" + qid + ".txt"))
print(uploads.make_file_to_question("./questions/" + qid1 + ".txt"))

