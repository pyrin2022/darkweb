#!/usr/bin/python
# -*- coding: euc-kr -*-

import os
import csv
import time
import datetime

def main():
    start = time.time()
    dir = "G:\\독수리\\medi1121"
    files=os.listdir(dir)
    files_csv = [f for f in files if f.endswith('.csv')]
    #print("filename:", files_csv)
    domain_file = "G:\\독수리\\email.csv"
    result_file = "G:\\독수리\\1121_result.csv"
    domain_list = []

    f = open(domain_file, "r")
    lines = f.readlines()
    f.close()
    for line in lines :
        line = line.strip()
        domain_list.append(line)
    #print(domain_list)

    for file in files_csv:
        print(os.path.join(dir, file))
        f = open(os.path.join(dir, file), "r", encoding='utf-8', errors='ignore')
        lines = f.readlines()
        f.close()

        count = 0
        total_count = 0
        for line in lines :
            line = line.strip()

            is_found=0
            for domain in domain_list :
                numbers = line.lower().find(domain)
                if numbers != -1 :
                    is_found = 1
                    break

            if is_found == 1:
                out = open(result_file, "a", encoding='utf-8', errors='ignore')
                out.write("%s\n" % (line))
                out.close()

            count += 1
            if count % 100000 == 0 :
                print (count)
            total_count += count

    sec = time.time() - start
    times = str(datetime.timedelta(seconds=sec))
    exe_time = times.split(".")[0]
    print("exec time: ", exe_time," count: ", total_count )

    if os.path.isfile(result_file) == False:
        print("No matches...")

if __name__ == "__main__":
    main()