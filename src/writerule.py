#!/usr/bin/env python
# -*- coding:utf-8
import sys
import os
import requests
import json
reload(sys)
sys.setdefaultencoding( "utf-8" )


start=1771
rule={"1":u"确认用户身份      " ,
      "2":u"确认卡是否是本人  " ,
      "3":u"肯定回答          " ,
      "4":u"否定回答          " ,
      "5":u"坐席自我介绍      " ,
      "6":u"继续营销|产品介绍 " ,
      "7":u"确认送货地址      " ,
      "8":u"收货提醒          " ,
      "9":u"问题              " ,
      "10":u"用户问:           " ,
      "11":u"坐席答            " ,
      "12":u"坐席确认          " ,
      "13":u"激活过程          " ,
      "14":u"其它              " }

#for (d ,x) in rule.items():
      #key=input("\nkey:");
      #if(str(key) =="1"):
      #    print rule[str(key)];
#      print d + "---" + x,
fo=open(u"content内容.txt","r");
fonew=open(u"识别.txt","a+")
lines = fo.readlines();
print len(lines)
for n in range (start , len(lines)) :
      line=lines[n]
      if( line.find(u"坐席")<0 and line.find(u"客户")<0):
            fonew.write(lines[n]);
            continue
      for item in ['"1": "确认用户身份      "     "8": "收货提醒          " ',  \
'"2": "确认卡是否是本人  "     "9": "问题              "' ,                    \
'"3": "肯定回答          "     "10": "用户问:           "',                    \
'"4": "否定回答          "     "11": "坐席答            "',                    \
'"5": "坐席自我介绍      "     "12": "坐席确认          "',                    \
'"6": "继续营销|产品介绍 "     "13": "激活过程          "',                    \
'"7": "确认送货地址      "     "14": "其它              "']:                   \
         print unicode(item.decode('utf-8')).encode('gbk')
      if(n>=1):
            print (n-1),lines[n-1].decode("utf-8"),
      print (n),line.decode("utf-8"),
      if(n+1<=len(lines)):
            print (n+1),lines[n+1].decode("utf-8"),


      key = raw_input(unicode('\n请选择类型：','utf-8').encode('gbk')).decode(sys.stdin.encoding)
      print '\n'
      
      if(not  rule.has_key(str(key))):
            key = raw_input(u"key : 1-E 请选择类型:").decode(sys.stdin.encoding)
      fonew.write(rule[str(key)] + "  _  " + lines[n])
      fonew.flush()
