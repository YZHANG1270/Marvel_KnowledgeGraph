# -*- coding:utf8 -*-
from marvel import Marvel
from marvel import exceptions
import time
import json
import ast
import csv
import yaml

import pandas as pd


class Marvel_gephi(object):
    '''use marvel, get name id, stories's count'''

    def __init__(self):
        PUBLIC_KEY = '25b558c56c28ea8839370f72250e7c31'
        PRIVATE_KEY = '0929fdf08c3134b73388825d209cc712b4657eda'
        self.path_results = r'data/all_results.json' # 所有角色的所有信息
        self.path_stories = r'data/stories.json'     # 所有故事的所有信息
        self.path_c = r'data/node_charac.csv'        # character: gephi 所需角色（节点）信息
        self.path_log = r'data/name_storielog.txt'   # log: 故事存储log
        self.path_up = r'data/update_charac.csv'     # update: 对gephi所需角色信息更新
        self.path_edg = r'data/edge_name_name_w.csv' # edge: gephi所需边信息
        self.m = Marvel(PUBLIC_KEY, PRIVATE_KEY)

    def store_charac(self):
        '''初步储存角色及相关故事数'''
        clog = []  # 请求次数较少时使用
        characters = self.m.characters
        with open(self.path_results, 'w') as f:
            for i in range(0, 1500, 100):  # 第一次请求,英雄数量1400多
                try:
                    all_characters = characters.all(limit=100, offset=i)
                    time.sleep(2)
                    print('till', i, 'insertbegin')
                    for i2 in all_characters['data']['results']:  # 存入数据
                        jsonData = json.dumps(i2)
                        f.write(jsonData)
                        f.write('\n')
                    print('ok', i)
                except exceptions.MarvelException as e:
                    print('MarvelException:', e)
                    print('bad', i, ':', i + 100)
                    clog.append(i)
                except exceptions.BadInputException as e:
                    print('BadInputException:', e)
                    print('bad', i, ':', i + 100)
                    clog.append(i)
            print('first insert,end')

        # # 请求出错时使用，一般出错的概率比较小，所以就不输出log.txt了
        # b = 0  # 请求次数
        # okl2 = []
        # while clog:
        #     for i in clog:
        #         try:
        #             all_characters = characters.all(limit=100, offset=i)
        #             time.sleep(2)
        #             print('till', i, 'insertbegin')
        #             for i2 in all_characters['data']['results']:
        #                 jsonData = json.dumps(i2)
        #                 f.write(jsonData)
        #             print('ok', i, ',delete', i)
        #             okl2.append(i)  # 删除列表元素
        #         except exceptions.MarvelException as e:
        #             print('MarvelException:', e)
        #             print('bad', i, ':', i + 100)
        #         except exceptions.BadInputException as e:
        #             print('BadInputException:', e)
        #             print('bad', i, ':', i + 100)
        #     for i3 in okl2:  # 删除列表元素
        #         clog.remove(i3)
        #     b += 1
        #     print('second insert,end,times:', b)

    def node(self):
        '''生成节点数据'''
        characters = []

        ff = open(self.path_results,'r')
        for q in ff:
            q = ast.literal_eval(q)
            characters.append([q['id'], q['name'], q['stories']['available']])  # 列表
        characters.sort(key=lambda x: x[2], reverse=True)  # 以相关故事数量降序排列

        headers = ['id', 'name', 'weight']  # 故事数量weight,角色名,id ：[1009610, 'Spider-Man', 5478]
        df = pd.DataFrame(characters,columns=headers)
        df.to_csv(self.path_c)


    def store_stories(self):
        '''存储英雄相关所有故事'''
        slog = []
        stories = self.m.stories
        # 从存入的文件中读取数据
        m1 = []
        with open(self.path_c, 'r', encoding='utf8') as f:
            f_csv = csv.reader(f)
            for r in f:
                m1.append(r.split(',')[0:3])
        m1 = m1[1:] # m1[1:] 全部跑完耗时很久

        with open(self.path_stories, 'w') as _f:
            for nameid in m1:  # nameid=[1009277, 'Domino', 296]角色id,角色名，相关故事数----接着从第六个角色开始
                for i in range(0, int(nameid[2]), 100):
                    # 第一次请求
                    try:
                        all_stories = stories.all(characters=nameid[0], offset=i, limit=100)
                        time.sleep(3)
                        print('till', i, 'insertbegin')
                        for i2 in all_stories['data']['results']:
                            jsonData = json.dumps({str(nameid[0]): i2}) # 保存character_id及相应stories
                            _f.write(jsonData)
                            _f.write('\n')
                        print('ok', i)
                    except exceptions.MarvelException as e:
                        print('MarvelException:', e)
                        print('bad', i, ':', i + 100)
                        slog.append(i)  # nameid及i
                    except exceptions.BadInputException as e:
                        print('BadInputException:', e)
                        print('bad', i, ':', i + 100)
                        slog.append(i)  # nameid及i
                print('first， insert, end')

            # # 差错处理
            # b = 0  # 总请求次数
            # okl = []
            # while slog and b < 5:
            #     for si in slog:  # 一次si不成功就自动进入下一个si
            #         try:
            #             all_stories = stories.all(characters=nameid[0], offset=si, limit=100)
            #             time.sleep(3)
            #             print('till', si, 'insertbegin')
            #             for i2 in all_stories['data']['results']:
            #                 pass # 同上处理
            #             print('ok', si, ',delete', si)
            #             okl.append(si)  # 删除请求成功的i
            #         except exceptions.MarvelException as e:
            #             print('MarvelException:', e)
            #             print('bad', si, ':', si + 100)
            #         except exceptions.BadInputException as e:
            #             print('BadInputException:', e)
            #             print('bad', si, ':', si + 100)
            #     for ok in okl:  # 删除请求成功的si
            #         slog.remove(ok)
            #     okl = []  # 格式化
            #     b += 1
            #     print('try,times:', b)
            # if slog:  # log输出
            #     with open(self.path_log, 'a+', encoding='utf8') as f:
            #         f.write(str(nameid))
            #         f.write(str(slog))
            #         f.write('\n')
            #         slog = []  # 格式化

    def add_stories(self, nameid, si):
        '''对log中信息手动抓取'''
        all_stories = self.m.stories.all(characters=nameid, offset=si, limit=100)
        time.sleep(3)
        print('till', si, 'insertbegin')
        for i2 in all_stories['data']['results']:  #
            print(i2)
            print({nameid[0]: i2})
            #{nameid[0]: i2}
        print('ok', si, ',delete', si)

    def update_charac(self):
        '''根据实际抓取数据，进行更新前面的相关故事数'''
        stories = self.m.stories

        # 从存入的文件中读取数据
        m1 = []
        with open(self.path_c, 'r', encoding='utf8') as f:
            for r in f:
                m1.append(r.split(',')[0:3])

        m1 = m1[1:] # m1[1:] 如果全部跑完耗时比较久
        c = 0
        counts = []
        for nameid in m1:
            all_stories_count = stories.all(characters=nameid[0], offset=0, limit=5)
            time.sleep(3)
            counts.append([nameid[0], all_stories_count['data']['total']])  # 更新故事数
            c += 1
            print(c)

        headers = ['nameid', 'stories_c']  # 故事id,name1id,name2id
        df = pd.DataFrame(counts, columns=headers)
        df.to_csv(self.path_up)

    def edge(self):
        '''生成便表格相关数据'''
        # csv文件生成，第二个edge文件生成
        dicn_stories = {}  # 存储故事id元组
        ff = open(self.path_stories, 'r')
        print('开始id和故事存储')
        # 存储故事id与故事名
        characters_c = []
        check = '1009610'  # 故事数最多的id
        for q2 in ff:
            q2 = yaml.load(q2)
            ckey = [ckey for ckey in q2.keys()]
            ckey = ckey[0]
            if ckey == check:
                characters_c.append((q2[ckey]['id'], q2[ckey]['title']))  # 故事数据
                dicn_stories[str(ckey)] = set(characters_c)  # 增加键值对,及数值更新
                check = ckey  # 更新人物id
            else:
                characters_c = []  # 根据key值清空列表
                characters_c.append((q2[ckey]['id'], q2[ckey]['title']))  # 故事数据
                check = ckey
        print('存储完毕。开始获取两两角色相关数据')

        # 从存入的节点文件中读取id数据
        m1 = []
        with open(self.path_c, 'r', encoding='utf8') as f:
            for r in f:
                m1.append(r.split(',')[0:3])
        m1 = m1[1:] # m1[1:] 全部跑完很耗时间
        # 两两角色相关故事数存储
        m2 = []
        for ind, chaid in enumerate(m1):  # nameid=[1009277, 'Domino', 296]角色id,角色名
            try:
                pre = dicn_stories[str(chaid[0])]  # 获取角色对应的故事

                for ind2, chaid2 in enumerate(m1):
                    if ind < ind2:
                        try:
                            nex = dicn_stories[str(chaid2[0])]  # 获取角色对应数据
                            count = len(pre & nex)
                            if count > 0:
                                m2.append([chaid[0], chaid2[0], count])
                        except:
                            print('故事收集还不完整，右边英雄的故事漏掉了')
            except:
                print('故事收集还不完整，左边英雄的故事漏掉了')

        headers = ['source', 'target', 'weight']  # name1id,name2id，同在一个故事的数量
        df = pd.DataFrame(m2, columns=headers)
        df.to_csv(self.path_edg)

        print('存储结束')


if __name__=="__main__":
    import os
    os.chdir('C:/Users/Yi/Desktop/Marvel_KnowledgeGraph')

    cool = Marvel_gephi()

    # cool.store_charac() #存储人物数据
    # print('人物储存完毕')

    # cool.node() #生成节点数据
    # print('节点数据生成完毕')

    # cool.store_stories()#存储故事数据
    # print('故事存储完毕，请检查log文件')

    # cool.update_charac()#更新故事数
    # print('人物故事更新完成')

    # cool.edge()#生成边数据
    # print('边数据完成')

