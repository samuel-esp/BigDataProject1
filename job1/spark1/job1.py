#!/usr/bin/env python3

"""spark application"""
import argparse
from pyspark.sql import SparkSession
import re
from datetime import datetime
from collections import Counter

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
    .appName("Job1 Spark") \
    .getOrCreate()

# read the input file and obtain an RDD with a record for each line
rdd = spark.sparkContext.textFile("/Users/samuel/Desktop/Reviews.csv").cache()

# remove csv header
removedHeaderRDD = rdd.filter(f=lambda word: not word.startswith("Id") and not word.endswith("Text"))

years2TextRDD = removedHeaderRDD.map(f=lambda line: (datetime.fromtimestamp(int(re.split(regex, line)[7])).strftime('%Y'), re.split(regex, line)[9]))

years2TextReducedRDD = years2TextRDD.reduceByKey(func=lambda a, b: a + " " + b)

years2WordRDD = years2TextReducedRDD.map(f=lambda item: (item[0], re.findall(r'[^,;\s]+', item[1])))

years2WordMostCommonRDD = years2WordRDD.map(f=lambda item: (item[0], Counter(item[1]).most_common()))

years2WordMostCommonRDDTopTen = years2WordMostCommonRDD.map(f=lambda item: (item[0], item[1][:10]))

# write all <year, list of (word, occurrence)> pairs in file
years2WordMostCommonRDDTopTen.saveAsTextFile(output_filepath)
