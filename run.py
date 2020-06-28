import importlib
import sys

from code.func import get_args

def run(web, crawler):
    """
    运行指定爬虫脚本
    Parameters
    ----------
    web : string
        网站名称
    crawler : string
        爬虫类型
    """
    # 脚本名
    module_name = f"code.{web}.{crawler}"
    # 获取所需参数
    args = get_args(web, crawler)
    for arg, des in args.items():
        args[arg] = str(input(f"{des}: "))
    # 运行
    module = importlib.import_module(module_name) 
    module.run(**args)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])