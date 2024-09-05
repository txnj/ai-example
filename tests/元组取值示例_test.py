if __name__ == '__main__':
    # 创建一个元组
    my_tuple = (1, 2, 3, 'a', 'b', 'c')

    # 1. 通过索引访问元素
    print(my_tuple[0])  # 输出: 1
    print(my_tuple[3])  # 输出: 'a'

    # 2. 负索引（从末尾开始计数）
    print(my_tuple[-1])  # 输出: 'c'
    print(my_tuple[-3])  # 输出: 'a'

    # 3. 切片
    print(my_tuple[1:4])  # 输出: (2, 3, 'a')
    print(my_tuple[:3])  # 输出: (1, 2, 3)
    print(my_tuple[3:])  # 输出: ('a', 'b', 'c')

    # 4. 解包
    a, b, c, *rest = my_tuple
    print(a, b, c, rest)  # 输出: 1 2 3 ['a', 'b', 'c']

    # 5. 遍历元组
    for item in my_tuple:
        print(item)

    # 6. 使用enumerate()同时获取索引和值
    for index, value in enumerate(my_tuple):
        print(f"索引 {index}: 值 {value}")

    # 7. 检查元素是否在元组中
    print('a' in my_tuple)  # 输出: True
    print(4 in my_tuple)  # 输出: False

    # 8. 获取元组长度
    print(len(my_tuple))  # 输出: 6
