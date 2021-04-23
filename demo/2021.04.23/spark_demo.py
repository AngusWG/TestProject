#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2020/11/29 12:52
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : spark_demo.py
from pyspark import SparkContext

sc = SparkContext("spark://127.0.0.1:8080", "count app")
words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"
     ])
counts = words.count()
print("Number of elements in RDD -> %i" % counts)
