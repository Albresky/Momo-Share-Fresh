#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/9/24 14:21
# @File    : main.py
# @Software: PyCharm


import argparse
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
        self.freeProxysGen = None
        self.proxys = []
        self.shareTargetTimes = times
        self.sharedTimes = 0
        self.proxyNum = 30
        self.delay = delay
        self.url = url

        self.genProxys()

    def getProxys(self):
        for proxy in self.freeProxysGen:
            self.proxys.append(proxy)

    def genProxys(self):
        print('\n开始获取代理IP...\n')
        if len(self.proxys) < self.proxyNum:
            self.freeProxysGen = self.proxyFetcher.freeProxy02()
            self.getProxys()
            if len(self.proxys) < self.proxyNum:
                self.freeProxysGen = self.proxyFetcher.freeProxy03()
                self.getProxys()
                if len(self.proxys) < self.proxyNum:
                    self.freeProxysGen = self.proxyFetcher.freeProxy05()
                    self.getProxys()
                    if len(self.proxys) < self.proxyNum:
                        self.freeProxysGen = self.proxyFetcher.freeProxy06()
                        self.getProxys()
                        if len(self.proxys) < self.proxyNum:
                            self.freeProxysGen = self.proxyFetcher.freeProxy07()
                            self.getProxys()
        print('\n代理IP获取完毕，共获取{}个代理IP\n'.format(len(self.proxys)))

    def momo_flash(self):
        print("\n开始刷墨墨背单词分享链接...\n")
        print("当前代理IP池数量：{}\n".format(len(self.proxys)))
        print("当前刷新延迟：{}ms\n".format(self.delay))
        for url in self.url:
            if len(self.proxys) < self.shareTargetTimes:
                self.genProxys()
            self.sharedTimes = 0
            for i in range(self.shareTargetTimes):
                try:
                    resp = requests.get(url=url, headers=utils.Headers.header(),
                                        proxies={"http": "http://{}".format(self.proxys[-1])}, verify=False)
                    if resp.status_code == 200:
                        self.sharedTimes += 1
                        print('成功分享第{}次，using proxy[{}]'.format(self.sharedTimes, self.proxys[-1]))
                    else:
                        print('分享失败，using proxy[{}]'.format(self.proxys[-1]))
                    self.proxys.pop()
                    sleep(self.delay)
                except Exception as e:
                    print(e)
            print('*' * 30 + '\n分享结束，共分享{}次\n'.format(self.sharedTimes))


if __name__ == '__main__':
    print("请不要使用VPN等代理工具，否则可能会导致代理IP获取失败\n")
    momoFlash = MomoFlash(args.url, args.num, args.delay)
    momoFlash.momo_flash()
    input('按任意键退出...')
