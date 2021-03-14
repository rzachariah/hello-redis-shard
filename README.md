# hello-redis-shard
Taking redis-shard for a spin

## Demo
Try the redis-shard demo

```
docker-compose up --build
```

This will start 4 local redis instances, and a python redis client. The client will set values and these will be sharded across redis instances.

redis-shard also supports a hash_tag feature, which enables us to send keys with a common substring to the same node.

```
client_1  | redis1
client_1  | redis1
client_1  | redis1
client_1  | redis1
client_1  | redis1
```

However, redis-shard does not support the scan operation.

```
client_1  | Traceback (most recent call last):
client_1  |   File "/usr/src/app/./app.py", line 42, in <module>
client_1  |     for key in r.scan_iter(match='ock'):
client_1  |   File "/usr/local/lib/python3.9/site-packages/redis_shard/shard.py", line 115, in __getattr__
client_1  |     raise NotImplementedError("method '%s' cannot be sharded" % method)
client_1  | NotImplementedError: method 'scan_iter' cannot be sharded
```