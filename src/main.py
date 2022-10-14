#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/9/24 14:21
# @File    : main.py
# @Software: PyCharm


import argparse
import logging
from time import sleep

import requests

import utils.Headers
from proxyFetcher import ProxyFetcher

parser = argparse.ArgumentParser(description='Momo Share Flash')
parser.add_argument('--url', '-url', type=str, help='墨墨背单词分享链接', required=True, nargs='+')
parser.add_argument('--num', type=int, help='点击量', required=False, default=30, nargs='?')
parser.add_argument('--delay', type=int, help='刷新延时(ms)', required=False, default=5, nargs='?')
args = parser.parse_args()


class MomoFlash:
    def __init__(self, url='', times=30, delay=5):
        self.proxyFetcher = ProxyFetcher()
        self.freeProxysGen = []
        self.proxys = []
        self.shareTargetTimes = times
        self.sharedTimes = 0
        self.proxyNum = 30
        self.delay = delay
        self.url = url
        self.trials = 0
        self.genProxys()

    def getProxys(self):
        for proxyPool in self.freeProxysGen:
            for proxy in proxyPool:
                self.proxys.append(proxy)

    def genProxys(self):
        print('\n开始获取代理IP...\n')
        self.freeProxysGen.append(self.proxyFetcher.freeProxy02())
        self.freeProxysGen.append(self.proxyFetcher.freeProxy03())
        self.freeProxysGen.append(self.proxyFetcher.freeProxy05())
        self.freeProxysGen.append(self.proxyFetcher.freeProxy06())
        self.freeProxysGen.append(self.proxyFetcher.freeProxy07())
        self.freeProxysGen.append(self.proxyFetcher.freeProxy09())
        self.freeProxysGen.append(self.proxyFetcher.freeProxy10())
        self.getProxys()
        print('\n代理IP获取完毕，共获取{}个代理IP\n'.format(len(self.proxys)))

    def momo_flash(self):
        print("\n开始刷墨墨背单词分享链接...\n")
        print("当前代理IP池数量：{}\n".format(len(self.proxys)))
        print("当前刷新延迟：{}ms\n".format(self.delay))
        for url in self.url:
            self.sharedTimes = 0
            self.trials = 0
            while self.sharedTimes < self.shareTargetTimes:
                if len(self.proxys) == 0:
                    self.genProxys()
                try:
                    self.trials += 1
                    nowProxy = {"https": "https://{}".format(self.proxys[-1]),
                                "http": "http://{}".format(self.proxys[-1])}
                    print("[{}]当前代理IP：{}".format(self.trials, nowProxy))
                    resp = requests.get(url=url, headers=utils.Headers.header(),
                                        proxies=nowProxy, verify=False, timeout=1)
                    if resp.status_code == 200:
                        print(resp.text)
                        self.sharedTimes += 1
                        print('成功分享第{}次，using proxy[{}]\n'.format(self.sharedTimes, self.proxys[-1]))
                    else:
                        print('分享失败， 代理超时=>[{}]\n'.format(self.proxys[-1]))
                except Exception as e:
                    print('分享失败，代理失效=>[{}]\n'.format(self.proxys[-1]))
                    logging.debug(e)
                finally:
                    self.proxys.pop()
                    sleep(self.delay)
                    print("成功【{}】次，当前任务：【{}】".format(self.sharedTimes, url))

            print('*' * 30 + '\n分享{}结束，共分享{}次\n'.format(url, self.sharedTimes))


if __name__ == '__main__':
    print("请不要使用VPN等代理工具，否则可能会导致代理IP获取失败\n")
    momoFlash = MomoFlash(args.url, args.num, args.delay)
    # momoFlash = MomoFlash(["http://httpbin.org/ip"], 10, 1)
    momoFlash.momo_flash()
    input('按任意键退出...')
