# pwdbud

## 0x00
>在挖SRC时，尝试top字典无果后，可以根据域名、公司名等因素来生成特定的字典

## 0x01
PwdBUD仅需三个参数，以域名或公司名为索引生成字典。
## 0x02
~~~shell
-d --domain    #域名

-c --company   #公司名

-o --outfile   #必须，输出文件
~~~
~~~shell
python pwdbud.py -d jd -c jingdong -o res.txt
~~~

## 0x03
~~~shell
摘录部分生成的密码
Jd20170105
Jd20170106
Jd19990521
Jd19990522
jD041008
jD041009
Jingdong@zxczxc
Jingdong@l123456
jingdong_zhoujie
jingdong_chenjianhua
Jingdong2013.
Jingdong2014.
~~~
## ToDo
~~~shell
已完成的规则:
域名+工号1   Jd20210101
域名+top1000   Jdadmin
域名+birth    jd19820101
公司名称+年份    Jingdong2022
公司名+特殊字符+年份    Jingdong@2019
公司名+特殊字符+top1000弱口令    Jingdong@2019
公司名称+年份+特殊字字符    Jingdong2021@
~~~
参考火线听火沙龙十七期