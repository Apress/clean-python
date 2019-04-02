import json

data = {'a':12, 'b':{'x':87, 'y':{'t1': 21, 't2':34}}
json.dumps(data, sort_keys=True, indent=4)
