import json

def common_format_type1 (list_obj) :
    output=[]
    if (len(list_obj) == 0) :
        return output
    for item in list_obj:
        output.append({
            'label':item['key']+'('+str(item['doc_count'])+')',
            'value':item['key'],
            'name':item['key']
        })
    return output



def dfs_old(component_list,items_dict):
    list_new=[]
    for item in component_list:
        if item['value'] in items_dict:
            item_new=item
            item_new['label']=item_new['name']+'('+str(items_dict[item_new['value']])+')'
            if 'children' in item_new and len(item_new['children'])!=0:
                item_new['children']=dfs(item['children'],items_dict)
            list_new.append(item_new)
    return list_new

def dfs(component_list, items_dict):
    list_new = []
    for item in component_list:
        if item['value'] in items_dict:
            item_new = item
            item_new['label'] = f"{item_new['name']}({str(items_dict[item_new['value']])})"
            # 如果有子节点，递归调用 dfs 填充
            if 'children' in item_new and len(item_new['children']) != 0:
                item_new['children'] = dfs(item['children'], items_dict)
            list_new.append(item_new)
    return list_new

def handle_detail (data) :
    newData = {
        'basic': {
            '_id': data['_id'],
            'title': data['_source']['title'],
            'publication_date': data['_source']['publication_date'],
            'effective_date': data['_source']['effective_date'],
            'e': data['_source']['enacting_body'],
        },
        'catalog': { }
    }
    # 确保 '_source' 字段存在
    if '_source' not in data:
        return newData

    # 检查 'content' 字段是否存在
    if 'content' in data['_source']:
        newData['catalog']['content'] = data['_source']['content']  # 直接添加 content

    return newData

def test (s) :
    s = '<p>' + s
    t = s.replace("\n", "</p><p>");
    t += '</p>'
    return t


def test1(item):
    for i in item:
        if len(i['fgid']) !=0:
            return true
    return false

def extract_aggregation_data(result, aggregation_name):
    # 获取大项聚合
    aggregations = result.get('aggregations', {})

    # 提取指定大项的聚合数据
    aggregation_data = aggregations.get(aggregation_name, {})

    extracted_data = []

    # 遍历子聚合
    for sub_aggregation_name, sub_aggregation_data in aggregation_data.items():
        # 检查子聚合数据是否为字典类型且包含 'buckets'
        if isinstance(sub_aggregation_data, dict):
            buckets = sub_aggregation_data.get('buckets', [])
            if buckets:  # 如果有 buckets 数据
                for bucket in buckets:
                    extracted_data.append({bucket.get('key'): bucket.get('doc_count')})

    return extracted_data

def recursive_fill(nodes, data):
    """
    递归填充树节点，根据聚合数据填充相应的 label 字段。

    参数:
    - nodes: 树的当前节点列表，可能包含子节点。
    - data: 聚合数据，包含 label 和 count 的字典。

    返回:
    - 更新后的树结构
    """
    for node in nodes:
        # 如果当前节点有子节点，则递归调用处理子节点
        if 'children' in node and node['children']:
            recursive_fill(node['children'], data)  # 递归填充子节点
        else:
            # 在叶子节点填充数据
            for item in data:
                for label, count in item.items():
                    # 如果节点的名字匹配，则更新 label
                    if node['name'] == label:
                        node['label'] = f"{label}({count})"  # 仅更新 label，不更新 value
                        break
    return nodes