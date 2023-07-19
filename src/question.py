import questionGroup

question_groups = {}


class Question:
    def __init__(self, question_stem, answer, user_id, name, q_id):
        self.question_stem = question_stem  # 题干
        self.tags = []  # 标签
        self.answer = answer  # 答案
        self.reply = []  # 用户的回答
        self.accesses = []  # 权限
        self.user = user_id  # 创建者
        self.name = name  # 问题名称
        self.q_id = q_id  # 编码

    def add_tag(self, tag):
        self.tags.append(tag)
        # add_question_to_group(self, tag)
        questionGroup.create_question_group(tag, self)

    def add_access(self, access):
        self.accesses.append(access)

    def add_reply(self, reply):
        self.reply = reply

    def is_right(self):
        return self.reply == self.answer

    def is_access(self, access):
        return access in self.accesses

    def get_question_stem(self):
        return self.question_stem

    def get_tags(self):
        return self.tags

    def get_answer(self):
        return self.answer

    def get_reply(self):
        return self.reply

    def __str__(self):
        return str({
            'question_stem': self.question_stem,
            'tags': self.tags,
            'answer': self.answer,
            'reply': self.reply,
            'accesses': self.accesses,
            'user': self.user,
            'name': self.name,
            'q_id': self.q_id
        })


class Choice(Question):  # 选择题（这里的answer和reply视为列表）
    def __init__(self, question_stem, answer, user_id, name, q_id, choices, ):
        super().__init__(question_stem, answer, user_id, name, q_id)
        self.choices = choices  # 选项

    def add_choice(self, choice):
        self.choices.append(choice)

    def get_choices(self):
        return self.choices

    def add_answer(self, answer):
        self.answer.append(answer)

    def add_reply(self, reply):
        self.reply.append(reply)

    def is_right(self):  # 如果传入的是ABCD这样的我按字典序排序完比较
        buf_answer = sorted(list(self.answer))
        buf_reply = sorted(list(self.reply))
        return buf_answer.__eq__(buf_reply)

    def __str__(self):
        return str({
            'question_stem': self.question_stem,
            'tags': self.tags,
            'answer': self.answer,
            'reply': self.reply,
            'accesses': self.accesses,
            'user': self.user,
            'name': self.name,
            'q_id': self.q_id,
            'choices': self.choices
        })


class Subjective(Question):  # 问答题
    def __init__(self, question_stem, answer, user_id, name, q_id):
        super().__init__(question_stem, answer, user_id, name, q_id)


class Judgment(Question):  # 判断
    def __init__(self, question_stem, answer, user_id, name, q_id):
        super().__init__(question_stem, answer, user_id, name, q_id)


class QuestionGroup:  # 问题组
    def __init__(self, question_group, tag):
        self.question_group = question_group
        self.tag = tag

    def add_question(self, question):
        list(self.question_group).append(question)

    def get_tag(self):
        return self.tag

    def get_question_group(self):
        return self.question_group


def add_question_to_group(question, tag):  # 将question加入对应的group中
    if tag in question_groups:
        question_group = question_groups[tag]
        question_group.add_question(question)
    else:
        buf = []
        question_group = QuestionGroup(buf, tag)
        question_group.add_question(question)
        question_groups[tag] = question_group


def get_questions_by_tag(tag):  # 根据tag获取问题组中的所有问题
    if tag in question_groups:
        question_group = question_groups[tag]
        return question_group.question_group
    else:
        return None


def get_question_by_index(tag, index):  # 根据tag和索引获取特定位置的问题
    questions = get_questions_by_tag(tag)
    if questions:
        if 0 <= index < len(questions):
            return questions[index]
    return None
