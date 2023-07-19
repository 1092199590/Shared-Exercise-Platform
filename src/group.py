import os


def create_group(user_id, group_name):
    user_path = "./users/" + user_id + ".txt"
    if not os.path.exists(user_path):
        return '用户不存在'
    file_user = open(user_path, 'r')
    user = eval(file_user.read())
    file_user.close()
    if not user['isAdmin']:
        return '无权限'
    group = {'g_name': group_name, 'g_members': [user_id]}
    group_path = "./groups/" + group_name + ".txt"
    if os.path.exists(group_path):
        return '群组已存在'
    file_group = open(group_path, 'w')
    file_group.write(str(group))
    file_group.close()
    # 修改用户信息
    user['g_name'].append(group_name)
    file_user = open(user_path, 'w')
    file_user.write(str(user))
    file_user.close()
    return '创建成功'


def add_group_member(operate_user_id, group_name, user_id):
    group_path = "./groups/" + group_name + ".txt"
    user_path = "./users/" + user_id + ".txt"
    # 判断用户是否存在
    if not os.path.exists(user_path):
        return '用户不存在'
    operate_user_path = "./users/" + operate_user_id + ".txt"
    if not os.path.exists(operate_user_path):
        return '操作用户不存在'
    if operate_user_id != user_id:
        # 判断是否有权限
        file_operate_user = open(operate_user_path, 'r')
        operate_user = eval(file_operate_user.read())
        file_operate_user.close()
        if not operate_user['isAdmin']:
            return '无权限'
    if os.path.exists(group_path):
        file_group = open(group_path, 'r')
        group = eval(file_group.read())
        file_group.close()
        if user_id in group['g_members']:
            return '该用户已存在组中'
        else:
            group['g_members'].append(user_id)
            file_group = open(group_path, 'w')
            file_group.write(str(group))
            file_group.close()
            # 修改用户信息
            file_user = open(user_path, 'r')
            user = eval(file_user.read())
            file_user.close()
            user['g_name'].append(group_name)
            file_user = open(user_path, 'w')
            file_user.write(str(user))
            file_user.close()
            return '添加成功'
    else:
        return '群组不存在'


def delete_group_member(operate_user_id, group_name, user_id):
    group_path = "./groups/" + group_name + ".txt"
    user_path = "./users/" + user_id + ".txt"
    # 判断用户是否存在
    if not os.path.exists(user_path):
        return '用户不存在'
    operate_user_path = "./users/" + operate_user_id + ".txt"
    if not os.path.exists(operate_user_path):
        return '操作用户不存在'
    if operate_user_id != user_id:
        # 判断是否有权限
        file_operate_user = open(operate_user_path, 'r')
        operate_user = eval(file_operate_user.read())
        file_operate_user.close()
        if not operate_user['isAdmin']:
            return '无权限'
    if os.path.exists(group_path):
        file_group = open(group_path, 'r')
        group = eval(file_group.read())
        file_group.close()
        if user_id in group['g_members']:
            group['g_members'].remove(user_id)
            file_group = open(group_path, 'w')
            file_group.write(str(group))
            file_group.close()
            # 修改用户信息
            file_user = open(user_path, 'r')
            user = eval(file_user.read())
            file_user.close()
            user['g_name'].remove(group_name)
            file_user = open(user_path, 'w')
            file_user.write(str(user))
            file_user.close()
            return '删除成功'
        else:
            return '该用户不存在组中'
    else:
        return '群组不存在'


def search_group(keyword):
    group_path = "./groups/"
    group_list = []
    for group_name in os.listdir(group_path):
        if keyword in group_name:
            group_list.append(group_name)
    return group_list


def get_group_users(group_name):
    group_path = "./groups/" + group_name + ".txt"
    if os.path.exists(group_path):
        file_group = open(group_path, 'r')
        group = eval(file_group.read())
        file_group.close()
        return group['g_members']
    else:
        return '群组不存在'
