# Update
个人demo项目，不断完善中...

两大块内容：**Marvel API**  和  **Knowledge Graph 知识图谱** 



**2019/04/08** 

- [x] Marvel 官网注册开发者账号 [[link](https://developer.marvel.com/)] （my developer account: yzhang1270）
- [x] Get a Key 获取公钥、私钥
- [x] python package: pip install marvel
- [x] 调试marvel，读接口参数文档 [[link](https://developer.marvel.com/docs)]，生成 Marvel API 调用说明：**marvel_api.ipynb** 
- [x] 多维度数据的整理分析：参数传递```captain america``` ，JSON返回数据：**json_captain_america.txt** 



##### Tasks

- [ ] 知识图谱 - 理论知识总结	输出到个人网站
- [ ] 图谱工具 - Neo4j 使用总结	输出到个人网站
- [ ] Cypher 语法总结	输出到个人网站
- [ ] 漫威API 熟悉
- [ ] 数据收集
- [ ] 建立图谱代码



##### 参考

- [ ] 超棒的marvel知识图谱展示 [[link](https://graphics.straitstimes.com/STI/STIMEDIA/Interactives/2018/04/marvel-cinematic-universe-whos-who-interactive/index.html)]
- [ ] 漫威API官网 [[link](https://developer.marvel.com/)]
- [ ] neo4j的相关博客 [[link](https://tbgraph.wordpress.com/)]
- [ ] 漫威，DC人物大全 [[link](https://www.douban.com/note/436744247/)] 
- [ ] 漫威人物关系图、观影顺序图 [[link](http://www.360doc.com/content/16/0528/19/29576369_563071456.shtml)]



##### 制作教程

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



如果之后将作品对外展示，请务必注意：

1. **请求上限** 3000次/天，并且需要设定请求来源网址（referrer）。建议通过自建缓存，以减少请求量
2. 需要在所有用到接口数据的页面上标注 **"Data provided by Marvel. © 2014 Marvel"**
3. 需提供到 Marvel 官网的反链（**http://marvel.com**）
4. 返回接口里的图片 URL 不是直接可访问的，需添加上所需图片尺寸和文件类型，拼出完整路径