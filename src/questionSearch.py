import os


def show_all_questions(user_id):  # 展示某用户所有有权限的题目
    file_user = open("./users/" + user_id + ".txt", 'r')
    user = eval(file_user.read())
    file_user.close()

    questions = []
    for question_id in os.listdir('./questions'):
        question_path = "./questions/" + question_id
        file_question = open(question_path, 'r')
        question = eval(file_question.read())
        file_question.close()
        if 'access' not in question.keys():
            question['access'] = []
        if user_id in question['access'] or question['user'] == user_id or user['isAdmin'] == 1:
            questions.append(question)
    return questions


def search_question(keywords, user_id, way):  # 通过方式way查找题目
    file_user = open("./users/" + user_id + ".txt", 'r')
    user = eval(file_user.read())
    file_user.close()

    questions = []
    for question_id in os.listdir('./questions'):
        question_path = "./questions/" + question_id
        file_question = open(question_path, 'r')
        question = eval(file_question.read())
        file_question.close()
        if 'access' not in question.keys():
            question['access'] = []
        if user_id in question['access'] or question['user'] == user_id or user['isAdmin'] == 1:
            if way == 'stem':
                if keywords in question['question_stem']:
                    questions.append(question)
            elif way == 'tag':
                if keywords in question['tags']:
                    questions.append(question)
            elif way == 'name':
                if keywords in question['name']:
                    questions.append(question)
    return questions


# print(show_all_questions('1'))
# print(search_question('test', '1', 'stem'))
