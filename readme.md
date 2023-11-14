## 开发工具

#### 1、 curl to requests https://curlconverter.com/

#### 2、Chrome浏览器  https://www.google.com/chrome/

## 项目说明

> 爬虫逆向和示例

## 一、常见逆向类型

### 1、阿里系 awc_sc__v2 项目示例

> 清除cookie，重新加载，找到设置的相关代码

### 2、请求体加密

> 使用xhr监听打断点，找到请求拦截器对应的加密代码

### 3、请求头签名认证

> 头部参数加密，需要模拟加密，加密参数一般是最开始的某段js代码进行加密的内容
> 1. 搜索关键字 decrypt encrypt JSON.parse 搜索自带的关键字
> 2. 搜索路径
> 3. 跟栈
     >
     >    --> 注意栈和栈之间是否从明文变为密文
     >
     >    --> 异步栈，看到Promise，去找回调方法

### 4、请求体和响应数据都有加密

```
# 一般需要算法包，使用
npm install crypto-js
# 引用
const CryotoJs = require('crypto-js')
```

> 1. 确定请求地址的栈中是否存在混淆JS
> 2. 搜索decrypt(判断网站是否为算法加密 一般为实例对象》实例方法 比如 a(实例对象).搜索decrypt
> 3. 搜索路径+json.parse(  注意：不是内置的方法函数的界面方法或者函数
> 4. 跟栈response对象的拦截器对象

### 二、排坑记录

#### 1. 逆向AES解密时，就近找到了秘钥，但是本地运行失败，可以通过debug反向输出秘钥

```js
// 输出words
k = CryptoJS.enc.Utf8.parse("Dt8j9wGw%6HbxfFn")
// 反向解析为字符串
k.toString(CryptoJS.enc.Utf8)

```

### 三、 python调用js的方法

> 推荐使用PyExecJS2+nodejs环境

```shell
# 安装 https://pypi.org/project/PyExecJS2/
pip install PyExecJS2
```

## 网站汇总

| 网站             | url                                                                                                    | 项目位置                        | 分类                 | 逆向说明                                                                                         |
|:---------------|:-------------------------------------------------------------------------------------------------------|:----------------------------|--------------------|:---------------------------------------------------------------------------------------------|
| 采招网            | [链接](https://search.bidcenter.com.cn/)                                                                 | [bidcenter](./bidcenter)    | 响应数据加密             | 响应数据加密，使用标准的AES加密，依赖crypto-js                                                                |
| 申万宏源证券         | [链接](https://www.swhysc.com/swhysc/financial/marginTradingList?channel=00010017000300020001&listId=2 ) | [swhysc](./swhysc)          | 响应数据加密             | 响应数据加密，加密版AES ，依赖crypto-js                                                                   |
| 行行查            | [链接](https://www.hanghangcha.com/)                                                                     | [hanghancha](./hanghangcha) | 响应数据加密             | 响应数据加密，使用标准的AES加密，依赖crypto-js                                                                |
| 烯牛数据           | [链接]( https://www.xiniudata.com/industry/newest?from=data)                                             | [xiniudata](./xiniudata)    | 需要登录，请求体加密，响应数据加密  | 请求体和响应数据都有加密,通过搜索关键词来找出加密的代码 ，依赖crypto-js                                                    |
| 网易云            | [链接](https://music.163.com/)                                                                           | [wangyiyun](./wangyiyun)    | 请求体加密              | 请求体进行了加密,通过xhr监听获取加密的地方，依赖crypto-js                                                          |
| 巨潮资讯数据中心       | [链接](https://webapi.cninfo.com.cn/#/marketDataDate)                                                    | [cninfo](./cninfo)          | 请求头加密              | 请求头进行了验证Accept-EncKey，使用了加密的AES，依赖crypto-js                                                  |
| 产业政策大数据平台      | [链接](http://www.spolicy.com/)                                                                          | [spolicy](./spolicy)        | 请求体加密              | 请求体加密，使用xhr监听打断点，找到请求拦截器对应的加密代码                                                              |
| 雪球             | [链接]( https://xueqiu.com/)                                                                             | [xueqiu](./xueqiu)          | cookie验证           | cookie验证，阿里系awc_sc__v2，清除cookie，重新加载，找到设置的相关代码                                               |
| 极简壁纸           | [链接]( https://bz.zzzmh.cn/index)                                                                       | [zzzmh](./zzzmh)            | 响应数据加密             | 响应数据加密，通过xhr断点，找到响应数据解密的地方，解密依赖window环境，使用jsdom来模拟,要下载图片需要搜索关键词down-span 找到设置下载地址的js         |
| 艺恩             | [链接](https://www.endata.com.cn/BoxOffice/BO/Year/index.html)                                           | [endata](./endata)          | 响应数据加密             | 响应数据加密，通过xhr断点或者JSON.parse+路径搜索找到加密位置                                                        |
| 全国建筑市场监管公共服务平台 | [链接](https://jzsc.mohurd.gov.cn/data/project)                                                          | [mohurd](./mohurd)          | 响应加密               | 关键词搜索JSON.parse + 路径搜索确定加密地址，比较坑的是秘钥地址变更了， 通过**f.toString(d.a.enc.Utf8)找到新的秘钥** ,依赖crypto-js |
| 1688找工厂        | [链接](https://sale.1688.com/factory/home.html)                                                          | [1688](./1688)              | 请求cookie和请求体sign签名 | 请求体签名和cookie认证                                                                               |通过搜索关键词sign: 和请求路径找到对应的js