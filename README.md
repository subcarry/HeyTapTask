# <p align="center">HeyTapTask</p>

## 免责声明
- 本仓库发布的HeyTapTask项目中涉及的任何脚本，仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断.

- 所有使用者在使用HeyTapTask项目的任何部分时，需先遵守法律法规。对于一切使用不当所造成的后果，需自行承担.对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害.

- 如果任何单位或个人认为该项目可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关文件.

- 任何以任何方式查看此项目的人或直接或间接使用该HeyTapTask项目的任何脚本的使用者都应仔细阅读此声明。本人保留随时更改或补充此免责声明的权利。一旦使用并复制了任何相关脚本或HeyTapTask项目的规则，则视为您已接受此免责声明.

您必须在下载后的24小时内从计算机或手机中完全删除以上内容.

> 您使用或者复制了本仓库且本人制作的任何脚本，则视为`已接受`此声明，请仔细阅读



## 环境

[Python3](https://www.python.org/) >= 3.6.8

## 已实现功能
* [x] 每日签到
* [x] 每日浏览商品任务
* [x] 每日分享商品任务
* [x] 赚积分活动
* [x] 积分大作战realme
* [x] 积分大作战HeyTap

## 函数说明
  self.reporinfo()   任务中心-签到的信息其中['today']用于判断是否为今天
  self.getGoodMess() 获取商品信息，用于浏览商品时使用   
  self.task()        完成任务中心任务
  self.task1()       完成积分大乱斗（realme）任务
  self.task2()       完成赚积分
  self.task3()       完成积分大乱斗（Heytap）任务
  
#### 一、Linux部署
```bash
yum install python3 -y

yum install git -y

git clone https://ghproxy.com/https://github.com/Esdeathaili/huantai.git   # 国内git较慢，故添加代理前缀

cd HeyTapTask

vi Ht_config.py
```

##### 编辑配置文件(本地/云函数)
```text
# 推荐方案(config.py)
{
    'user':'',                                                  # 自定义备注(为了区分账号，包括未登录状态下)
    'CK':'source_type=xxx;TOKENSID=TOKEN_xxxx;app_param=xxxx',  # 用户环境变量 Cookie,建议全部粘贴,且顺序不可乱
    'UA':'UA'                                                   # 用户环境变量 User-Agent
}
```

##### 变量获取
- CK和UA信息需自行抓包，欢太商城 -> 我的 -> 任务中心 -> 领券中心
- 抓包地址:`https://store.oppo.com/cn/oapi/users/web/checkPeople/isNewPeople`
