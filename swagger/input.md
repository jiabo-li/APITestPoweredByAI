openapi: 3.0.0
info:
  title: 用户管理 API
  description: 简单示例文档
  version: 1.0.0

servers:
  - url: https://api.example.com/v1
    description: 生产环境
  - url: http://localhost:8080/v1
    description: 本地环境

paths:
  /users:
    get:
      summary: 获取用户列表
      parameters:
        - name: page
          in: query
          description: 页码
          required: false
          schema:
            type: integer
            default: 1
      responses:
        '200':
          description: 成功
          content:
            application/json:
              example:
                code: 200
                data:
                  - id: 1
                    name: 张三
                    email: zhangsan@example.com
                  - id: 2
                    name: 李四
                    email: lisi@example.com

    post:
      summary: 创建用户
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - name
                - email
              properties:
                name:
                  type: string
                email:
                  type: string
                  format: email
                age:
                  type: integer
            example:
              name: 王五
              email: wangwu@example.com
              age: 25
      responses:
        '201':
          description: 创建成功
          content:
            application/json:
              example:
                code: 201
                message: 创建成功
                data:
                  id: 3
                  name: 王五
                  email: wangwu@example.com
        '400':
          description: 参数错误

  /users/{userId}:
    get:
      summary: 获取用户详情
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: integer
          description: 用户ID
      responses:
        '200':
          description: 成功
          content:
            application/json:
              example:
                code: 200
                data:
                  id: 1
                  name: 张三
                  email: zhangsan@example.com
                  age: 28
        '404':
          description: 用户不存在