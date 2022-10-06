# redis_queue

# Redis RDB, Redis AOF and Beanstalkd queue perfomance test

# Run containers
`docker-compose up`

# URLs (Put 2 messages to queue and get 1 message)
redis_rdb_urls.txt  
redis_aof_urls.txt  
beanstalkd_urls.txt  

# Siege commands
```
siege -c 10 --time=60S -f URL_FILE
siege -c 25 --time=60S -f URL_FILE
siege -c 50 --time=60S -f URL_FILE
siege -c 100 --time=60S -f URL_FILE
```

# Results
## Response time, secs
concurrent | Redis RDB | Redis AOF | Beanstalkd |  
--- | --- | --- | --- |  
10 | 0.05 | 0.04 | 0.06 |  
25 | 0.11 | 0.12 | 0.14 |  
50 | 0.22 | 0.23 | 0.28 |  
100 | 0.44 | 0.44 | 0.55 | 
250 | 1.13 | 1.12 | 1.41 |
 
## Transaction rate, trans/sec
concurrent | Redis RDB | Redis AOF | Beanstalkd |  
--- | --- | --- | --- |  
10 | 205.47 | 227.23 | 172.57 |  
25 | 218.16 | 202.72 | 172.91 |  
50 | 224.69 | 220.99 | 180.32 |  
100 | 227.27 | 226.96 | 180.54 |
250 | 218.61 | 221.05 | 175.09 |
 
## Longest transaction
concurrent | Redis RDB | Redis AOF | Beanstalkd |  
--- | --- | --- | --- |  
10 | 0.15 | 0.11 | 0.12 |  
25 | 0.32 | 0.24 | 0.30 |  
50 | 0.45 | 0.37 | 0.44 |  
100 | 0.57 | 0.62 | 0.80 |
250 | 1.75 | 1.57 | 2.03 |
