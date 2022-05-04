#!/usr/bin/env python3

"""spark application"""
import argparse
from pyspark.sql import SparkSession
import re
from operator import add

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
    .appName("Job3 Spark") \
    .config("spark.executor.instances", 15) \
    .getOrCreate()


def lists_intersect(l1, l2):
    if len(set(l1).intersection(l2)) >= 3:  # have 3 or more same elements
        return set(l1).intersection(l2)


# read the input file and obtain an RDD with a record for each line
rdd = spark.sparkContext.textFile("/Users/samuel/Desktop/Reviews.csv").cache()

# remove csv header
removedHeaderRDD = rdd.filter(f=lambda word: not word.startswith("Id") and not word.endswith("Text"))

filteredScoreRDD = removedHeaderRDD.filter(f=lambda line: int(re.split(regex, line)[4]) >= 4)

user2ProductsRDD = filteredScoreRDD.map(f=lambda line: (re.split(regex, line)[2], re.split(regex, line)[1]))

user2ProductsReducedRDD = user2ProductsRDD.reduceByKey(func=lambda a, b: a + " " + b)

filteredElementsRDD = user2ProductsReducedRDD.filter(f=lambda line: len(line[1]) >= 3)

user2ProductsList = filteredElementsRDD.map(f=lambda item: (item[0], item[1].split(" ")))

cartesianRDD = user2ProductsList.cartesian(user2ProductsList).filter(lambda x: x[0][0] != x[1][0] and lists_intersect(x[0][1], x[1][1]))

resultRDD = cartesianRDD.map(f=lambda x: (x[0][0], x[1][0], x[0][1]))

resultCleanedRDD = resultRDD.filter(lambda x: hash(x[0]) > hash(x[1]))

resultCleanedRDD.saveAsTextFile(output_filepath)