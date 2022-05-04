#!/usr/bin/env python3

"""spark application"""
import argparse
from pyspark.sql import SparkSession
import re
import time

regex = ",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"

# create parser and set its arguments
parser = argparse.ArgumentParser()
parser.add_argument("--input_path", type=str, help="Input file path")
parser.add_argument("--output_path", type=str, help="Output folder path")

# parse arguments
args = parser.parse_args()
input_filepath, output_filepath = args.input_path, args.output_path

# initialize SparkSession with the proper configuration
spark = SparkSession \
    .builder \
    .appName("Job2 Spark") \
    .getOrCreate()

# read the input file and obtain an RDD with a record for each line
rdd = spark.sparkContext.textFile("file:///home/simoc/Documents/big_data/Reviews.csv").cache()

# remove csv header
removedHeaderRDD = rdd.filter(f=lambda word: not word.startswith("Id") and not word.endswith("Text"))

user2ProductsRDD = removedHeaderRDD.map(f=lambda line: (re.split(regex, line)[2], re.split(regex, line)[1] + '\t' + re.split(regex, line)[6]))

user2ProductsReducedRDD = user2ProductsRDD.reduceByKey(func=lambda a, b: a + "\t\t" + b)

user2ProductsListRDD = user2ProductsReducedRDD.map(f=lambda item: (item[0], item[1].split("\t\t")))

user2ProductsListCleanedRDD = user2ProductsListRDD.map(f=lambda item: (item[0], [(x.split("\t")[0], x.split("\t")[1]) for x in item[1]]))

finalRDD = user2ProductsListCleanedRDD.map(f=lambda x: (x[0], sorted(x[1], key=lambda item: item[1], reverse=True)))

firstFiveRDD = finalRDD.map(f=lambda item: (item[0], item[1][:5]))

start_time = time.time()
firstFiveRDD.collect()
end_time = time.time()
print("Total execution time: {} seconds".format(end_time - start_time))
print("ok")

firstFiveRDD.saveAsTextFile("file:///home/simoc/Documents/big_data/spark2output")
