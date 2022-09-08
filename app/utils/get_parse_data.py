from app.utils.process_recruit_detail_info import extract_info
from app.utils.process_job_info import handle_search
import re
from app.extensions import config_loader

all_provinces = config_loader.load_region()
"""
{'期望工作地点': '', '招工单位': [], '招工信息': [{'工种': ['吊顶'], '期望工作地点': '', '招工单位': [], 
'招工人数': [], '联系人': [], '联系电话': '15822775267'}], 
'联系人': '无', '联系电话': ['15822775267'], '联系微信': '无', '项目内容': '专业格栅;方通;矿棉板;'}
"""


def to_str(item):
    if type(item) == str:
        return item
    else:
        if not item:
            return ""
        return "".join(item)


def to_list(item):
    if type(item) == list:
        return item
    else:
        if not item:
            return []
        return [item]


def postprocess_working_place(working_place):
    if not working_place:
        return []
    new_working_place = []
    for item in working_place:
        if len(item) > 1:
            new_working_place.append(item)
    if len(new_working_place) == 1:
        if new_working_place[0] in all_provinces:
            return []
        else:
            return new_working_place
    else:
        return new_working_place


def format_return_result(res):
    formated_res = dict()
    working_place = to_list(res["期望工作地点"])
    # 处理单独省、市、区的情况，以及不正确的地址
    formated_res["期望工作地点"] = postprocess_working_place(working_place)
    # TODO:拍脑袋定的长度，后期修改
    recruit_company = to_list(res["招工单位"])
    if len(recruit_company) > 20:
        formated_res["招工单位"] = []
    else:
        formated_res["招工单位"] = recruit_company
    recruit_infos = res["招工信息"]
    formated_res["联系人"] = to_str(res["联系人"])
    formated_res["联系电话"] = to_list(res["联系电话"])
    formated_res["联系微信"] = to_str(res["联系微信"])
    formated_res["项目内容"] = res["项目内容"]
    new_recruit_info = []
    for each_info in recruit_infos:
        info_dict = dict()
        info_dict["工种"] = to_str(each_info["工种"])
        info_dict["期望工作地点"] = to_str(each_info["期望工作地点"])
        info_dict["招工单位"] = to_list(each_info["招工单位"])
        info_dict["招工人数"] = to_str(each_info["招工人数"])
        info_dict["联系人"] = to_list(each_info["联系人"])
        info_dict["联系电话"] = to_str(each_info["联系电话"])
        new_recruit_info.append(info_dict)
    formated_res["招工信息"] = new_recruit_info
    return formated_res


def seg_punc(msg):
    pattern = r'\n|\t|:|：|,|，| |!|！|\n'
    if not isinstance(msg, str):
        return {}
    result = re.split(pattern, msg)
    res, types, number, city, place, contact = extract_info(msg, None, None, None)
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
    res['项目内容'] = qa_sentence
    formated_res = format_return_result(res)
    return formated_res


def find_job(msg):
    pattern = r'\n|\t|:|：|,|，| |!|！|\n'
    if not isinstance(msg, str):
        return {}
    result = re.split(pattern, msg)
    res, person, city, types, contact = handle_search(msg)
    print(result)
    for i in range(len(result)):
        for j in range(len(person)):
            # print(types[j])
            p1 = re.compile(person[j])
            m = p1.findall(result[i])
            if len(m) != 0:
                result[i] = ""
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
    res["项目内容"] = qa_sentence
    formated_res = format_return_result(res)
    return formated_res
