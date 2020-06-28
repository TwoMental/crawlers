# crawlers
## description
写过的一些爬虫汇总，仅供交流，爬虫有害网络环境，谨慎批量使用。

## structure
```python
├── ...
├── code                        # 代码部分
│   └── bilibili                ## b站相关
│       ├── danmaku_history.py  ### 历史弹幕爬虫
│       └── danmaku_recent.py   ### 最近弹幕爬虫
└── data                        # 样例数据部分，结构同代码部分
```

## usage
- 进入虚拟环境
`pipenv shell`
- 安装相关的包
`pipenv install`
- 运行特定爬虫
`python run.py ${web} ${crawler}`


## pppppre
*如果没有从第一句就跑不通请按需参考这里*
- mac
```shell
# 安装brew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# 安装pipenv
brew install pipenv
```


