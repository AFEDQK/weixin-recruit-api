from app.utils.process_recruit_detail_info import extract_info
from app.utils.process_job_info import handle_search
import re


def seg_punc(msg):
    pattern = r'\n|\t|:|：|,|，| |!|！|\n'
    result = re.split(pattern, msg)
    res, types, number, city, place, contact = extract_info(msg, None, None, None)
    print(result)
    for i in range(len(result)):
        for j in range(len(types)):
            p1 = re.compile(types[j])
            m = p1.findall(result[i])
            if len(m) != 0:
                result[i] = ""
        for j in range(len(number)):
            p1 = re.compile(number[j])
            m = p1.findall(result[i])
            if len(m) != 0:
                result[i] = ""
        for j in range(len(city)):
            p1 = re.compile(city[j])
            m = p1.findall(result[i])
            if len(m) != 0:
                result[i] = ""

        for j in range(len(place)):
            p1 = re.compile(place[j])
            m = p1.findall(result[i])
            # print("招工单位匹配：", m)
            if len(m) != 0:
                result[i] = ""
                # print("招工单位匹配成功，以用空格替换")
        for j in range(len(contact)):
            p1 = re.compile(contact[j])
            m = p1.findall(result[i])
            # print("联系电话匹配：", m)
            if len(m) != 0:
                result[i] = ""
                # print("联系电话匹配成功，以用空格替换")

        p1 = re.compile("联系电话|报名电话|电话")
        m = p1.findall(result[i])
        # print(m)
        if len(m) != 0:
            result[i] = ""
            # print("匹配到")

    qa_sentence = ""
    for i in range(len(result)):
        # print(result[i])
        if len(result[i]) != 0:
            qa_sentence += result[i]
            qa_sentence += ";"
        # print(qa_sentence)
        # if i == len(result) - 1:
        #     qa_sentence += "。"
    # print(qa_sentence)
    res['项目内容'] = qa_sentence

    # json_data = json.dumps(res, indent=4, ensure_ascii=False)
    # return json_data
    return res

def find_job(msg):
    pattern = r'\n|\t|:|：|,|，| |!|！|\n'
    result = re.split(pattern, msg)
    res, person, city, types, contact = handle_search(msg)
    # types = "你好"
    # print(len(types))
    print(result)
    for i in range(len(result)):
        # print("测试", i, "：", result[i])
        for j in range(len(person)):
            # print(types[j])
            p1 = re.compile(person[j])
            m = p1.findall(result[i])
            # print("工种匹配：", m)
            if len(m) != 0:
                result[i] = ""
                # print("工种匹配成功，以用空格替换")
                # print("工种为：", types[j])
        for j in range(len(city)):
            p1 = re.compile(city[j])
            m = p1.findall(result[i])
            # print("人数匹配：", m)
            if len(m) != 0:
                result[i] = ""
                # print("人数成功，以用空格替换")
        for j in range(len(types)):
            p1 = re.compile(types[j])
            m = p1.findall(result[i])
            # print("期望工作地点匹配：", m)
            if len(m) != 0:
                result[i] = ""
                # print("期望工作地点匹配成功，以用空格替换")
        for j in range(len(contact)):
            p1 = re.compile(contact[j])
            m = p1.findall(result[i])
            # print("招工单位匹配：", m)
            if len(m) != 0:
                result[i] = ""
                # print("招工单位匹配成功，以用空格替换")

        p1 = re.compile("联系电话|报名电话|电话")
        m = p1.findall(result[i])
        # print(m)
        if len(m) != 0:
            result[i] = ""
            # print("匹配到")

    qa_sentence = ""
    for i in range(len(result)):
        # print(result[i])
        if len(result[i]) != 0:
            qa_sentence += result[i]
            qa_sentence += ";"
        # print(qa_sentence)
        # if i == len(result) - 1:
        #     qa_sentence += "。"
    # print(qa_sentence)
    res['项目内容'] = qa_sentence
    # json_data = json.dumps(res, indent=4, ensure_ascii=False)
    return res

