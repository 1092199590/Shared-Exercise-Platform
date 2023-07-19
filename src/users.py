# 实现用户和管理员注册登录
import os
from group import *


def register(user_id, user_pwd, user_name, is_admin):
    user = {'u_id': user_id, 'u_pwd': user_pwd, 'u_name': user_name, 'isAdmin': is_admin, 'g_name': []}
    user_path = "./users/" + user_id + ".txt"
    # 判断是否有user_path文件，如果有则返回用户已存在
    if os.path.exists(user_path):
        return '用户已存在'
    file_user = open(user_path, 'w')
    file_user.write(str(user))
    file_user.close()
    return '注册成功'


def signup(user_id, user_pwd):
    user_path = "./users/" + user_id + ".txt"
    if os.path.exists(user_path):
        file_user = open(user_path, 'r')
        user = eval(file_user.read())
        file_user.close()
        if user_pwd == user['u_pwd']:
            return '登录成功'
        else:
            return '密码错误'
    else:
        return '用户不存在'


def change_pwd(user_id, new_pwd):
    user_path = "./users/" + user_id + ".txt"
    if os.path.exists(user_path):
        file_user = open(user_path, 'r')
        user = eval(file_user.read())
        file_user.close()
        user['u_pwd'] = new_pwd
        file_user = open(user_path, 'w')
        file_user.write(str(user))
        file_user.close()
        return '修改成功'
    else:
        return '用户不存在'


def change_name(user_id, new_name):
    user_path = "./users/" + user_id + ".txt"
    if os.path.exists(user_path):
        file_user = open(user_path, 'r')
        user = eval(file_user.read())
        file_user.close()
        user['u_name'] = new_name
        file_user = open(user_path, 'w')
        file_user.write(str(user))
        file_user.close()
        return '修改成功'
    else:
        return '用户不存在'


def delete_user(user_id):
    user_path = "./users/" + user_id + ".txt"
    if os.path.exists(user_path):
        file_user = open(user_path, 'r')
        user = eval(file_user.read())
        file_user.close()
        # 删除用户所在的所有群组
        for group_name in user['g_name']:
            delete_group_member(user_id, group_name, user_id)
        # 删除用户文件
        os.remove(user_path)
        return '删除成功'
    else:
        return '用户不存在'


def get_user_groups(user_id):
    user_path = "./users/" + user_id + ".txt"
    if os.path.exists(user_path):
        file_user = open(user_path, 'r')
        user = eval(file_user.read())
        file_user.close()
        return user['g_name']
    else:
        return '用户不存在'
