# newspaper-manage-system

## 项目背景

本项目为我和[杜老大](https://github.com/dusz7)合作的外包项目。于我们大二末期编写。   
当时我二人即将结束上海快仓科技有限公司的实习，踏入大三生活，正值囊中羞涩，于是出卖了~~原本就没有的~~Geek精神，用廉价的劳动力换取了些许钱财。   
    
## 项目简介

### 概述

本项目分为server端、browser端以及Android端。我和杜老大发挥己长，我使用擅长的Python语言开发server端，杜老大使用Java语言开发Android端。
至于我俩均似懂非懂的大前端，就用半吊子水平共同开发，杜老大主要实现Html+css的UI部分，我主要实现Js的控制部分。   
该仓库存放server端与browser端代码，Android端的代码存放在[杜老大的家里](https://github.com/dusz7/NewspaperDemo)。   
    
### 目录

`app`目录下为该项目server端与browser端主要的代码实现，基于flask框架进行开发，前后端通信使用restful API，其中`app/api`为安卓端提供API，
`app/main`为browser端提供API，`app/static`存放所需静态文件，`app/template`存放前端模块。    
`doc`目录下为前后端接口文档。   
`script`为数据库、部署等相关的脚本。   

### 使用说明

运行前请使用pip安装相关依赖：

    sudo pip install -r requirements.txt

运行`manage.py`脚本打开服务器说明：

    python manage.py
    
使用`runserver`指令运行服务器：

    python manage.py runserver
    
### 部署

使用flask+nginx+gunicorn+supervisor方案。    
    
