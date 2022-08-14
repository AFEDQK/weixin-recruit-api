# -*- coding: utf-8 -*- #
# @Time : 2022/8/14 22:59
import csv
import json
import time

import requests


def load_data(fp):
    data = []
    with open(fp, "r", encoding="utf-8") as fd:
        reader = csv.reader(fd)
        next(reader)
        for line in reader:
            if not line:
                continue
            data.append(line[0])
    print(len(data))
    print(data)
    return data


url = "http://127.0.0.1:2022/msgProcess/recruit"


def test_special_example(data):
    result = []
    start_time = time.time()
    for text in data:
        ret = requests.get(url, data={"text": text})
        res = json.loads(ret.text)
        if not res:
            continue
        result.append((text, res))
    end_time = time.time()
    consume_time = end_time - start_time
    print(f"consume_time:{consume_time}")
    return result


def write_to_csv(save_fp, result):
    with open(save_fp, "w", encoding="utf-8", newline="") as fd:
        writer = csv.writer(fd)
        writer.writerow(["text", "result"])
        writer.writerows(result)


def main():
    fp = "false_examples.csv"
    data = load_data(fp)
    result = test_special_example(data)
    save_fp = "examples_result.csv"
    write_to_csv(save_fp, result)


if __name__ == '__main__':
    main()
