import glob
import json
import sys


def load_json(file):
    with open(file, 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    return obj


if len(sys.argv) > 1:
    output = sys.argv[1]

    path = './lib/domains/'
    files = [f for f in glob.glob(path + "**/*.json", recursive=True)]

    hosts = []

    for f in files:
        j = load_json(f)
        try:
            a = j['pattern']
        except:
            a = j['host']
        hosts.append(a)

    hosts.sort()

    o = open(output, 'w')
    o.write("\n".join(hosts))
    o.close()
