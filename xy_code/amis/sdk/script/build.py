#coding=UTF-8
import io
import json

obj={
    "02": {
        "status": 0,
        "msg": "OK",
        "data": {
            "options": [
                {
                    "value": "0201",
                    "label": "刑事一审"
                },
                {
                    "value": "0202",
                    "label": "刑事二审"
                },
                {
                    "children": [
                        {
                            "value": "0204",
                            "label": "刑事依职权再审审查"
                        },
                        {
                            "value": "0205",
                            "label": "刑事申诉再审审查"
                        },
                        {
                            "value": "0206",
                            "label": "刑事抗诉再审审查"
                        },
                        {
                            "value": "0207",
                            "label": "刑事再审"
                        }
                    ],
                    "value": "0203",
                    "label": "刑事审判监督"
                },
                {
                    "value": "0208",
                    "label": "申请没收违法所得"
                },
                {
                    "children": [
                        {
                            "value": "0210",
                            "label": "死刑复核"
                        },
                        {
                            "value": "0211",
                            "label": "法定刑以下判处刑罚复核"
                        },
                        {
                            "value": "0212",
                            "label": "特殊假释复核"
                        }
                    ],
                    "value": "0209",
                    "label": "刑事复核"
                },
                {
                    "children": [
                        {
                            "value": "0214",
                            "label": "申请强制医疗审查"
                        },
                        {
                            "value": "0215",
                            "label": "解除强制医疗审查"
                        },
                        {
                            "value": "0216",
                            "label": "强制医疗复议"
                        },
                        {
                            "value": "0217",
                            "label": "强制医疗监督"
                        }
                    ],
                    "value": "0213",
                    "label": "强制医疗"
                },
                {
                    "children": [
                        {
                            "value": "0219",
                            "label": "停止执行死刑请求审查"
                        },
                        {
                            "value": "0220",
                            "label": "依职权停止执行死刑"
                        },
                        {
                            "value": "0221",
                            "label": "停止执行死刑调查"
                        },
                        {
                            "value": "0222",
                            "label": "停止执行死刑调查审查"
                        }
                    ],
                    "value": "0218",
                    "label": "停止执行死刑"
                },
                {
                    "children": [
                        {
                            "value": "0224",
                            "label": "刑罚与执行变更审查"
                        },
                        {
                            "value": "0225",
                            "label": "刑罚与执行变更监督"
                        },
                        {
                            "value": "0226",
                            "label": "刑罚与执行变更备案"
                        }
                    ],
                    "value": "0223",
                    "label": "刑罚与执行变更"
                },
                {
                    "value": "0227",
                    "label": "其他"
                },
                {
                    "children": [
                        {
                            "value": "0229",
                            "label": "申请安置教育审查"
                        },
                        {
                            "value": "0230",
                            "label": "解除安置教育审查"
                        },
                        {
                            "value": "0231",
                            "label": "安置教育复议"
                        },
                        {
                            "value": "0232",
                            "label": "安置教育监督"
                        }
                    ],
                    "value": "0228",
                    "label": "安置教育"
                }
            ]
        }
    },
    "03": {
        "status": 0,
        "msg": "OK",
        "data": {
            "options": [
                {
                    "value": "0301",
                    "label": "民事一审"
                },
                {
                    "value": "0302",
                    "label": "民事二审"
                },
                {
                    "children": [
                        {
                            "value": "0304",
                            "label": "民事依职权再审审查"
                        },
                        {
                            "value": "0305",
                            "label": "民事申诉再审审查"
                        },
                        {
                            "value": "0306",
                            "label": "民事抗诉再审审查"
                        },
                        {
                            "value": "0307",
                            "label": "民事再审"
                        }
                    ],
                    "value": "0303",
                    "label": "民事审判监督"
                },
                {
                    "value": "0308",
                    "label": "第三人撤销之诉"
                },
                {
                    "children": [
                        {
                            "value": "0310",
                            "label": "选民资格"
                        },
                        {
                            "value": "0311",
                            "label": "宣告失踪、宣告死亡"
                        },
                        {
                            "value": "0312",
                            "label": "财产代管人申请变更代管"
                        },
                        {
                            "value": "0313",
                            "label": "行为能力认定"
                        },
                        {
                            "value": "0314",
                            "label": "监护人指定异议"
                        },
                        {
                            "value": "0315",
                            "label": "监护关系变更"
                        },
                        {
                            "value": "0316",
                            "label": "认定财产无主"
                        },
                        {
                            "value": "0317",
                            "label": "实现担保物权"
                        },
                        {
                            "value": "0318",
                            "label": "调解协议司法确认"
                        },
                        {
                            "value": "0319",
                            "label": "设立海事赔偿责任限制基金"
                        },
                        {
                            "value": "0320",
                            "label": "海事债权登记与受偿"
                        },
                        {
                            "value": "0321",
                            "label": "撤销仲裁裁决"
                        },
                        {
                            "value": "0322",
                            "label": "申请确认仲裁协议效力"
                        },
                        {
                            "value": "0323",
                            "label": "民事特别程序监督"
                        }
                    ],
                    "value": "0309",
                    "label": "特别程序"
                },
                {
                    "children": [
                        {
                            "value": "0325",
                            "label": "船舶优先权催告"
                        },
                        {
                            "value": "0326",
                            "label": "公示催告"
                        }
                    ],
                    "value": "0324",
                    "label": "催告"
                },
                {
                    "children": [
                        {
                            "value": "0328",
                            "label": "申请支付令审查"
                        },
                        {
                            "value": "0329",
                            "label": "支付令监督"
                        }
                    ],
                    "value": "0327",
                    "label": "督促"
                },
                {
                    "value": "0330",
                    "label": "其他"
                },
                {
                    "children": [
                        {
                            "value": "0332",
                            "label": "人身安全保护令申请审查"
                        },
                        {
                            "value": "0333",
                            "label": "人身安全保护令变更"
                        }
                    ],
                    "value": "0331",
                    "label": "人身安全保护令"
                }
            ]
        }
    },
    "01": {
        "status": 0,
        "msg": "OK",
        "data": {
            "options": [
                {
                    "children": [
                        {
                            "value": "0102",
                            "label": "刑事提级管辖"
                        },
                        {
                            "value": "0103",
                            "label": "刑事指定管辖"
                        }
                    ],
                    "value": "0101",
                    "label": "刑事管辖"
                },
                {
                    "children": [
                        {
                            "value": "0105",
                            "label": "民事提级管辖"
                        },
                        {
                            "value": "0106",
                            "label": "民事指定管辖"
                        },
                        {
                            "value": "0107",
                            "label": "民事移交管辖审批"
                        },
                        {
                            "value": "0108",
                            "label": "民事管辖协商"
                        },
                        {
                            "value": "0109",
                            "label": "民事管辖上诉"
                        },
                        {
                            "value": "0110",
                            "label": "民事管辖监督"
                        }
                    ],
                    "value": "0104",
                    "label": "民事管辖"
                },
                {
                    "children": [
                        {
                            "value": "0112",
                            "label": "行政提级管辖"
                        },
                        {
                            "value": "0113",
                            "label": "行政指定管辖"
                        },
                        {
                            "value": "0114",
                            "label": "行政管辖上诉"
                        }
                    ],
                    "value": "0111",
                    "label": "行政管辖"
                },
                {
                    "children": [
                        {
                            "value": "0116",
                            "label": "行政赔偿提级管辖"
                        },
                        {
                            "value": "0117",
                            "label": "行政赔偿指定管辖"
                        },
                        {
                            "value": "0118",
                            "label": "行政赔偿管辖协商"
                        },
                        {
                            "value": "0119",
                            "label": "行政赔偿管辖上诉"
                        }
                    ],
                    "value": "0115",
                    "label": "行政赔偿管辖"
                }
            ]
        }
    },
    "06": {
        "status": 0,
        "msg": "OK",
        "data": {
            "options": [
                {
                    "children": [
                        {
                            "value": "0602",
                            "label": "认可与执行台湾地区法院裁判审查"
                        },
                        {
                            "value": "0603",
                            "label": "认可与执行台湾地区仲裁裁决审查"
                        },
                        {
                            "value": "0604",
                            "label": "认可与执行香港特别行政区法院裁判审查"
                        },
                        {
                            "value": "0605",
                            "label": "认可与执行香港特别行政区仲裁裁决审查"
                        },
                        {
                            "value": "0606",
                            "label": "认可与执行澳门特别行政区法院裁判审查"
                        },
                        {
                            "value": "0607",
                            "label": "认可与执行澳门特别行政区仲裁裁决审查"
                        },
                        {
                            "value": "0608",
                            "label": "认可与执行审查复议"
                        },
                        {
                            "value": "0609",
                            "label": "其他认可与执行审查"
                        }
                    ],
                    "value": "0601",
                    "label": "认可与执行申请审查"
                },
                {
                    "children": [
                        {
                            "value": "0611",
                            "label": "请求台湾地区送达文书审查"
                        },
                        {
                            "value": "0612",
                            "label": "请求香港特别行政区法院送达文书审查"
                        },
                        {
                            "value": "0613",
                            "label": "请求澳门特别行政区法院送达文书审查"
                        },
                        {
                            "value": "0614",
                            "label": "台湾地区请求送达文书审查"
                        },
                        {
                            "value": "0615",
                            "label": "协助台湾地区送达文书"
                        },
                        {
                            "value": "0616",
                            "label": "香港特别行政区法院请求送达文书审查"
                        },
                        {
                            "value": "0617",
                            "label": "协助香港特别行政区法院送达文书"
                        },
                        {
                            "value": "0618",
                            "label": "澳门特别行政区法院请求送达文书审查"
                        },
                        {
                            "value": "0619",
                            "label": "协助澳门特别行政区法院送达文书"
                        }
                    ],
                    "value": "0610",
                    "label": "送达文书"
                },
                {
                    "children": [
                        {
                            "value": "0621",
                            "label": "请求台湾地区调查取证审查"
                        },
                        {
                            "value": "0622",
                            "label": "请求香港特别行政区调查取证审查"
                        },
                        {
                            "value": "0623",
                            "label": "请求澳门特别行政区法院调查取证审查"
                        },
                        {
                            "value": "0624",
                            "label": "台湾地区请求调查取证审查"
                        },
                        {
                            "value": "0625",
                            "label": "协助台湾地区调查取证"
                        },
                        {
                            "value": "0626",
                            "label": "香港特别行政区请求调查取证审查"
                        },
                        {
                            "value": "0627",
                            "label": "协助香港特别行政区调查取证"
                        },
                        {
                            "value": "0628",
                            "label": "澳门特别行政区法院请求调查取证审查"
                        },
                        {
                            "value": "0629",
                            "label": "协助澳门特别行政区法院调查取证"
                        }
                    ],
                    "value": "0620",
                    "label": "调查取证"
                },
                {
                    "children": [
                        {
                            "value": "0631",
                            "label": "接收在台湾地区被判刑人"
                        },
                        {
                            "value": "0632",
                            "label": "向台湾地区移管被判刑人"
                        }
                    ],
                    "value": "0630",
                    "label": "被判刑人移管"
                },
                {
                    "children": [
                        {
                            "value": "0634",
                            "label": "接收台湾地区移交罪赃"
                        },
                        {
                            "value": "0635",
                            "label": "向台湾地区移交罪赃"
                        }
                    ],
                    "value": "0633",
                    "label": "罪脏移交"
                }
            ]
        }
    },
    "07": {
        "status": 0,
        "msg": "OK",
        "data": {
            "options": [
                {
                    "children": [
                        {
                            "value": "0702",
                            "label": "承认与执行外国法院裁判审查"
                        },
                        {
                            "value": "0703",
                            "label": "承认与执行国外仲裁裁决审查"
                        },
                        {
                            "value": "0704",
                            "label": "其他承认与执行审查"
                        }
                    ],
                    "value": "0701",
                    "label": "承认与执行申请审查"
                },
                {
                    "children": [
                        {
                            "value": "0706",
                            "label": "外国法院请求送达文书审查"
                        },
                        {
                            "value": "0707",
                            "label": "送达外国法院文书"
                        },
                        {
                            "value": "07048",
                            "label": "请求外国法院送达文书审查"
                        }
                    ],
                    "value": "0705",
                    "label": "送达文书"
                },
                {
                    "children": [
                        {
                            "value": "0710",
                            "label": "外国法院请求调查取证审查"
                        },
                        {
                            "value": "0711",
                            "label": "外国法院请求调查取证实施"
                        },
                        {
                            "value": "0712",
                            "label": "请求外国法院调查取证审查"
                        }
                    ],
                    "value": "0709",
                    "label": "调查取证"
                },
                {
                    "children": [
                        {
                            "value": "0714",
                            "label": "接收在外国被判刑人"
                        },
                        {
                            "value": "0715",
                            "label": "向外国移管被判刑人"
                        }
                    ],
                    "value": "0713",
                    "label": "被判刑人移管"
                },
                {
                    "children": [
                        {
                            "value": "0717",
                            "label": "请求外国引渡"
                        },
                        {
                            "value": "0718",
                            "label": "协助外国引渡"
                        }
                    ],
                    "value": "0716",
                    "label": "引渡"
                }
            ]
        }
    },
    "04": {
        "status": 0,
        "msg": "OK",
        "data": {
            "options": [
                {
                    "value": "0401",
                    "label": "行政一审"
                },
                {
                    "value": "0402",
                    "label": "行政二审"
                },
                {
                    "children": [
                        {
                            "value": "0404",
                            "label": "行政依职权再审审查"
                        },
                        {
                            "value": "0405",
                            "label": "行政申诉再审审查"
                        },
                        {
                            "value": "0406",
                            "label": "行政抗诉再审审查"
                        },
                        {
                            "value": "0407",
                            "label": "行政再审"
                        }
                    ],
                    "value": "0403",
                    "label": "行政审判监督"
                },
                {
                    "children": [
                        {
                            "value": "0409",
                            "label": "非诉行政行为申请执行审查"
                        },
                        {
                            "value": "0410",
                            "label": "非诉行政行为申请执行审查复议"
                        }
                    ],
                    "value": "0408",
                    "label": "行政非诉审查"
                },
                {
                    "value": "0411",
                    "label": "其他"
                }
            ]
        }
    },
    "05": {
        "status": 0,
        "msg": "OK",
        "data": {
            "options": [
                {
                    "children": [
                        {
                            "value": "0502",
                            "label": "行政赔偿一审"
                        },
                        {
                            "value": "0503",
                            "label": "行政赔偿二审"
                        },
                        {
                            "value": "0504",
                            "label": "行政赔偿依职权再审审查"
                        },
                        {
                            "value": "0505",
                            "label": "行政赔偿申请再审审查"
                        },
                        {
                            "value": "0506",
                            "label": "行政赔偿抗诉再审审查"
                        },
                        {
                            "value": "0507",
                            "label": "行政赔偿再审"
                        },
                        {
                            "value": "0508",
                            "label": "其他行政赔偿"
                        }
                    ],
                    "value": "0501",
                    "label": "行政赔偿"
                },
                {
                    "children": [
                        {
                            "value": "0510",
                            "label": "法院作为赔偿义务机关自赔"
                        },
                        {
                            "value": "0511",
                            "label": "赔偿委员会审理赔偿"
                        },
                        {
                            "value": "0512",
                            "label": "司法赔偿监督审查"
                        },
                        {
                            "value": "0513",
                            "label": "赔偿确认申诉审查"
                        },
                        {
                            "value": "0514",
                            "label": "司法赔偿监督上级法院赔偿委员会重审"
                        },
                        {
                            "value": "0515",
                            "label": "司法赔偿监督本院赔偿委员会重审"
                        }
                    ],
                    "value": "0509",
                    "label": "司法赔偿"
                },
                {
                    "value": "0516",
                    "label": "其他赔偿"
                },
                {
                    "children": [
                        {
                            "value": "0518",
                            "label": "刑事司法救助"
                        },
                        {
                            "value": "0519",
                            "label": "民事司法救助"
                        },
                        {
                            "value": "0520",
                            "label": "行政司法救助"
                        },
                        {
                            "value": "0521",
                            "label": "国家赔偿司法救助"
                        },
                        {
                            "value": "0522",
                            "label": "执行司法救助"
                        },
                        {
                            "value": "0523",
                            "label": "涉诉信访司法救助"
                        }
                    ],
                    "value": "0517",
                    "label": "司法救助"
                },
                {
                    "value": "0524",
                    "label": "其他司法救助"
                }
            ]
        }
    },
    "08": {
        "status": 0,
        "msg": "OK",
        "data": {
            "options": [
                {
                    "children": [
                        {
                            "value": "0802",
                            "label": "司法拘留"
                        },
                        {
                            "value": "0803",
                            "label": "司法罚款"
                        }
                    ],
                    "value": "0801",
                    "label": "司法制裁审查"
                },
                {
                    "value": "0804",
                    "label": "司法制裁复议"
                }
            ]
        }
    },
    "09": {
        "status": 0,
        "msg": "OK",
        "data": {
            "options": [
                {
                    "value": "0901",
                    "label": "非诉财产保全审查"
                },
                {
                    "value": "0902",
                    "label": "非诉行为保全审查"
                },
                {
                    "value": "0903",
                    "label": "非诉行为保全复议"
                },
                {
                    "value": "0904",
                    "label": "非诉证据保全审查"
                }
            ]
        }
    },
    "99": {
        "status": 0,
        "msg": "OK",
        "data": {
            "options": [
                {
                    "value": "9999",
                    "label": "其他"
                }
            ]
        }
    },
    "10": {
        "status": 0,
        "msg": "OK",
        "data": {
            "options": [
                {
                    "children": [
                        {
                            "value": "1002",
                            "label": "首次执行"
                        },
                        {
                            "value": "1003",
                            "label": "恢复执行"
                        },
                        {
                            "value": "1004",
                            "label": "财产保全执行"
                        }
                    ],
                    "value": "1001",
                    "label": "执行实施"
                },
                {
                    "children": [
                        {
                            "value": "1006",
                            "label": "执行异议"
                        },
                        {
                            "value": "1007",
                            "label": "执行复议"
                        },
                        {
                            "value": "1008",
                            "label": "执行监督"
                        },
                        {
                            "value": "1009",
                            "label": "执行协调"
                        }
                    ],
                    "value": "1005",
                    "label": "执行审查"
                },
                {
                    "value": "1010",
                    "label": "其他执行"
                }
            ]
        }
    }
}

keylist=["01","02","03","04","05","06","07","08","09","10","99"]
options=[]
for key in keylist:
	item={
		"label":"",
		"options":obj[key]["data"]["options"]
	}
	options.append(item)
print(options)
# output={}

# def dfs(options,input):
#     for option in input["#"]:
#         obj={
#             "label":option["text"],
#             "value":option["id"]
#         }
#         if option["id"] in input:
#             obj["children"]=dfs_help(input,input[option["id"]])
#         options.append(obj)

# def dfs_help(obj,list_obj):
#     res=[]
#     for item in list_obj:
#         obj={
#             "label":item["text"],
#             "value":item["id"],
#         }
#         if item["id"] in obj:
#             obj["children"]=dfs_help(obj[item["id"]])
#         res.append(obj)
#     return res

# for key in keylist:
#     print("------"+key+"---------")
#     children=spcx[key]
#     # 第一遍将元素按parent进行分组
#     item_obj={}
#     for child in children:
#         if child["parent"] not in item_obj:
#             item_obj[child["parent"]]=[]
#         item_obj[child["parent"]].append(child)
#     # dfs构建组件
#     options=[]
#     dfs(options,item_obj)
#     obj={
#             "status":0,
#             "msg":"OK",
#             "data":{
#                 "options":options
#             }
#     }
#     output[key]=obj

with open("output.json", "w") as file:
    json.dump(options, file,ensure_ascii=False)