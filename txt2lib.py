import sys
import pathlib
import json
import os.path


def array_reverse(lst):
    return [ele for ele in reversed(lst)]


def valid_sub_zone(hostname):
    return [x for x in hostname if x != '' and x != '*']


def process_row(row):
    hostname = str(row[0].replace('/', '')).split('.')
    host = valid_sub_zone(hostname)
    if len(host) > 1:
        zones = array_reverse(host)

        try:
            tcp = row[2].split(",")
        except:
            tcp = []

        try:
            udp = row[3].split(",")
        except:
            udp = []

        y = {
            'description': row[1],
            'host': ".".join(host),
            'tcp': tcp,
            'udp': udp
        }

        p = os.path.realpath("./lib/domains/" + "/".join(zones) + '.json')
        print("Line {}: {}".format(row[0], p))
        pretty = json.dumps(y, sort_keys=True, indent=4)

        dirname = os.path.dirname(p)
        pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)

        json_file = open(p, "w")
        json_file.write(pretty);
        json_file.close()


def import_file(filename):
    file1 = open(filename, 'r')
    count = 0

    while True:
        line = file1.readline()
        row = line.strip().split("\t")

        ## process row
        process_row(row)

        # if line is empty
        # end of file is reached
        if not line:
            break

    file1.close()


if len(sys.argv) == 2:
    filename = sys.argv[1]
    import_file(filename)

elif len(sys.argv) == 5:
    row = sys.argv
    del(row[0])
    process_row(row)