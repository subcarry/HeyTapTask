# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/11
# @Author  : 2984922017@qq.com
# @File    : config.py
# @Software: PyCharm

import requests
import time
import random

from config import accounts


class HuanTai:
    def __init__(self,dic):
        self.session = requests.session()
        self.dic = dic

#任务中心-签到的信息
    def reporinfo(self):
        url = 'https://store.oppo.com/cn/oapi/credits/web/credits/show'
        headers = {'Host': 'store.oppo.com', 'Connection': 'keep-alive', 'source_type': '501', 'clientPackage': 'com.oppo.store', 'Cache-Control': 'no-cache', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36 oppostore/201202 ROM/V0.0 brand/Android model/MuMu', 'Accept': 'application/json, text/plain, */*', 'Referer': 'https://store.oppo.com/cn/app/taskCenter/index?us=gerenzhongxin&um=hudongleyuan&uc=renwuzhongxin', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,en-US;q=0.9'}
        self.index = self.session.get(url=url,headers=headers).json()
        for i in self.index['data']['userReportInfoForm']['gifts']:
            if i['today'] == True:
                self.data = i
                break

#签到
    def report(self):
        url = 'https://store.oppo.com/cn/oapi/credits/web/report/immediately'
        headers = {'Host': 'store.oppo.com', 'Connection': 'keep-alive', 'source_type': '501',
                   'clientPackage': 'com.oppo.store', 'Cache-Control': 'no-cache',
                   'Accept': 'application/json, text/plain, */*',
                   'Referer': 'https://store.oppo.com/cn/app/taskCenter/index?us=gerenzhongxin&um=hudongleyuan&uc=renwuzhongxin',
                   'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,en-US;q=0.9'}
        data = {'amount': self.data['credits'],
                'type': self.data['type'],
                'gift': self.data['gift']}
        response = self.session.post(url= url, headers= headers, data=data).json()
        print(response)

#获取商品信息
    def getGoodMess(self, count=10):
        taskUrl = f'https://msec.opposhop.cn/goods/v1/SeckillRound/goods/{random.randint(100, 250)}'  # 随机商品
        headers = {
            'clientPackage': 'com.oppo.store',
            'Host': 'msec.opposhop.cn',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'User-Agent': 'okhttp/3.12.12.200sp1',
            'Accept-Encoding': 'gzip',
        }
        params = {
            'pageSize': count + random.randint(1, 3)
        }
        response = self.session.get(url=taskUrl, headers=headers, params=params).json()
        if response['meta']['code'] == 200:
            self.shopId = response['detail']

#浏览商品
    def gotoGoods(self):
        for i in self.shopId:
            url = 'https://msec.opposhop.cn/goods/v1/info/sku'
            params = {
                'skuId': i['skuid'],
                'secKillRoundId': '',
                'cfId': ''
            }
            response = self.session.get(url= url, params=params).json()
            time.sleep(random.randint(5,7))
            print(response)

#分享商品
    def shareGoods(self):
        url = 'https://msec.opposhop.cn/users/vi/creditsTask/pushTask?marking=daily_sharegoods'
        for i in range(4):
            time.sleep(random.randint(1, 3))
            self.session.get(url=url).json()
            print('success')

#任务中心领取
    def cashingCredits(self, marking):
        url = 'https://store.oppo.com/cn/oapi/credits/web/credits/cashingCredits'
        headers = {'Host': 'store.oppo.com', 'Connection': 'keep-alive', 'source_type': '501',
                   'clientPackage': 'com.oppo.store', 'Cache-Control': 'no-cache',
                   'Accept': 'application/json, text/plain, */*',
                   'Referer': 'https://store.oppo.com/cn/app/taskCenter/index?us=gerenzhongxin&um=hudongleyuan&uc=renwuzhongxin',
                   'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,en-US;q=0.9'}
        data = {
                'marking': marking,
                'amount': 20,
                'type': 2
        }
        sponse = self.session.post(url= url, headers= headers, data= data).json()
        if sponse['code'] == 200:
            print('领取成功!!!')
        elif sponse['code']==1000005:
            print('{}!!!'.format(sponse['errorMessage']))
        else:
            print('领取失败!!!')


#获取人物列表
    def getTaskbar(self, aid='1582'):
        url = 'https://hd.oppo.com/task/list'
        data = {'aid': aid}
        taskInfo = self.session.get(url=url,params= data).json()
        taskInfo["taskId"] = aid
        return taskInfo

#领取奖励
    def awardInt(self, taskInfo):
        url = 'https://hd.oppo.com/task/award'
        for shop in taskInfo['data']:
            if shop['t_status'] == 1:
                data = {
                    'aid': taskInfo['taskId'],
                    't_index': shop['t_index']
                }
                headers = {
                    'Host': 'hd.oppo.com', 'Connection': 'keep-alive',
                    'clientPackage': 'com.oppo.store', 'Cache-Control': 'no-cache',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Origin':'https://hd.oppo.com',
                    'Accept': '*/*',
                    'Referer': 'https://hd.oppo.com/act/m/2021/2021/realmejifendalu/index.html',
                    'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,en-US;q=0.9'
                }
                response = self.session.post(url= url, data= data, headers= headers).json()
                print(response)
                time.sleep(random.randint(2,3))
                print('{}: 奖励领取成功！'.format(shop['title']))

            elif shop['t_status'] == 0:
                print('{}: 任务未完成！'.format(shop['title']))

            elif  shop['t_status'] == 2:
                print('{}: 奖励已领取！'.format(shop['title']))
#任务中心
    def task(self):
        #签到
        if self.index['data']['userReportInfoForm']['status'] == 0:
            self.report()
            print('签到成功！')
        else:
            print('已签到过！')

        for temp in self.index['data']['everydayList']:
            time.sleep(random.randint(2,3))
            print('{},{}!'.format(temp['name'],temp['completeStatus']))
        # 浏览网页
            if temp['name'] == '浏览商品' and temp['completeStatus'] == 0:
                self.gotoGoods()
                self.cashingCredits(marking=temp['marking'])
        # 分享商品
            elif temp['name'] == '分享商品到微信' and temp['completeStatus'] == 0:
                self.shareGoods()
                self.cashingCredits(marking=temp['marking'])
            else:
                break
            #更新状态
            self.reporinfo()
        #领取奖励
        for temp in range(2):
            if self.index['data']['everydayList'][temp]['completeStatus'] == 1:
                self.cashingCredits(marking=self.index['data']['everydayList'][temp]['marking'])

            elif self.index['data']['everydayList'][temp]['completeStatus'] == 2:
                print('{}奖励已领取!!!'.format(self.index['data']['everydayList'][temp]['name']))


    #积分大乱斗完成任务代码
    def finalTask(self, taskCode, aid='1582'):
        url = 'https://hd.oppo.com/task/finish'
        data = {
            'aid': aid,
            't_index': taskCode
        }
        self.session.post(url=url, data=data).json()


#赚积分任务1(积分大乱斗)
    def task1(self):    
        aid = '1582'
        task = self.getTaskbar(aid= aid)

        for temp in task['data']:
            time.sleep(random.randint(2, 3))
        #参与欢太超级宠粉
            if temp['title'] == '分享商品' and temp['t_status'] == 0:
                self.shareGoods()
                pass
        #分享商品
            elif temp['t_status']=='0' :
                self.finalTask(temp['t_index'], aid)

        #更新数据
        time.sleep(1)
        task = self.getTaskbar(aid=aid)
        #任务领奖
        self.awardInt(task)

#积分大乱斗2
    def task3(self):
        aid = '1598'
        task = self.getTaskbar(aid=aid)
        for temp in task['data']:
            if temp['t_status']=='0' :
                time.sleep(random.randint(2, 3))
                self.finalTask(temp['t_index'], aid)

        time.sleep(1)
        task = self.getTaskbar(aid=aid)
        self.awardInt(task)

    #赚积分任务2
    def task2(self):
        aid = '1418'
        task = self.getTaskbar(aid= aid)
        for shop in task['data']:
            #签到
            if shop['title'] == '每日签到' and shop['t_status']==0:
                url = 'https://hd.oppo.com/task/finish'
                data = {
                    'aid': '1418',
                    't_index': shop['t_index']
                }
                response = self.session.post(url= url, data= data).json()
                print(response['msg'])

            #浏览商品
            if shop['title'] == '浏览商详' and shop['t_status'] == 0:
                self.gotoGoods()

        #更新数据
        task = self.getTaskbar(aid= aid)
        #领取奖励
        self.awardInt(task)
        #抽奖(待完善)
        for i in range(3):
            time.sleep(random.randint(1,2))
            url = 'https://hd.oppo.com/platform/lottery'
            data = {
                'aid': task['taskId'],
                'lid': '1307',
                'source_type': '5018',
                'isCheck': '',
                's_channel' : 'vivo'
            }
            headers = {
                'Host': 'hd.oppo.com', 'Connection': 'keep-alive',
                'clientPackage': 'com.oppo.store', 'Cache-Control': 'no-cache',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://hd.oppo.com',
                'Accept': '*/*',
                'Referer': 'https://hd.oppo.com/act/m/2021/2021/realmejifendalu/index.html',
                'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,en-US;q=0.9'
            }
            response = self.session.post(url= url,data= data, headers= headers).json()
            print(response)

#全部函数
    def runTask(self):
        self.reporinfo()
        self.getGoodMess()
        self.clockIn()
        self.task()
        self.task1()
        self.task2()
        self.task3()

#设置默认cook
    def start(self):
        self.session.headers.update({
            "User-Agent":self.dic['UA']
        })
        self.session.cookies.update({
            "Cookie":self.dic['CK']
        })
        self.runTask()
#启动接口（兼容腾讯云）
def main_handler(event, context):
    for each in accounts:
        if each['CK'] != "" and each['UA'] != "":
            huantai = HuanTai(each)
            huantai.start()


if __name__ == '__main__':
    main_handler('', '')
