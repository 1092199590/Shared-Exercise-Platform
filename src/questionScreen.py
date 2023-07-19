import os
import re


def is_admin(user_id):  # 判断是否为管理员
    user_path = "./users/" + user_id + ".txt"
    if os.path.exists(user_path):
        file_user = open(user_path, 'r')
        user = eval(file_user.read())
        file_user.close()
        return user['isAdmin']
    else:
        return False


def delete_question(question_id):  # 删除题目
    question_path = "./questions/" + question_id + ".txt"
    if os.path.exists(question_path):
        os.remove(question_path)
        # 遍历question_group文件夹，删除该题目
        for group_name in os.listdir('./question_group'):
            group_path = "./question_group/" + group_name
            file_group = open(group_path, 'r')
            group = eval(file_group.read())
            file_group.close()
            if question_id in group:
                group.remove(question_id)
                file_group = open(group_path, 'w')
                file_group.write(str(group))
                file_group.close()
        return '删除成功'
    else:
        return '题目不存在'


def search_sensitive_word(question, sensitive_word):  # 查找敏感词位置
    locate = {'question_stem': [], 'answer': [], 'name': []}
    # 找出题干中所有的敏感词的位置
    for m in re.finditer(sensitive_word, question['question_stem']):
        locate['question_stem'].append(m.span())
    # 找出答案中所有的敏感词的位置
    for m in re.finditer(sensitive_word, question['answer']):
        locate['answer'].append(m.span())
    # 找出题名中所有的敏感词的位置
    for m in re.finditer(sensitive_word, question['name']):
        locate['name'].append(m.span())
    return locate

# print(search_sensitive_word({'question_stem': 'test asdadas test', 'tags': [], 'answer': 'answer adsasd test','user': '1', 'name': 'mytest1'}, 'test'))
