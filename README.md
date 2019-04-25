  ![](https://github.com/YZHANG1270/Marvel_KnowledgeGraph/blob/master/img/hero.png?raw=true)
[点我！快点我！](https://graphics.straitstimes.com/STI/STIMEDIA/Interactives/2018/04/marvel-cinematic-universe-whos-who-interactive/index.html)


# Marvel Knowledge Graph
个人demo项目，走向未知，不断完善中...

#### Tasks

- [x] 漫威API 熟悉
- [x] 知识图谱科普帖 [[link](http://codewithzhangyi.com/2019/04/23/knowledge-graph-intro/)]
- [ ] py2neo，cypher 语法总结
- [x] Marvel 数据收集
- [ ] 建立图谱代码
- [x] 想玩一下的工具：Neo4j ; Gephi



#### Update

**2019/04/08** 

- [x] Data source: **Marvel API** [[link](https://developer.marvel.com/)] 
- [x] Marvel 官网注册开发者账号 [[link](https://developer.marvel.com/)] （my developer account: yzhang1270）
- [x] Get a Key 获取公钥、私钥
- [x] python package: pip install marvel
- [x] 调试marvel，读接口参数文档 [[link](https://developer.marvel.com/docs)]，生成 Marvel API 调用说明：*marvel_api.ipynb* 
- [x] 多维度数据的整理分析：参数传递`captain america` ，JSON返回数据：*json_captain_america.txt*  

**2019/04/25** 

- [x] **功能：** 存储英雄及相关故事信息 - *marvel_gephi.py* 
- [x] **存储：** 存储英雄及相关故事信息 - *data/.* 
- [x] gephi 下载、安装、成功运行
- [x] gephi 数据准备：data/gephi/.
  - [x] 节点数据：[id, name, story num]
  - [x] 关系数据：[character1, character2, story num]
- [x] gephi 绘制英雄图谱 [[tutorial](https://gitee.com/crossin/snippet/tree/master/marvel-gephi)] ![](https://github.com/YZHANG1270/Marvel_KnowledgeGraph/blob/master/img/gephi.png?raw=true) 



#### 拓展

- [ ] 超惊艳！必看！Marvel 图谱可视化 [[link](https://graphics.straitstimes.com/STI/STIMEDIA/Interactives/2018/04/marvel-cinematic-universe-whos-who-interactive/index.html)]
- [ ] neo4j的相关博客 [[link](https://tbgraph.wordpress.com/)]
- [ ] 漫威，DC人物大全 [[link](https://www.douban.com/note/436744247/)] 
- [ ] 漫威人物关系图、观影顺序图 [[link](http://www.360doc.com/content/16/0528/19/29576369_563071456.shtml)]
- [ ] gephi 图谱可视化demo [[link](https://exploring-data.com/vis/programmers-search-relations/)]

 

#### 其他制作教程

- [ ] [part1](https://medium.com/neo4j/create-a-data-marvel-develop-a-full-stack-application-with-spring-and-neo4j-part-1-350f0f7e6609) 
- [ ] [part2](https://medium.com/neo4j/create-a-data-marvel-develop-a-full-stack-application-with-spring-and-neo4j-part-2-12186b929cb2?sk=dc964e4bf6496141730dde704bcabb47) 
- [ ] [part3](https://medium.com/neo4j/create-a-data-marvel-develop-a-full-stack-application-with-spring-and-neo4j-part-3-3ac3380e0edb) 
- [ ] [part4](https://medium.com/neo4j/create-a-data-marvel-part-4-how-to-design-the-application-874ba6ea08a5) 
- [ ] [part5](https://medium.com/neo4j/create-a-data-marvel-part-5-writing-the-domain-classes-27a39ab0666a) 
- [ ] [part6](https://medium.com/neo4j/create-a-data-marvel-part-6-developing-more-entities-be5aeab1817a) 
- [ ] [part7](https://medium.com/neo4j/create-a-data-marvel-part-7-connecting-the-graph-bc7ed9e2b843) 
- [ ] [part8](https://medium.com/neo4j/create-a-data-marvel-part-8-controlling-and-servicing-our-comic-endpoints-4dd08b81e0e) 
- [ ] [part9](https://medium.com/neo4j/create-a-data-marvel-part-9-building-the-webpage-for-comics-1ceb26f8a5be) 
- [ ] [part10](https://medium.com/neo4j/creating-a-data-marvel-part-10-lessons-and-resources-8ffb5bf0ad1) 



#### Attention

1. 请求上限 3000次/天，并且需要设定请求来源网址（referrer）
2. 需要在所有用到接口数据的页面上标注 **"Data provided by Marvel. ©Marvel"** 
3. 需提供到 Marvel 官网（ **http://marvel.com** ） 
4. 返回接口里的图片 URL 不是直接可访问的，需添加上所需图片尺寸和文件类型，拼出完整路径