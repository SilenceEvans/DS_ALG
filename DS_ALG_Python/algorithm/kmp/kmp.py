"""
kmp：尽快找到模式串在待匹配串中的位置
"""


def kmp(s, p):
    """
    :param s: 待匹配串
    :param p: 模式串
    :return:
    """
    i = 0  # 待匹配串的指针
    j = 0  # 模式串的指针

    next_ = get_next(p)
    while i < len(s):
        # 如果两个串元素相等，则各自的指针都后移一位
        if (s[i] == p[j]) | (j == -1):
            i += 1
            j += 1
            if j == len(p):
                return i - j
        else:
            # 此时就应该回退，回退的位置需要到next数组中去找
            # 如果两个串第一个元素就不相等，那么主串指针需要后移一位，子串则需要从0开始或者后移到合适的位置，
            # 所以 j 要么是-1，要么是其他位置的元素，是-1则可以加1就是第一个元素
            j = next_[j]


# 定义生成next_[]数组的方法
def get_next(p):
    j = 0
    k = -1
    next_ = [0 for i in range(len(p))]
    next_[0] = -1
    while j < len(p):
        """
        那如果假设此时 next[j] = k,也即 p[k-1] = p[j-1] 此时会有两种情况：
        1、p[k] = p[j],此时next[j+1] = k+1,即确定了下一个元素的next数组中的值
        2、p[k] != p[j],此时k需要回退，回到k之前的最大前后缀相同子串长度位置
          此时 k = next[k]，找到此时这个k位置的值来与 p[j]进行比较
        """
        if (p[k] == p[j]) | (k == -1):
            if j + 1 == len(p):
                break
            next_[j + 1] = k + 1
            j += 1
            k += 1
        else:
            k = next_[k]
    return next_


if __name__ == '__main__':
    s = "aaaceaadcaadbaada"
    p = "aada"
    a = kmp(s, p)
    print(a)
