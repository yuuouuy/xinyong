## 🧠 智能分析模块下载与配置说明

本模块为“社会信用治理决策支持与风险预警”系统的智能分析平台，支持 Docker 一键部署、可视化控制、知识库检索与 API 接入等功能。

------

### 📦 1. 模块下载

- **文件名**：`docker.tar.gz`
- **下载地址**：[百度网盘链接](https://pan.baidu.com/s/12MlBHLn3DXZgemoSMbQbfA?pwd=dpzt)
- **提取码**：`dpzt`

下载完成后请解压，并确保本地已安装以下环境：

-  Docker
-  Docker Compose

------

### 🚀 2. 启动服务

在解压后的目录下执行以下命令启动服务：

```bash
bash
cd docker
docker compose up -d
```

------

### 🌐 3. 登录与使用

启动成功后，在浏览器访问：

```bash
bash
http://localhost/signin
```

默认登录账号：

- 用户名：`739499915@qq.com`
- 密码：`a12345678`

![image-20250526170600153](../../xy_code/assets/image-a.png)

登录后点击顶部的「工作室」，选择：

> **社会信用治理决策支持与风险预警智能分析**

即可进入工作流管理界面。

操作流程：

1. 点击「发布」
2. 选择「发布更新」
3. 点击「运行」进入工作流执行界面

![image-20250526170812490](./xy_code/assets/image-b.png)

![image-20250526170834966](./xy_code/assets/image-c.png)

![image-20250526170852871](./xy_code/assets/image-d.png)

![image-20250526170907540](./xy_code/assets/image-e.png)

------

### 🔧 4. Nginx 配置说明（部署后端时用）

将以下配置加入服务器 Nginx 的 `server` 块中：

```
nginx复制编辑# 智能问答服务
location /chat/ {
    proxy_pass http://172.20.163.29/chat/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}

# 静态资源
location /_next/ {
    proxy_pass http://172.20.163.29/_next/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}

# 后端 API
location /api/ {
    proxy_pass http://172.20.163.29/api/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}

# logo 图标静态路径
location /logo/ {
    alias /home/casedb/logo/;
}

# 文件服务
location /files/ {
    proxy_pass http://172.20.163.29/files/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

> 💡 说明：
>
> - `172.20.163.29` 是智能问答服务的部署地址；
> - `/logo/` 路径应指向本机的实际 logo 文件目录，目录中需包含 `logo.png`，**文件名不可更改**。

------

### 📁 5. 数据存放与知识库导入

系统默认已加载 15,000 份裁判文书，相关数据源如下：

- 主数据包：
  - [百度网盘链接](https://pan.baidu.com/s/1uckC_LdmlkcnUxCKqxj0GQ?pwd=dc2k)
  - 提取码：`dc2k`
- 附加数据包：
  - [百度网盘链接](https://pan.baidu.com/s/1NByKKUikwSy10CrvgXXrEA?pwd=tfws)
  - 提取码：`tfws`

#### 添加知识库数据的方式：

1. 点击左侧导航中的 **知识库**；
2. 点击「创建知识库」或进入已有知识库点击「添加文件」；
3. 上传文档后，确保在**工作流中的知识检索节点添加了对应知识库**，并点击「发布」使其生效。

------

### 🔌 6. 使用“仅输出知识检索结果”的 API

在「工作室」中切换至：

> **社会信用治理决策支持与风险预警智能分析2**

操作步骤：

1. 点击「发布」；
2. 点击「发布更新」。

此时 API 即可正常使用。

------

### 🧪 7. 示例 API 请求

#### 🗝️ 默认 API Key：

- **完整回复**：`app-mmHO10g8e5SGJjvsbaxyQrG8`
- **仅返回知识检索内容**：`app-QNhleGtU1PmqzOI5hpWd90y8`

#### 📬 示例 curl 请求：

```bash
bash
curl -X POST "http://172.20.163.29/v1/chat-messages" \
--header "Authorization: Bearer app-QNhleGtU1PmqzOI5hpWd90y8" \
--header "Content-Type: application/json" \
--data-raw '{
  "inputs": {},
  "query": "为我介绍一个信用卡失信的案例",
  "response_mode": "blocking",
  "conversation_id": "",
  "user": "abc-123"
}'
```
