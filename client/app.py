from redis_shard.shard import RedisShardAPI

servers = [
    {'name': 'redis1', 'host': 'redis1', 'port': 6379},
    {'name': 'redis2', 'host': 'redis2', 'port': 6379},
    {'name': 'redis3', 'host': 'redis3', 'port': 6379},
    {'name': 'redis4', 'host': 'redis4', 'port': 6379},
]

r = RedisShardAPI(servers, hash_method='md5', strict_redis=True)

print(r.get_server_name('bar'))
print(r.get_server_name('c{bar}'))
print(r.get_server_name('c{bar}d'))
print(r.get_server_name('c{bar}e'))
print(r.get_server_name('e{bar}f'))

# hash_tag feature uses string between {} as hash key
# these keys will land on the same node
r.set('foo', 'bar')
r.set('{foo}d', 'bar')
r.set('love{foo}l', 'bar')
r.set('{foo}', 'bar')

# set is good
r.set('bar', 'stool')
r.set('{bar}d', 'stool')
r.set('love{bar}l', 'stool')
r.set('re{bar}', 'stool')

# setex is good
r.setex('s{ock}', time=3600, value=1)
r.setex('ock', time=3600, value=2)
r.setex('sm{ock}', time=3600, value=3)
r.setex('d{ock}ing', time=3600, value=3)

# get is good
print(r.get('s{ock}'))
print(r.get('sm{ock}'))

# # scan is not supported by redis-shard
for key in r.scan_iter(match='ock'):
    print(key)