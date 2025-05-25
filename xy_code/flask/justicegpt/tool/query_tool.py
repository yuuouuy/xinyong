import datetime
import json

# condition_mapping_cname={
#     "keywords":"关键字",
#     "fulltext":"全文检索",
#     "anyou":"案由",
#     "case_name":"案件名称",
#     "court_name":"法院名称",
#     "case_no":"案件号",
#     "court_level":"法院层级",
#     "type":"案件类型",
#     "article_type":"文书类型",
#     "procedure":"审判程序",
#     "judge":"法官名称",
#     "public_type":"公开类型",
#     "law_office":"律所",
#     "person":"当事人",
#     "law_article":"法律依据",
#     "lawer":"律师",
#     "date":"裁判日期",
#     "year":"裁判日期"
# }
condition_mapping_cname={
    "content":"全文检索",
    "effective_date":"施行日期",
    "publication_date":"公布日期",
    "grade":"效力位阶",
    "scenario":"治理场景",
    "enacting_body":"制定机关",
}
condition_mapping_ename={
    "content":"content",
    "effective_date":"effective_date",
    "publication_date":"publication_date",
    "grade":"efficacy_hierarchy.grade",
    "scenario":"governance_scenario.scenario",
    "enacting_body":"enacting_body"
}


def params_to_list(params):
    condition_list = []
    if "$$id" in params:
        del params["$$id"]
    for key in params:
        if len(params[key]) != 0:
            condition_list.append({
                "ename": condition_mapping_ename[key],
                "cname": condition_mapping_cname[key],
                "value": params[key]
            })
    return condition_list



def law_article_tool(law_article):
    if(',' in law_article):
        return law_article.split(",")
    elif('，' in law_article):
        return law_article.split("，")
    else:
        return [law_article,""]

def date_tool(date):
    date_list=date.split(",")
    date_list[0]=int(date_list[0])
    date_list[1]=int(date_list[1])
    date0= datetime.datetime.fromtimestamp(date_list[0])
    date1= datetime.datetime.fromtimestamp(date_list[1])
    ans=[date0.strftime('%Y-%m-%d'),date1.strftime('%Y-%m-%d')]
    return ans

def condition_to_json(condition):
    obj = {}
    obj_litigant = {}
    arrayA = []
    arrayB = []

    advanced_A={
        "quanwen": {"quanwen":{"quanwen":""}},
        "s1": {"s1":{"s1":""}},
        "s7": {"s7":{"s7":""}},
        "court_name": {"court_name":{"court_name":""}},
        "s31": {"s31":{"start":"","end":""}},
        "officers_name": {"officers_name":{"officers_name":""}},
        "s17": {"s17":{"s17":""}},
        "legal_basis": {"legal_basis":{}}
    }
    advanced_B={
        "cause_id": {"cause_id": {"cause_id": ""}}, 
        "court_id": {"court_id": {"court_id": ""}},
        "court_level": {"court_level": {"court_level": ""}},
        "s8": {"s8": {"s8": ""}},
        "spcx": [{"lvl1_spcx": {"lvl1_spcx": ""}}, {"lvl2_spcx": {"lvl2_spcx": ""}}],
        "s6": {"s6": {"s6": ""}},
        "s43": {"s43": {"s43": ""}},
        "keywords": {"keywords": {"keywords": ""}}
    }
    advanced_C=[
        "litigant.name",
        "litigant.attorney.attorney_name",
        "litigant.attorney.attorney_firm"
    ]
    id_to_cn={
        "court_level": {
            "1":"最高人民法院",
            "2":"高级人民法院",
            "3":"中级人民法院",
            "4":"基层人民法院"
        },
        "cycle": {
            "*-60.0": "2个月内",
            "60.0-120.0": "3-4个月",
            "120.0-180.0": "5-6个月",
            "180.0-240.0": "7-8个月",
            "240.0-300.0": "9-10个月",
            "300.0-*": "10个月以上"
        },
        "litigant": {
            "1": "自然人",
            "2": "企事业法人",
            "3": "教研机构",
            "4": "其他"
        },
        "cause_count": {
            "9300": "知识产权合同纠纷",
            "9363": "知识产权权属、侵权纠纷",
            "9433": "不正当竞争纠纷",
            "9449": "垄断纠纷",
            "9299": "总和"
        },
        "type_count": {
            "9301": "著作权",
            "9364": "著作权",
            "9315": "商标权",
            "9393": "商标权",
            "9319": "专利权",
            "9396": "专利权   ",
            "9433": "不正当竞争纠纷",
            "9449": "垄断纠纷",
            "9299": "总和"
        },
        "s6": {
            "10": "其他",
            "00": "全部",
            "01": "判决书",
            "02": "裁定书",
            "03": "调解书",
            "04": "决定书",
            "05": "通知书",
            "09": "令"
        },
        "s8": {
            "01": "管辖案件",
            "02": "刑事案件",
            "03": "民事案件",
            "04": "行政案件",
            "05": "国家赔偿与司法救助案件",
            "06": "区际司法协助案件",
            "07": "国际司法协助案件",
            "08": "司法制裁案件",
            "09": "非诉保全审查案件",
            "10": "执行案件",
            "11": "强制清算与破产案件",
            "99": "其他"
        },
        "lvl1_spcx": {
            "1001":"执行实施","1005":"执行审查","1010":"其他执行","1101":"强制清算与破产清算申请审查","1104":"强制清算与破产上诉","1107":"强制清算与破产监督","1110":"强制清算","1111":"破产","9999":"其他","0101":"刑事管辖","0104":"民事管辖","0111":"行政管辖","0115":"行政赔偿管辖","0201":"刑事一审","0202":"刑事二审","0203":"刑事审判监督","0208":"申请没收违法所得","0209":"刑事复核","0213":"强制医疗","0218":"停止执行死刑","0223":"刑罚与执行变更","0227":"其他","0228":"安置教育","0301":"民事一审","0302":"民事二审","0303":"民事审判监督","0308":"第三人撤销之诉","0309":"特别程序","0324":"催告","0327":"督促","0330":"其他","0331":"人身安全保护令","0401":"行政一审","0402":"行政二审","0403":"行政审判监督","0408":"行政非诉审查","0411":"其他","0501":"行政赔偿","0509":"司法赔偿","0516":"其他赔偿","0517":"司法救助","0524":"其他司法救助","0601":"认可与执行申请审查","0610":"送达文书","0620":"调查取证","0630":"被判刑人移管","0633":"罪脏移交","0701":"承认与执行申请审查","0705":"送达文书","0709":"调查取证","0713":"被判刑人移管","0716":"引渡","0801":"司法制裁审查","0804":"司法制裁复议","0901":"非诉财产保全审查","0902":"非诉行为保全审查","0903":"非诉行为保全复议","0904":"非诉证据保全审查"
        },
        "lvl2_spcx": {
            "1002":"首次执行","1003":"恢复执行","1004":"财产保全执行","1006":"执行异议","1007":"执行复议","1008":"执行监督","1009":"执行协调","1102":"强制清算申请审查","1103":"破产申请审查","1105":"强制清算上诉","1106":"破产上诉","1108":"强制清算监督","1109":"破产监督","1112":"破产清算","1113":"破产重整","1114":"破产和解","0102":"刑事提级管辖","0103":"刑事指定管辖","0105":"民事提级管辖","0106":"民事指定管辖","0107":"民事移交管辖审批","0108":"民事管辖协商","0109":"民事管辖上诉","0110":"民事管辖监督","0112":"行政提级管辖","0113":"行政指定管辖","0114":"行政管辖上诉","0116":"行政赔偿提级管辖","0117":"行政赔偿指定管辖","0118":"行政赔偿管辖协商","0119":"行政赔偿管辖上诉","0204":"刑事依职权再审审查","0205":"刑事申诉再审审查","0206":"刑事抗诉再审审查","0207":"刑事再审","0210":"死刑复核","0211":"法定刑以下判处刑罚复核","0212":"特殊假释复核","0214":"申请强制医疗审查","0215":"解除强制医疗审查","0216":"强制医疗复议","0217":"强制医疗监督","0219":"停止执行死刑请求审查","0220":"依职权停止执行死刑","0221":"停止执行死刑调查","0222":"停止执行死刑调查审查","0224":"刑罚与执行变更审查","0225":"刑罚与执行变更监督","0226":"刑罚与执行变更备案","0229":"申请安置教育审查","0230":"解除安置教育审查","0231":"安置教育复议","0232":"安置教育监督","0304":"民事依职权再审审查","0305":"民事申诉再审审查","0306":"民事抗诉再审审查","0307":"民事再审","0310":"选民资格","0311":"宣告失踪、宣告死亡","0312":"财产代管人申请变更代管","0313":"行为能力认定","0314":"监护人指定异议","0315":"监护关系变更","0316":"认定财产无主","0317":"实现担保物权","0318":"调解协议司法确认","0319":"设立海事赔偿责任限制基金","0320":"海事债权登记与受偿","0321":"撤销仲裁裁决","0322":"申请确认仲裁协议效力","0323":"民事特别程序监督","0325":"船舶优先权催告","0326":"公示催告","0328":"申请支付令审查","0329":"支付令监督","0332":"人身安全保护令申请审查","0333":"人身安全保护令变更","0404":"行政依职权再审审查","0405":"行政申诉再审审查","0406":"行政抗诉再审审查","0407":"行政再审","0409":"非诉行政行为申请执行审查","0410":"非诉行政行为申请执行审查复议","0502":"行政赔偿一审","0503":"行政赔偿二审","0504":"行政赔偿依职权再审审查","0505":"行政赔偿申请再审审查","0506":"行政赔偿抗诉再审审查","0507":"行政赔偿再审","0508":"其他行政赔偿","0510":"法院作为赔偿义务机关自赔","0511":"赔偿委员会审理赔偿","0512":"司法赔偿监督审查","0513":"赔偿确认申诉审查","0514":"司法赔偿监督上级法院赔偿委员会重审","0515":"司法赔偿监督本院赔偿委员会重审","0518":"刑事司法救助","0519":"民事司法救助","0520":"行政司法救助","0521":"国家赔偿司法救助","0522":"执行司法救助","0523":"涉诉信访司法救助","0602":"认可与执行台湾地区法院裁判审查","0603":"认可与执行台湾地区仲裁裁决审查","0604":"认可与执行香港特别行政区法院裁判审查","0605":"认可与执行香港特别行政区仲裁裁决审查","0606":"认可与执行澳门特别行政区法院裁判审查","0607":"认可与执行澳门特别行政区仲裁裁决审查","0608":"认可与执行审查复议","0609":"其他认可与执行审查","0611":"请求台湾地区送达文书审查","0612":"请求香港特别行政区法院送达文书审查","0613":"请求澳门特别行政区法院送达文书审查","0614":"台湾地区请求送达文书审查","0615":"协助台湾地区送达文书","0616":"香港特别行政区法院请求送达文书审查","0617":"协助香港特别行政区法院送达文书","0618":"澳门特别行政区法院请求送达文书审查","0619":"协助澳门特别行政区法院送达文书","0621":"请求台湾地区调查取证审查","0622":"请求香港特别行政区调查取证审查","0623":"请求澳门特别行政区法院调查取证审查","0624":"台湾地区请求调查取证审查","0625":"协助台湾地区调查取证","0626":"香港特别行政区请求调查取证审查","0627":"协助香港特别行政区调查取证","0628":"澳门特别行政区法院请求调查取证审查","0629":"协助澳门特别行政区法院调查取证","0631":"接收在台湾地区被判刑人","0632":"向台湾地区移管被判刑人","0634":"接收台湾地区移交罪赃","0635":"向台湾地区移交罪赃","0702":"承认与执行外国法院裁判审查","0703":"承认与执行国外仲裁裁决审查","0704":"其他承认与执行审查","0706":"外国法院请求送达文书审查","0707":"送达外国法院文书","07048":"请求外国法院送达文书审查","0710":"外国法院请求调查取证审查","0711":"外国法院请求调查取证实施","0712":"请求外国法院调查取证审查","0714":"接收在外国被判刑人","0715":"向外国移管被判刑人","0717":"请求外国引渡","0718":"协助外国引渡","0802":"司法拘留","0803":"司法罚款"
        }
    }

    for item in condition:
        if ((item['ename'] == 'litigant.name') or (item['ename'] == 'litigant.attorney.attorney_name' ) or (item['ename'] == 'litigant.attorney.attorney_firm' )):
            # 当事人
            obj_litigant[item['ename']] = item['value']
        else:
            obj[item['ename']] = item['value']

    # A类
    for item in advanced_A:
        if (item in obj and len(obj[item])!=0) :
            if (item == 's31') :
                advanced_A[item][item]['start'] = obj[item][0]
                advanced_A[item][item]['end'] = obj[item][1]
                arrayA.append(advanced_A[item])
            elif (item == 'legal_basis') :
                if(len(obj[item][0])==0 and len(obj[item][1])==0):
                    continue
                elif (len(obj[item][0])!=0 and len(obj[item][1])!=0) :
                    advanced_A[item][item]['law'] = {"law":obj[item][0]}
                    advanced_A[item][item]['article'] = {"article":obj[item][1],"legal_basis_last":True}
                    arrayA.append(advanced_A[item])
                elif (len(obj[item][0])!=0) :
                    advanced_A[item][item]['law'] = {"law":obj[item][0],"legal_basis_last":True}
                    arrayA.append(advanced_A[item])
                else :
                    advanced_A[item][item]['article'] = {"article": obj[item][1], "legal_basis_last": True}
                    arrayA.append(advanced_A[item])
            else :
                advanced_A[item][item][item] = obj[item]
                arrayA.append(advanced_A[item])
    #A类last
    if ( len(arrayA)!= 0 ) :
        last = arrayA[len(arrayA)-1]
        name = list(last.keys())[0]
        arrayA[len(arrayA)-1][name]['last'] = True

    #B类
    for item in advanced_B:
        if (item in obj and len(obj[item])!=0) :
            if (item == 's8') :
                advanced_B[item][item][item] = id_to_cn['s8'][obj[item]]
                arrayB.append(advanced_B[item])
            elif (item == 'spcx') :
                if (id_to_cn['lvl1_spcx'][obj[item]]) :
                    advanced_B[item][0]['lvl1_spcx']['lvl1_spcx'] = id_to_cn['lvl1_spcx'][obj[item]]
                    arrayB.append(advanced_B[item][0])
                else :
                    advanced_B[item][1]['lvl2_spcx']['lvl2_spcx'] = id_to_cn['lvl2_spcx'][obj[item]]
                    arrayB.append(advanced_B[item][1])
            else:
                advanced_B[item][item][item] = obj[item]
                arrayB.append(advanced_B[item])
    #B 类的 litigant 特殊处理
    litigant = {}
    for item in advanced_C:
        if (item in obj_litigant and len(obj_litigant[item])!=0) :
            if (item == 'litigant.name') :
                litigant['name'] = obj_litigant[item]
            elif (item == 'litigant.attorney.attorney_name') :
                if (not litigant['attorney']) :
                    litigant['attorney'] = {}
                litigant['attorney']['attorney_name'] = {"attorney_name": obj_litigant[item]}
            elif (item == 'litigant.attorney.attorney_firm') :
                if (not litigant['attorney']) :
                    litigant['attorney'] = {}
                litigant['attorney']['attorney_firm'] = {"attorney_firm": obj_litigant[item]}

    if (len(litigant)!=0) :
        if litigant['attorney'] :
            litigant['attorney']['litigant_last'] = True 
        else :
            litigant['litigant_last'] = True
    if (len(litigant)!=0):
        arrayB.append({ litigant: litigant })

    #B类last
    if ( len(arrayB) != 0 ) :
        last = arrayB[len(arrayB)-1]
        name = list(last.keys())[0]
        arrayB[len(arrayB)-1][name]['last'] = True
    for item in arrayA:
        for key in item:
            obj[key]=item[key]
    for item in arrayB:
        for key in item:
            obj[key]=item[key]
    return obj

def condition_to_json_simple_v3(params):
    result = {}

    # 时间参数处理
    for time_param in ["effective_date", "publication_date"]:
        # 查找时间字段的值
        value = next((item["value"] for item in params if item["ename"] == time_param), None)
        if value:
            if isinstance(value, list) and len(value) == 2:
                start, end = value
                result[time_param] = {"start": start, "end": end}
            else:
                result[time_param] = {"start": None, "end": None}
        else:
            result[time_param] = {"start": None, "end": None}

    # 普通字段处理
    for plain_param in ["content", "enacting_body", "grade","scenario"]:
        value = next((item["value"] for item in params if item["ename"] == plain_param), "")
        result[plain_param] = value

    return result


def condition_to_json_simple_v5(params):
    result = {}

    # 统一处理所有字段
    for key, value in params.items():
        # 排除不需要处理的字段，例如 'from', 'sort'
        if key not in ["from", "sort"]:
            if value:  # 只有当字段值非空时才加入 result
                result[key] = value

    return result

