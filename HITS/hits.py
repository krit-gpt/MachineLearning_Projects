# your code here 
from collections import defaultdict


import json
source = []
destination = []
weight = []
with open('HITS.json') as data_file:
    for line in data_file:
        data = json.loads(line)
        if data['user']['id'] != data['retweeted_status']['user']['id']:
            source.append(data['user']['id'])
            #print(data['user']['id'])
            destination.append(data['retweeted_status']['user']['id'])
            weight.append(data['retweeted_status']["retweet_count"])

# print(source)
# print(destination)
# print(weight)

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        node = [v,w]
        self.graph[u].append(node)

        

g = Graph()
# print(g)

for i in range(len(source)):
    g.addEdge(source[i], destination[i], weight[i])

for i in range(1000):
    print(g.graph[source[i]])

#destination - g.graph[i][0][0]
#weights - g.graph[i][0][1]
        
