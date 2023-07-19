from question import *
import os


def share_question_to_group(question_id, group_name):  # 分享单个问题到群组
    group_path = "./groups/" + group_name + ".txt"
    question_path = "./questions/" + question_id + ".txt"
    file_question = open(question_path, 'r')
    question = eval(file_question.read())
    file_question.close()
    if 'access' not in question.keys():
        question['access'] = []
    if os.path.exists(group_path):
        file_group = open(group_path, 'r')
        group = eval(file_group.read())
        file_group.close()
        for user_id in group['g_members']:
            # 如果用户已经有权限了，就不再添加
            if user_id in question['access']:
                continue
            question['access'].append(user_id)
        file_question = open(question_path, 'w')
        file_question.write(str(question))
        file_question.close()
        return '分享成功'
    else:
        return '群组不存在'


def share_question_to_all(question_id):  # 分享单个问题到所有用户
    question_path = "./questions/" + question_id + ".txt"
    file_question = open(question_path, 'r')
    question = eval(file_question.read())
    file_question.close()
    if 'access' not in question.keys():
        question['access'] = []
    for user_id in os.listdir('./users'):
        # 如果用户已经有权限了，就不再添加
        if user_id[:-4] in question['access']:
            continue
        question['access'].append(user_id[:-4])
    file_question = open(question_path, 'w')
    file_question.write(str(question))
    file_question.close()
    return '分享成功'


def share_questiongroup_to_group(question_tag, group_name, user_id):  # 分享问题组到群组
    question_group_path = "./question_group/" + question_tag + ".txt"
    group_path = "./groups/" + group_name + ".txt"
    file_group = open(group_path, 'r')
    group = eval(file_group.read())
    file_group.close()
    if os.path.exists(group_path):
        file_tag = open(question_group_path, 'r')
        questions_in_tag = eval(file_tag.read())
        file_tag.close()
        # 修改问题组中的问题的权限
        for question_id in questions_in_tag:
            question_path = "./questions/" + question_id + ".txt"
            file_question = open(question_path, 'r')
            question = eval(file_question.read())
            if 'access' not in question.keys():
                question['access'] = []
            file_question.close()
            if not question['user'] == user_id:
                continue
            for group_user_id in group['g_members']:
                # 如果用户已经有权限了，就不再添加
                if group_user_id in question['access']:
                    continue
                question['access'].append(group_user_id)
            file_question = open(question_path, 'w')
            file_question.write(str(question))
            file_question.close()
        return '分享成功'
    else:
        return '群组不存在'


def share_questiongroup_to_all(question_tag, user_id):  # 分享问题组到所有用户
    question_group_path = "./question_group/" + question_tag + ".txt"
    file_tag = open(question_group_path, 'r')
    questions_in_tag = eval(file_tag.read())
    file_tag.close()
    # 修改问题组中的问题的权限
    for question_id in questions_in_tag:
        question_path = "./questions/" + question_id + ".txt"
        file_question = open(question_path, 'r')
        question = eval(file_question.read())
        file_question.close()
        if 'access' not in question.keys():
            question['access'] = []
        if not question['user'] == user_id:
            continue
        for user in os.listdir('./users'):
            # 如果用户已经有权限了，就不再添加
            if user[:-4] in question['access']:
                continue
            question['access'].append(user[:-4])
        file_question = open(question_path, 'w')
        file_question.write(str(question))
        file_question.close()
    return '分享成功'


# print(share_questiongroup_to_all('O', '1'))
