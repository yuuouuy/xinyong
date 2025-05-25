import redis
import json

from ..config.config import redis_host,redis_port,redis_expire_time

# 根据前端查询参数生成redis库的key
def build_key(params):
   key_str=''
   for key in params:
      key_str+=params[key]+'|'
   return key_str

# 将数据插入到redis
def input_dict(the_dict,the_key):
   cli=redis.StrictRedis(host=redis_host, port=redis_port, db=0)
   # 序列化字典并插入到 Redis
   serialized_dict = json.dumps(the_dict)
   cli.set(the_key, serialized_dict)
   if redis_expire_time!=0:
      cli.expire(the_key,redis_expire_time) # 设置过期时间，单位是秒

# 从redis中查询数据
def output_dict(the_key):
   cli=redis.StrictRedis(host=redis_host, port=redis_port, db=0)
   # 从 Redis 中获取并反序列化字典
   search_ans=cli.get(the_key)
   if search_ans == None:
      return None
   else:
      retrieved_dict = json.loads(search_ans)
      return retrieved_dict