# pwdbud

## 0x00
>在挖SRC时，对登录界面尝试过top字典无果后，可以根据域名、公司名或其他元素来生成特定的字典

## 0x01
PwdGEN要做的是大而全，不必指定生成规则，全部生成就完事儿了。毕竟弱口令爆破这事儿是玄学，用户指不定用的是哪个奇奇怪怪的密码。
## 0x02
~~~shell
-d --domain    #域名

-c --company   #公司名

-e --element   #其他元素

-o --outfile   #必须，输出文件
~~~
~~~shell
python pwdgen.py -d jd -c jingdong -o res.txt
~~~

## 0x03


## ToDo

