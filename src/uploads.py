from question import *
import re


def upload_single_question(question_stem, tags, answer, user_id, name):  # 上传问题，填写相关信息
    with open("q_id.txt", "r") as file:  # q_id文件位于当前目录，用于生成唯一编号
        qid = int(file.read())
    with open("q_id.txt", "w") as file:
        qid += 1
        file.write(str(qid))

    question = Question(question_stem, answer, user_id, name, qid)
    question_path = "./questions/" + str(qid) + ".txt"

    for tag in tags:
        question.add_tag(tag)

    file_question = open(question_path, 'w')
    file_question.write(str(question))
    file_question.close()
    return '上传成功'


def upload_single_choice(question_stem, tags, answer, user_id, name, choices):  # 上传选择题
    with open("q_id.txt", "r") as file:
        qid = int(file.read())
    with open("q_id.txt", "w") as file:
        qid += 1
        file.write(str(qid))

    question = Choice(question_stem, answer, user_id, name, qid, choices)
    question_path = "./questions/" + str(qid) + ".txt"

    for tag in tags:
        question.add_tag(tag)

    file_question = open(question_path, 'w')
    file_question.write(str(question))
    file_question.close()
    return '上传成功'


def upload_question_by_file(file_path):  # 通过文件批量上传问题
    """ 默认和文件中question的格式为
        str({
            'question_stem': question_stem,
            'tags': tags,
            'answer': answer,
            'user': user,
            'name': name,
            ('choices':choices)
        })
    """
    with open(file_path, "r") as file:
        contents = file.read()

    if len(contents) == 0:
        return "文件为空"

    pattern = r'\{(.*?)\}'  # 定义匹配大括号内内容的正则表达式模式
    matches = re.findall(pattern, contents)

    if len(matches) == 0:
        return "文件格式错误"

    for match in matches:
        match = "{" + str(match) + "}"
        try:
            dic = eval(match)
        except (SyntaxError, NameError):
            return "文件格式错误"

        assert isinstance(dic, dict)

        try:
            question_stem = dic["question_stem"]  # 题干
        except KeyError:
            return "文件格式错误"

        try:
            tags = dic["tags"]  # 标签
        except KeyError:
            return "文件格式错误"

        try:
            answer = dic["answer"]  # 答案
        except KeyError:
            return "文件格式错误"

        try:
            user = dic["user"]  # 创建者
        except KeyError:
            return "文件格式错误"

        try:
            name = dic["name"]  # 问题名称
        except KeyError:
            return "文件格式错误"

        if len(dic) == 6:
            try:
                choices = ["choices"]  # 选项
            except KeyError:
                return "文件格式错误"
        else:
            choices = []

        if len(dic) == 5:
            upload_single_question(question_stem, tags, answer, user, name)
        elif len(dic) == 6:
            upload_single_choice(question_stem, tags, answer, user, name, choices)
        else:
            return "文件格式错误"

    return "上传成功"


def make_file_to_question(file_path):  # 将文件转化成question类
    with open(file_path, "r") as file:
        contents = file.read()

    try:
        dic = eval(contents)
    except (SyntaxError, NameError):
        return "文件格式错误1"

    assert isinstance(dic, dict)

    if not all(key in dic for key in ["question_stem", "tags", "answer", "reply", "accesses", "user", "name", "q_id"]):
        return "文件格式错误2"

    question_stem = dic.get("question_stem")
    tags = dic.get("tags")
    answer = dic.get("answer")
    reply = dic.get("reply")
    accesses = dic.get("accesses")
    user = dic.get("user")
    name = dic.get("name")
    q_id = dic.get("q_id")
    choices = dic.get("choices")

    if choices is not None:
        question = Choice(question_stem, answer, user, name, q_id, choices)
    else:
        question = Question(question_stem, answer, user, name, q_id)
    question.tags = tags
    question.accesses = accesses
    question.user = user
    question.name = name
    question.q_id = q_id
    question.reply = reply

    return question


def change_single_attribute(file_path, attribute, command):  # 为函数添加或修改属性
    """
    :param file_path: 相应question的文件
    :param attribute: 想要添加的函数属性
    :param command:
    {
        question_stem  # 题干
        tags # 标签
        answer  # 答案
        reply  # 用户的回答
        accesses  # 权限
        name  # 问题名称
        choices # 选项，选择题时使用
     }
    """
    question = make_file_to_question(file_path)
    if question == "文件格式错误":
        return "文件格式错误"
    if command == "question_stem":
        question.question_stem = attribute
    elif command == "tags":
        question.tags = attribute
    elif command == "answer":
        question.answer = attribute
    elif command == "reply":
        question.reply = attribute
    elif command == "accesses":
        question.accesses = attribute
    elif command == "name":
        question.name = attribute
    elif command == "choices" and isinstance(question, Choice):
        question.choices = attribute
    else:
        print("不存在该指令")
        return None

    with open(file_path, "w") as file:
        file.write(question.__str__())

    return "修改完成"


def add_single_attribute(file_path, attribute, command):  # 为函数添加或修改属性
    """
    :param file_path: 相应question的文件
    :param attribute: 想要添加的函数属性
    :param command:
    {
        tags # 标签
        （answer）  # 答案，选择题可用
        reply  # 用户的回答
        accesses  # 权限
        choices # 选项，选择题时使用
     }
    """

    question = make_file_to_question(file_path)
    if question == "文件格式错误":
        return "文件格式错误"

    if command == "tags":
        question.add_tag(attribute)
    elif command == "answer" and isinstance(question, Choice):
        question.add_answer(attribute)
    elif command == "reply":
        question.add_reply(attribute)
    elif command == "accesses":
        question.add_access(attribute)
    elif command == "choices" and isinstance(question, Choice):
        question.add_choice(attribute)
    else:
        print("不存在该指令")
        return None

    with open(file_path, "w") as file:
        file.write(question.__str__())

    return "修改完成"
