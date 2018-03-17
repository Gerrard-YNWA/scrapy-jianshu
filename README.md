# scrapy-jianshu
scrapy爬取简书主页信息，后端存储到MongoDB，用flask提供api访问

### 依赖
* scrapy
* pymongo
* flask

运行一次
```
scrapy crawl homepage
```

后台定时运行
```
nohup python main.py &
```

flask api 服务
```
python api.py
```

客户端请求
```
 curl "http://127.0.0.1:6666/hot?page=1&size=2"
{
  "code": 0, 
  "data": [
    {
      "article_abstract": "\n      3月12日，湖南永州，某投资公司高管黄某驾奔驰冲上人行道，撞倒一名女性路人，致其当场死亡。（澎湃新闻） 要说到一般情况，肇事司机都会急急忙忙打120或报警，心态应该是很紧张才...\n    ", 
      "article_link": "/p/e2fa6c4afb2a", 
      "author": "太秭帝", 
      "author_link": "/u/cf25dcd83f26", 
      "category": "社会热点", 
      "comments": 225, 
      "like": 155, 
      "post_time": "2018-03-15T02:19:07+08:00", 
      "reward": 3, 
      "title": "高管开奔驰撞死女路人，竟自信微笑称：“我买的全保，这些都买了”", 
      "views": 9706
    }, 
    {
      "article_abstract": "\n      今年3月6号，简书官方账号发布了一则消息：《简书新版发现页文章推荐系统上线公告》，宣布了在3月15日简书首页将会退出历史舞台，进而用更加现代化的机器算法取而代之。 遥想当年，...\n    ", 
      "article_link": "/p/52e23b6f662e", 
      "author": "田宝谈写作", 
      "author_link": "/u/09c373f051cf", 
      "category": "读书", 
      "comments": 106, 
      "like": 155, 
      "post_time": "2018-03-15T08:48:58+08:00", 
      "reward": 5, 
      "title": "没有首页后的简书怎么玩？这份攻略送给你", 
      "views": 6307
    } 
  ], 
  "msg": "success"
}

```

