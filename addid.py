#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import argparse
import sys
import base64

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='create new id field out of source_id and record_id, encode source_id to base64 too')
    parser.add_argument('-prefix',type=str,default="dswarm-",help='set prefix for new id-field.')
    args=parser.parse_args()
    
    for line in sys.stdin:
        try:
            jline=json.loads(line)
        except ValueError:
            print("unclean jsonline: ")
            print(line)
        if "source_id" in jline and  "record_id" in jline:
                jline["id"] = ( args.prefix + jline["source_id"] + "-" + str(base64.urlsafe_b64encode(bytes(jline["record_id"],'utf-8')).decode('utf-8')).rstrip('='))
                sys.stdout.write(json.dumps(jline,indent=None)+"\n")
