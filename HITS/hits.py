# your code here 
from collections import defaultdict
import json

source_orig = []
destination_rev = []
destination_orig = []
source_rev = []
weight = []
wt = {}

with open('HITS.json') as data_file:
    for line in data_file:
        data = json.loads(line)
        if data['user']['id'] != data['retweeted_status']['user']['id']:
            source_orig.append(data['user']['id'])
            destination_rev.append(data['user']['id'])
            #print(data['user']['id'])
            destination_orig.append(data['retweeted_status']['user']['id'])
            source_rev.append(data['retweeted_status']['user']['id'])
            weight.append(data['retweeted_status']["retweet_count"])
            tup = (data['user']['id'], data['retweeted_status']['user']['id'])
            if tup in wt:
                wt[tup] +=1
            else:
                wt[tup] = 1


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        node = [v,w]
        self.graph[u].append(node)

        

g_orig = Graph()
g_rev = Graph()
# print(g)

for i in range(len(source_orig)):
    g_orig.addEdge(source_orig[i], destination_orig[i], weight[i])
    g_rev.addEdge(source_rev[i], destination_rev[i], weight[i])

# for i in range(10):
#     print(g_orig.graph[source_orig[i]])
    
# print("-----------------------------------------------------")

# for k,v in g_orig.graph.items():
#     print(k,v)
    
# print("-----------------------------------------------------")

# for i in range(10):
#     print(g_rev.graph[source_rev[i]])

#destination - g.graph[i][0][0]
#weights - g.graph[i][0][1]
        
print("Finished")
# print wt

# your code here
# Make a dictionary each for storing the hubs score and another for storing
# the authorities score.
dict_hubs= {}
dict_auth= {}

#Giving each hub and each authority a starting weight of 1
#g_orig.graph.keys() -- have the hubs
#g_rev.graph.keys() -- have the authorities

for i in g_orig.graph.keys():
    dict_hubs[i] = 1
    dict_auth[i] = 1
for i in g_orig.graph.values():
    dict_hubs[i[0][0]] = 1
    dict_auth[i[0][0]] = 1
#print(dict_auth)

# for i in g_orig.graph.keys():
#     print i

# # for i in g_rev.graph.keys():
# #     print i
    
'''
Now simply, for calculating the hubs score, we can get all the 
authorities a hub points to by g_orig.graph[source_orig[i][j][0]]

To calculate the authorities score, we can get all the hubs from the
g_rev.graph[source_rev[i][j][0]]
'''

summ = 0
# for j in range(len(g_orig.graph[source_orig[i]])):
#     summ += dict_auth[g_orig.graph[source_orig[i][j][0]]]
# dict_hubs[i] = summ
for i in range(200):
    for k,v in g_orig.graph.items():
        summ = 0
        for dest in v:
            if dest[0] in dict_auth:
                summ += dict_auth[dest[0]]
        dict_hubs[k]=summ
        
    #normalising the hub scores
    total = 0
    for k,v in dict_hubs.items():
        total += v**2
    
    for k,v in dict_hubs.items():
        dict_hubs[k] = v/(total**0.5)

    for k,v in g_rev.graph.items():
        summ = 0
        for dest in v:
            if dest[0] in dict_hubs:
                summ += dict_hubs[dest[0]]
        dict_auth[k]= summ
    
    total = 0
    for k,v in dict_auth.items():
        total += v**2
    
    for k,v in dict_auth.items():
        dict_auth[k] = v/(total**0.5)
        
sorted_hubs = sorted(dict_hubs.items(), key=lambda x:x[1], reverse=True)[:10]
sorted_auth = sorted(dict_auth.items(), key=lambda x:x[1], reverse=True)[:10]

print("Taking the Weighted graph..")
print("Top 10 Hubs Scores --")
for i in range(len(sorted_hubs)):
    print str(i+1) + '.' + ' ' + str(sorted_hubs[i][0]) + '  '+  str(sorted_hubs[i][1]) 
    
print("\n")
print("Top 10 Authorities Scores --")
for i in range(len(sorted_hubs)):
    print str(i+1) + '.' + ' ' + str(sorted_auth[i][0]) + '  '+  str(sorted_auth[i][1]) 
    

# your code here
# Make a dictionary each for storing the hubs score and another for storing
# the authorities score.
dict_hubs= {}
dict_auth= {}

#Giving each hub and each authority a starting weight of 1
#g_orig.graph.keys() -- have the hubs
#g_rev.graph.keys() -- have the authorities

#Initializing all the hubs and authorities scores
for i in g_orig.graph.keys():
    dict_hubs[i] = 1
    dict_auth[i] = 1
for i in g_orig.graph.values():
    dict_hubs[i[0][0]] = 1
    dict_auth[i[0][0]] = 1

'''
Now simply, for calculating the hubs score, we can get all the 
authorities a hub points to by g_orig.graph[source_orig[i][j][0]]

To calculate the authorities score, we can get all the hubs from the
g_rev.graph[source_rev[i][j][0]]
'''

summ = 0
# for j in range(len(g_orig.graph[source_orig[i]])):
#     summ += dict_auth[g_orig.graph[source_orig[i][j][0]]]
# dict_hubs[i] = summ
for i in range(200):
    for k,v in g_orig.graph.items():
        summ = 0
        for dest in v:
            if dest[0] in dict_auth:
                summ += dict_auth[dest[0]]/wt[(k,dest[0])]
        dict_hubs[k]=summ
        
    #normalising the hub scores
    total = 0
    for k,v in dict_hubs.items():
        total += v**2
    
    for k,v in dict_hubs.items():
        dict_hubs[k] = v/(total**0.5)

    for k,v in g_rev.graph.items():
        summ = 0
        for dest in v:
            if dest[0] in dict_hubs:
                summ += dict_hubs[dest[0]]/wt[(dest[0],k)]
        dict_auth[k]= summ
    
    total = 0
    for k,v in dict_auth.items():
        total += v**2
    
    for k,v in dict_auth.items():
        dict_auth[k] = v/(total**0.5)
        
sorted_hubs = sorted(dict_hubs.items(), key=lambda x:x[1], reverse=True)[:10]
sorted_auth = sorted(dict_auth.items(), key=lambda x:x[1], reverse=True)[:10]

print("Taking the Unweighted graph...")
print("Top 10 Hubs Scores --")
for i in range(len(sorted_hubs)):
    print str(i+1) + '.' + ' ' + str(sorted_hubs[i][0]) + '  '+  str(sorted_hubs[i][1]) 
    
print("\n")
print("Top 10 Authorities Scores --")
for i in range(len(sorted_hubs)):
    print str(i+1) + '.' + ' ' + str(sorted_auth[i][0]) + '  '+  str(sorted_auth[i][1]) 
    
