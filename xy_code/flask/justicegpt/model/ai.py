from ..config.config import ai_url
from ..mock.ai_mock import extract_answer
import json,requests,time,datetime

condition_number={
    'court_level':{
        '全部':'0',
        '最高人民法院':'1',
        '高级人民法院':'2',
        '中级人民法院':'3',
        '基层人民法院':'4'
    },
    'anyou':{
        '刑事案由':'1',
        '民事案由':'9000',
        '执行案由(2011版)':'3200',
        '国家赔偿案由(2011版)':'2100',
        '行政案由':'xzay'
    },
    'case_type':{
        '管辖案件':'01',
        '刑事案件':'02',
        '民事案件':'03',
        '行政案件':'04',
        '国家赔偿与司法救助案件':'05',
        '区际司法协助案件':'06',
        '国际司法协助案件':'07',
        '司法制裁案件':'08',
        '非诉保全审查案件':'09',
        '执行案件':'10',
        '强制清算与破产案件':'11',
        '其他':'99'
    },
    'article_type':{
        '判决书': '01',
        '裁定书':'02',
        '调解书': '03',
        '决定书': '04',
        '通知书': '05',
        '令': '09',
        '其他': '10'
    },
    'public_type':{
        '文书公开':'01',
        '信息公开':'02'
    }
}

def timestamp_tool(year,month,day):
    date_obj = datetime.datetime(year, month, day)
    timestamp = int(date_obj.timestamp())
    return str(timestamp)

def aiSearch_api(params):
    # 返回的数据
    output={
        'status':0,
        'msg':'',
        'data':{}
    }
    try:
        # 1 向ai服务发请求
        url=ai_url+'/extract_4_0'
        headers= {
            "Content-Type": "application/json",
            'Connection': 'close'
        }
        body = json.dumps(params)
        response = requests.post(url, data=body, headers=headers)
        response.close()
        # 2 对返回数据进行解析
        text=eval(response.text[8:-3])
        # time.sleep(5)
        # text=extract_answer # mock数据
        string='解析结果： | '
        for key in text:
            if len(text[key])!=0 and key!='裁判年份':
                string=string+text[key]+' | '
        if '裁判年份' in text and len(text['裁判年份']) !=0:
            years=text['裁判年份'].split(',')
            string=string+years[0]+'-'+years[-1]+' | '
            text['裁判年份']=timestamp_tool(int(years[0]),1,1)+','+timestamp_tool(int(years[-1]),12,31)
        # 3 返回结果
        output['data']={
            "wait": False,
            "string":string,
            "anyou": condition_number['anyou'][text['案由']] if ('案由' in text and text['案由'] in condition_number['anyou']) else "",
            "case_name": text['案件名称'] if '案件名称' in text else '',
            "court_name": text['法院名称'] if '法院名称' in text else '',
            "case_no": text['案件号'] if '案件号' in text else '',
            "court_level": condition_number['court_level'][text['法院层级']] if ('法院层级' in text and text['法院层级'] in condition_number['court_level']) else "",
            "type": condition_number['case_type'][text['案件类型']] if ('案件类型' in text and text['案件类型'] in condition_number['case_type']) else "",
            "article_type": condition_number['article_type'][text['文书类型']] if ('文书类型' in text and text['文书类型'] in condition_number['article_type']) else "",
            "judge": text['法官名称'] if '法官名称' in text else '',
            "public_type": condition_number['public_type'][text['公开类型']] if ('公开类型' in text and text['公开类型'] in condition_number['public_type']) else "",
            "law_office": text['律所'] if '律所' in text else '',
            "person": text['当事人'] if '当事人' in text else '',
            "lawer": text['律师']if '律师' in text else '',
            "date": text['裁判年份'] if '裁判年份' in text else '',
        }
    except Exception as e:
        print(e)
        output['data']['wait']=False
        output['data']['string']='解析结果：网络或解析错误，请重试！'
        return output
    return output

def aiAsk_api(params):
     # 返回的数据
    output={
        'status':0,
        'msg':'',
        'data':{}
    }
    try:
        # 1 向ai服务发请求
        url=ai_url+'/qa_4_0'
        headers= {
            "Content-Type": "application/json"
        }
        body = json.dumps(params)
        response = requests.post(url, data=body, headers=headers)
        # 2 对返回结果进行解析
        output['data']['answer']=response.json()['answer']
        response.close()
        # output['data']['answer']=qa_answer['Answer'] # mock数据
        output['data']['wait']=False
        # time.sleep(5)
    except Exception as e:
        print(e)
        output['data']['answer']='网络或者解析错误，请重试！'
        output['data']['wait']=False
        return output
    return output