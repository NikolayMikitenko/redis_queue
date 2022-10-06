from fastapi import FastAPI
import redis
import random
import json
from fastapi.responses import JSONResponse
import beanstalkc


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

############################ RDB #################################
@app.get("/get_queue_redis_rdb")
async def get_queue_redis_rdb():
    r = redis.Redis(host='redis_rdb', port=6379)
    v = r.lpop('queue')
    print(v)
    
@app.post("/set_queue_redis_rdb")
async def set_queue_redis_rdb():
    r = redis.Redis(host='redis_rdb', port=6379)
    r.rpush('queue', get_customer_order())

############################ AOF #################################
@app.get("/get_queue_redis_aof")
async def get_queue_redis_aof():
    r = redis.Redis(host='redis_aof', port=6379)
    v = r.lpop('queue')
    print(v)
    
@app.post("/set_queue_redis_aof")
async def set_queue_redis_aof():
    r = redis.Redis(host='redis_aof', port=6379)
    r.rpush('queue', get_customer_order())

############################ RDB #################################
@app.get("/get_queue_beanstalkd")
async def get_queue_beanstalkd():
    b = beanstalkc.Connection(host='beanstalkd', port=11300)
    #b.use('queue')
    job = b.reserve()
    print(job.body)
    job.delete()

@app.post("/set_queue_beanstalkd")
async def set_queue_beanstalkd():
    b = beanstalkc.Connection(host='beanstalkd', port=11300)
    #b.use('queue')
    b.put(get_customer_order())

def get_customer_order():
    return json.dumps({'cutomer':random.randint(0, 100), 'product':random.randint(0, 1000), 'quantity': random.randint(0, 10)})
    