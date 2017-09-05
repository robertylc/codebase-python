#!/usr/local/bin/python3
# coding=utf-8
def main():
    # 打开一个文件
    fo = open("../../../foo.txt", "r+")
    str = fo.read(3000)
    print "读取的字符串是 : ", str

    # 查找当前位置
    position = fo.tell();
    print "当前文件位置 : ", position

    # 把指针再次重新定位到文件开头
    position = fo.seek(0, 0);
    str = fo.read(10);
    print "重新读取字符串 : ", str

    # 关闭打开的文件
    fo.close()

if __name__ == '__main__':
    #main()
    fo = open("../../../foo.txt", "r+")
    str = fo.read(3000)
