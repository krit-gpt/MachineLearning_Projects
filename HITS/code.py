# your code here 
import json
source = []
destination = []
weight = []
with open('test.json') as data_file:
    for line in data_file:
        data = json.loads(line)
        if data['user']['id'] != data['retweeted_status']['user']['id']:
            source.append(data['user']['id'])
            destination.append(data['retweeted_status']['user']['id'])
            weight.append(data['retweeted_status']["retweet_count"])

print(source)
print(destination)
print(weight)