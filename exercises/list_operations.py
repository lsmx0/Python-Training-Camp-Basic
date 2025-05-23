def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作

    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数

    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    pass
    if operation == "add":
        # 添加学生，args[0]=姓名
        students.append(args[0])
    elif operation == "remove":
        # 删除学生，args[0]=姓名
        if args[0] in students:
            students.remove(args[0])
    elif operation == "update":
        # 更新学生姓名，args[0]=旧姓名，args[1]=新姓名
        if args[0] in students:
            index = students.index(args[0])
            students[index] = args[1]
    return students