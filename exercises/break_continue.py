def skip_multiples_of_three(n):
    """
    返回从1到n的所有非3的倍数的整数列表

    参数:
    - n: 正整数上限

    返回:
    - 从1到n中所有不是3的倍数的整数列表
    """
    # 请在下方编写代码
    pass
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            continue
        result.append(i)
    return result