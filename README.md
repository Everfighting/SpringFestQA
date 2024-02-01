<div align="center">
    <img src="https://github.com/Everfighting/SpringFestQA/blob/main/assets/logo.jpeg" width=30% />
</div>

# SpringFestQA（年关走亲访友渡劫助手）

## 介绍
    SpringFestQA（年关走亲访友渡劫助手）收集了网络上中国春节的怼亲戚语录，
    基于InternLM2进行微调以及检索增强链生成的模仿年轻人语气对亲戚提问作出巧妙回答的语言模型。
    过年走亲访友过程中，难免遇到亲戚的热辣提问让你不知所措，还在为躺在床上才回想起来如何回怼而感到懊恼吗？
    直接将棘手的提问交给大模型，让亲戚哑口无言。
    
    在可视化网页界面中，我们提供了三种不同的回答风格：委婉认真、转换话题和阴阳怪气，
    以满足不同性格的人的回答需求。通过直接点击右侧的按钮，可以生成对应风格的回答。

## OpenXLab体验地址：
```
https://openxlab.org.cn/apps/detail/SijieLyu/SpringFestQA
```
## SpringFestQA整体流程框架
待流程图完成后补充到这里

## 数据收集
    数据集放在本仓库的data目录下：
### 1）MBTI
    为开源的MBTI中文版本数据集，jason格式，包含四个主题：感情、收入、学业、房子这四类。
    具体可参考 https://github.com/PKU-YuanGroup/Machine-Mindset/tree/main/datasets/behaviour
### 2）origin_data
    用ChatGLM生成的五种风格的数据库，csv格式，分别是诙谐幽默、转换话题、委婉回答、阴阳怪气、故作神秘/深沉，
    每种数据1万条，保证数据量足够，并在调试过程中优化为3种稳定且差异性输出的风格。
### 3）alpaca_data
    以origin_data为原始数据转换成的json格式数据，转换代码可参考convert.py

## 基于大语言模型的数据增广方法
    - 先行人工拟定对于回答的基于不同风格的少量样例数据
    - 根据少量数据构造对应的prompt
    - 将prompt输入LLM生成更多的数据语料
    - 对语料进行人工审核构建对应的训练数据集

## 模型微调
    依据MBTI数据和QA对，使用Xtuner对InternLM-Chat-7B的性格和内在知识储备进行部分参数微调，形成微调后的模型SpringFest。
    性格的训练出来但回答不太有用，要多轮对话才能体现人格，但大模型多轮对话能力有限，发现效果不如预期。【可以在gradio页面上增加I/E选项，后端可调用不同模型】

## 构建知识库（RAG）
    依据QA对，基于langchain框架构建进行embedding，形成外挂知识库，可以针对用户的 query 进行语义向量检索，得到与用户提问相关的知识片段。【可以在页面上增加prompt提示】
    Prompt调优
    当知识库内容不足时，转而激发微调后的SpringFest大模型能力，用incontext-learning的方法给模型展示正确的例子生成回答，
    包括但不限于：
    1.使用system prompt让模型明确任务；
    2.通过委婉认真、转移话题、阴阳怪气三个风格的内置prompt，满足用户自行切换回答风格的需求。
    [图片]

## ModelScope模型
### 模型权重下载(代码中已内置下载，不需要操作)
    https://www.modelscope.cn/binbeing/SpringFestQA.git
    SpringFestQA是InternLM2为底座模型，使用春节话题数据集和性格数据集，通过XTuner进行微调后获得的模型。可安装modelscope库后按以下命令进行下载：
    ```
    import torch
    from modelscope import snapshot_download, AutoModel, AutoTokenizer
    import os
    model_dir = snapshot_download('binbeing/SpringFestQA', cache_dir='./')
    ```
## 模型部署
- 部署到应用平台（以OpenXLab为例）
仅需要 Fork 本仓库，然后在 OpenXLab 上创建一个新的项目，将 Fork 的仓库与新建的项目关联，即可在 OpenXLab 上部署 SpringFestQA。
- 部署到本地（以InternStudio开发机为例）
    ```
    git clone https://github.com/Lyusijie/SpringFestQA.git
    
    python app.py

    ssh -CNg -L 7860:127.0.0.1:7860 root@ssh.intern-ai.org.cn -p 33471做端口转发（
            其中33471改为自己开发机端口）
    ```
- 本地网页打开：127.0.0.1:7860
