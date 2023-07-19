# -*- coding: utf-8 -*-
from question import *
import os


def create_question_group(question_tag, Question):  # 新建或向问题组内添加新问题
    question_group_path = "./question_group/" + question_tag + ".txt"
    if not os.path.exists(question_group_path):
        file_tag = open(question_group_path, 'w')
        file_tag.write("[]")
        file_tag.close()
    file_tag = open(question_group_path, 'r+')
    questions_in_tag = eval(file_tag.read())
    file_tag.close()
    now_question = str(Question.q_id)
    questions_in_tag.append(now_question)
    file_tag = open(question_group_path, 'r+')
    file_tag.write(str(questions_in_tag))
    # Question.tags.append(question_tag)
    return "添加成功"


def delete_question_group(question_tag, Question):
    question_group_path = "./question_group/" + question_tag + ".txt"
    if not os.path.exists(question_group_path):
        return '不存在该标签'
    file_tag = open(question_group_path, 'r+')
    questions_in_tag = eval(file_tag.read())
    file_tag.close()
    now_question = str(Question.name) + '-' + str(Question.q_id)
    index = -1
    for i in range(len(questions_in_tag)):
        if str(questions_in_tag[i]) == str(now_question):
            index = i
    if index == -1:
        return '不在该类中'
    questions_in_tag.pop(index)
    file_tag = open(question_group_path, 'r+')
    file_tag.truncate(0)
    file_tag.write(str(questions_in_tag))
    return '删除成功'


def get_questions_by_tag(tag):
    question_group_path = "./question_group/" + tag + ".txt"
    if not os.path.exists(question_group_path):
        return None
    else:
        file_tag = open(question_group_path, "r")
        questions_in_tag = eval(file_tag.read())
        return questions_in_tag


def get_intersection(former, tag):
    question_group_path = "./question_group/" + tag + ".txt"
    if not os.path.exists(question_group_path):
        return None
    else:
        file_tag = open(question_group_path, "r")
        latter = eval(file_tag.read())
    return list(set(latter).intersection(set(former)))


def get_union(former, tag):
    question_group_path = "./question_group/" + tag + ".txt"
    if not os.path.exists(question_group_path):
        return None
    else:
        file_tag = open(question_group_path, "r")
        latter = eval(file_tag.read())
    return list(set(latter).union(set(former)))
