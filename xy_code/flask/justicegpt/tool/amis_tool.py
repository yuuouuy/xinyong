import datetime
import copy

def build_tags(params):
    component=[
            {
            "type":"tpl",
            "tpl":"<span style=\"font-weight:bold;\">已选条件："
        }
    ]
    item_template={
            "type":"tag",
            "label":'',
            "closable":True,
            "displayMode":"normal",
            "color":"rgb(234,177,58)",
            "onEvent":{
                "close":{
                    "actions":[
                        {
                            "actionType":"setValue",
                            "componentId":"outer",
                            "args":{
                              "value":{
                              }
                            }
                        },
                        {
                            "actionType":"reload",
                            "componentId":"service02"
                        },
                        {
                            "actionType":"reload",
                            "componentId":"service01"
                        },
                        {
                            "actionType":"reload",
                            "componentId":"service00"
                        }
                    ]
                }
            }
          }
    label_dict=label_build(params)
    for key in params:
        if len(params[key])==0:
            continue
        item=copy.deepcopy(item_template) 
        item['label']=label_dict[key]
        item['onEvent']['close']['actions'][0]['args']['value'][key]=''
        component.append(item)
    return component

def label_build(params):
    if len(params['publication_date'])!=0:
        publication_date_list=date_tool(params['publication_date'])
    if len(params['effective_date'])!=0:
        effective_date_list=date_tool(params['effective_date'])
    return {
        'content':params['content'],
        'enacting_body':"制定机关："+params['enacting_body'],
        'grade':"效力位阶："+params['grade'],
        'scenario':"治理场景："+params['scenario'],
        'city_management':params['city_management'],
        'safety_construction':params['safety_construction'],
        'publication_date':publication_date_list[0]+"至"+publication_date_list[1] if len(params['publication_date'])!=0 else '',
        'effective_date': effective_date_list[0] + "至" + effective_date_list[1] if len(params['effective_date']) != 0 else '',
        'local_nation':params['local_nation'],
        'province':params['province'],
        'agency_bank':params['agency_bank'],
        'competent_authority':params['competent_authority'],
    }

def date_tool(date):
    date_list=date.split(",")
    return [seconds_to_date(int(date_list[0])+43200),seconds_to_date(int(date_list[1]))]
 
def seconds_to_date(seconds):
    dt = datetime.datetime.utcfromtimestamp(0) + datetime.timedelta(milliseconds=seconds*1000)
    year = dt.year
    month = dt.month
    day = dt.day
    return f"{year}-{month}-{day}"

def detail_tool(obj):
    data={
        "basic":obj['basic']
    }
    catalog={}
    for key in obj['catalog']:
        catalog[key]=html_tool(obj['catalog'][key])
    data['catalog']=catalog
    return data

def html_tool(input_str):
    str_new=input_str.replace("</p>","\n").replace("<p>","        ")
    return str_new
