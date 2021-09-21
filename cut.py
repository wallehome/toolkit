# coding=utf-8

import re
import os

import common


class CutFile(object):
    """分割文件
    @param src {string}  待分割的文件
    @param dist {string} 分割后存放的文件夹
    @param preg {string} 分割的正则表达式
    @returns {void}
    """

    def __init__(self, src, dist, preg):
        if not os.path.isfile(src):
            raise Exception("src 必须为一个文件")

        dist = dist.rstrip("/") + "/"
        if not os.path.exists(dist):
            os.mkdir(dist)

        if not os.path.isdir(dist):
            raise Exception("dist 必须为一个目录，分割出来的文件存放于该目录")

        self.src = src
        self.dist = dist
        self.pattern = re.compile(preg)

    def newFileName(self, step):
        return self.dist + "t" + str("%04d" % step) + '.dat'

    def cut(self):
        current = False
        step = 1
        with open(self.src, encoding="utf-8") as f:
            for line in f:
                r = self.pattern.findall(line)
                if r:
                    filename = self.newFileName(step)
                    print(filename)
                    current = open(filename, encoding="utf-8", mode="w")
                    current.write(common.CommonText.TEXT_HEADER)
                    step += 1
                if current:
                    current.write(line)
