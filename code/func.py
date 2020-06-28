import os, sys

def get_data_path(code_name):
    code_path = "/".join(code_name.split('/')[:-1])
    data_path = code_path.replace("code", "data")
    data_name = code_name.replace("code", "data").replace(".py", ".csv")
    if not os.path.exists(data_path):
        os.mkdir(data_path)
    return data_name

def get_args(web, crawler):
    relation = {
        "bilibili": {
            "danmaku_history": {
                "av": "请输入视频av号",
                "start_day": "请输入起始日期，如2020-01-01",
                "end_day": "请输入结束日期，如2020-01-02"
            }
        }
    }
    return relation[web][crawler]