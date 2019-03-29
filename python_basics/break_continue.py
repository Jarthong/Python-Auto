# break continue
m = 0
while m < 2:
    m += 1
    print('----m的值是：', m)
    for i in range(0, 10):
        if i == 5:
            # for循环到5的时候，就退出了for循环（5后面的i值都不循环了），再从外面的while重新开始执行
            # break

            # 没有退出了for循环（5后面的i值还会继续循环），只是跳过了i等于5时候的那个一个循环后面的语句
            continue
        print('i的值是：', i)

