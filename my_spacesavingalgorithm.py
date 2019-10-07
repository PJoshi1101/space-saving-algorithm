# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:19:32 2019

@author: pooja
"""

#from collections import Counter
import json
import matplotlib.pyplot as mp
import os

#----------------------------------------------------------------------------------------------#
#class to implement space saving algorithm.
#consists of 4 methods used to perform task listed below
#If value is present in the dictionary, increment the counter, 
#else add the value to the dictionary
#if counter is full(depends on K) get least common element from the dictionany, 
#replace the value and increment the counter
#----------------------------------------------------------------------------------------------#
class space_saving:
    
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

#function to increment the count in the dictionary.
#input param - dictionary object, dictionary key
#output param - modified dictionary object        
    def inc_count(my_dict,item):
        my_dict[item] = my_dict[item] + 1
        return my_dict
    
#function to add element in the dictionary.
#input param - dictionary object, dictionary key
#output param - modified dictionary object
    def add_element(my_dict,item):
        my_dict[item] = 1
        return my_dict
    
#function to get the least count from the counter and replace it with given item.
#incrment the counter by 1
#input param - dictionary object, dictionary key
#output param - modified dictionary object
    def replace_element(my_dict,item):
        my_dict[item] = my_dict.pop(my_dict.most_common()[:-2:-1][0][0])
        my_dict[item] = my_dict[item] + 1
        return my_dict
     
#function get top k elements from the dictionary.
#input param - dictionary object, top k value
#output param - dictionary of top k value
    def countTopK(my_dict, n):
        return my_dict.most_common(n)
    
#function to plot the bar graph
#input param - plot_data - data to plot,
#               x_label - text to display on x-axis
#               y_label - text to display on y-axis
#               title - graph title
#               imgname - image name to save the output        
#output param - bar graph        
def plot(plot_data,x_label,y_label,title,imgname):
    
    Xaxis = []
    Yaxis = []
    
    for x in range(len(plot_data)):
        Xaxis.append(plot_data[x][0])
    
    for y in range(len(plot_data)):
        Yaxis.append(plot_data[y][1])
        
    mp.figure(figsize = (10,3))
    mp.xticks(rotation = 90)    
    mp.title(title)
    mp.xlabel(x_label)
    mp.ylabel(y_label)
        
    mp.bar(Xaxis,Yaxis)
    
#save the chart in working directory location
    mp.savefig(imgname,bbox_inches="tight")
  
#function will read the json file
#@inputparam - jsonfile
#@outputparam - json data
def readjsonfile(path):
    
    print("Start Execution----readjsonfile")
    
    with open(path) as json_file:
           json_data = json.load(json_file)
    
    print("End Execution----readjsonfile")
       
    return json_data

#function to fetch all the files of type json
#input param - file path
#output param - array of json files

def get_filesfromdir(path):
    files = []
    
# loop to read all the files of type json from the specified filepath
# r=root, d=directories, f = files
    for r, d, f in os.walk(path):
       for file in f:
           if '.json' in file:
               files.append(os.path.join(path, file))

    return files


             