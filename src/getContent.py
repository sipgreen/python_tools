#!/usr/bin/env python
# -*- coding:utf-8
import sys
import requests
import json
reload(sys)
sys.setdefaultencoding( "utf-8" )

fo = open(u"rule.txt", "w")
rule={"1":u"确认用户身份"      ,
"2":u"确认卡是否是本人"  ,
"3":u"肯定回答"          ,
"4":u"否定回答"          ,
"5":u"坐席自我介绍"      ,
"6":u"继续营销|产品介绍" ,
"7":u"确认送货地址"      ,
"8":u"收货提醒"          ,
"9":u"问题"              ,
"A":u"用户问:"           ,
"B":u"坐席答"            ,
"C":u"坐席确认"          ,
"D":u"激活过程"          ,
"E":u"其它"              }

fo.write(rule["1"])

numbers=['CZ_1519060312165900001000',
'CZ_1519060312165900001001']

header={"Content-Type":"application/json"}


fo = open(u"content内容2.txt", "w")
for number in numbers:
  payload='{ "query": { "wildcard": { "serialNumber": { "value": "'+number+'", "boost": 2.0 } } } }'
  r = requests.get('http://172.30.66.18:9200/audio/_search', data=payload, headers=header)
  obj=json.loads(r.text)

  for hit in obj['hits']['hits']:
        fo.write("_id: " + hit['_id']+"------------------------------------------------------\n")
        fo.write('\n')
        if(hit['_source']['sttInfo'].has_key('sttSentences')):
            izuoxi=obj['hits']['hits'][0]['_source']['sttInfo']['sttSentences'][0]['channel'];
            zuoxi = u'【坐席】' ;
            for t in obj['hits']['hits'][0]['_source']['sttInfo']['sttSentences']:
                zuoxi = '【坐席】' ;
                if( t['channel']==1 ):
                   zuoxi=u'【客户】';
                if( t['channel']!=izuoxi ):
                   #fo.write('\r\n')
                   izuoxi=t['channel']
                fo.write('"' +zuoxi + '":  ' + t['centent'] +'' +"\n")

  fo.write('\n')
  fo.write('\n')
  fo.write('\n')
  fo.write('\n')
#fo.write(r.text)
#['hits']['_source']


