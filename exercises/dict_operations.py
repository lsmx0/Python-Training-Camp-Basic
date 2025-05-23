def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作

    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数

    返回:
    - 根据操作返回不同结果
    """
    # 请在下方编写代码
    pass
    if operation == "add":
        # 添加学生，args[0]=姓名，args[1]=成绩
        students_dict[args[0]] = args[1]
        return students_dict
    
    elif operation == "remove":
        # 删除学生，args[0]=姓名
        if args[0] in students_dict:
            del students_dict[args[0]]
        return students_dict
    
    elif operation == "update":
        # 更新学生成绩，args[0]=姓名，args[1]=新成绩
        if args[0] in students_dict:
            students_dict[args[0]] = args[1]
        return students_dict
    
    elif operation == "get":
        # 获取学生成绩，args[0]=姓名
        return students_dict.get(args[0])