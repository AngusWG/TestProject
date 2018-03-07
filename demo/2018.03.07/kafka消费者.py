# kafka的使用 consumer使用
import json

from kafka import KafkaConsumer

# 消费kafka中最新的数据 并且自动提交offsets[消息的偏移量]
consumer = KafkaConsumer('robot',
                         group_id='ts',
                         bootstrap_servers=['192.168.14.240:9092'])
for message in consumer:
    # 注意: message ,value都是原始的字节数据，需要decode
    # 例如: message.value.decode('utf-8')

    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))

# 下面代码展示了kafkaConsumer常用的几个参数
# 1:消费kafka中保存最早的数据，kafka默认保存几天的历史数据，不管这些数据是否消费，如果想读取最早打数据就需要设置如下参数,第二个参数是不自动提交消费数据的offset
KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

# 2:消费json 格式的消息:
KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))

# 3:设置当kafka中没有可消费的数据超时时间
KafkaConsumer(consumer_timeout_ms=1000)  # 如果1秒内kafka中没有可供消费的数据，自动退出

# 如果kafka一个group中同时设置了n个topic,想同时从几个topic中消费数据，代码如下：
# 假设有三个topic，topic的名称分别是：topic1=awesome1 topic2=awesome2 topic3=awesome3
consumer = KafkaConsumer()
consumer.subscribe(pattern='^awesome.*')
