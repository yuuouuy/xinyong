import requests
import json
import time

from ..tool.query_tool import params_to_list, condition_to_json, condition_to_json_simple_v5
from ..tool.format_tool import handle_detail,extract_aggregation_data,recursive_fill
from ..tool.amis_tool import build_tags, detail_tool
from ..config.config import es_url, ai_url, es_index
from ..mock.ai_mock import extract_answer, qa_answer
from ..model import redis_cache
from ..tool.static.aggregations_tree import tree

def index_api(params):
    # 0 先看redis中是否有缓存数据
    key_str = redis_cache.build_key(params)
    redis_res = redis_cache.output_dict(key_str)
    if redis_res != None:
        print('命中缓存:' + key_str)
        return {
            'status': 0,
            'msg': '',
            'data': {
                'aggregations': redis_res
            }
        }
    print('缓存未命中:' + key_str)
    start_second = time.time()
    # 1 格式化查询条件
    advancedJson = {
        'id': 'xyQuery_v2.0',
        'params': {

        }
    }
    print(params)
    # condition = params_to_list(params)
    advancedJson['params'] = condition_to_json_simple_v5(params) if len(params) > 0 else {}
    # 2 向es服务器发情求
    body = str(advancedJson).replace('\'', '\'').replace('True', 'true')
    url = es_url + '/' + es_index + '/_search/template'
    headers = {
        'Content-Type': 'application/json',
        'Connection': 'close'
    }
    body = json.dumps(advancedJson, ensure_ascii=False)
    response = requests.post(url, data=body.encode('utf-8'), headers=headers)
    # 3 对返回结果进行解析
    result = response.json()
    response.close()
    aggregations = {}
    # 4 提取并填充 governance_scenario 和 efficacy_hierarchy 数据
    dimensions = ['governance_scenario', 'efficacy_hierarchy']
    for dimension in dimensions:
        items_dict = extract_aggregation_data(result, dimension)
        aggregations[dimension]= recursive_fill(tree['data']['aggregations'][dimension],items_dict)
    newResult = {
        'status': 0,
        'msg': '',
        'data': {
            'aggregations': aggregations
        }
    }
    # 4 更新redis，并返回
    end_second = time.time()
    if end_second - start_second >= 1:
        print('es响应时间超过1s，更新缓存')
        redis_cache.input_dict(aggregations, key_str)
    else:
        print('es响应时间在1s内，不进行缓存')
    return newResult


def page_api(params):
    # 1 构建es查询
    advancedJson = {
        'id': 'xyQuery_v2.0',
        'params': {
        }
    }
    print(params)
    # sort和from字段用于结果排序和分页，要单独处理
    sort = params['sort']
    page_from = params['from']
    del params['sort']
    del params['from']

    # condition = params_to_list(params)
    # print(condition)
    advancedJson['params'] = condition_to_json_simple_v5(params) if len(params) > 0 else {}
    print(advancedJson['params'])
    advancedJson['params']['from'] = page_from

    if sort == '01':
        advancedJson['params']['sort_order'] = 'desc'
        advancedJson['params']['publication_date_sort'] = {
            's31_sort_order': 'desc'
        }
    else:
        advancedJson['params']['sort_order'] = 'desc'
        advancedJson['params']['publication_date_sort'] = None
    # 2 向es服务器发情求
    url = es_url + '/' + es_index + '/_search/template'
    headers = {
        'Content-Type': 'application/json',
        'Connection': 'close'
    }
    body = json.dumps(advancedJson, ensure_ascii=False)
    response = requests.post(url, data=body.encode('utf-8'), headers=headers)
    # 3 对返回结果进行解析
    result = response.json()
    print(result)
    response.close()
    try:
        newResult = {
            'status': 0,
            'msg': '',
            'data': {
                'hits': {
                    'total': result['hits']['total']['value'] if 'hits' in result and 'total' in result['hits'] else 0,
                    'hits': result['hits']['hits']
                },
                'json': advancedJson
            }
        }
    except Exception as e:
        newResult = {
            'status': 1,
            'msg': '无数据',
            'data': ''
        }
        return newResult
    return newResult


def detail_api(params):
    # 1 查询es数据库
    url = es_url + '/' + es_index + '/_doc/' + params['id']
    response = requests.get(url)
    result = response.json()
    response.close()
    # 2 对返回结果进行解析
    newResult = detail_tool(handle_detail(result))
    res = {
        "status": 0,
        "msg": "",
        "data": newResult
    }
    return res


def tags_api(params):
    res = {
        "status": 0,
        "msg": "",
        "data": build_tags(params)
    }
    return res