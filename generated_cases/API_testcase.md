根据您提供的OpenAPI定义，我将为 `/users` (GET, POST) 和 `/users/{userId}` (GET) 接口生成标准格式的测试用例。

### 接口 1: GET /users (获取用户列表)

**TC_GetUsers_01**
*   **Test Title**: 正常场景 - 获取用户列表（默认页码）
*   **Preconditions**: 系统中存在至少一个用户。
*   **Test Steps**:
    1.  向 `/users` 发送 GET 请求。
*   **Test Data**: 无
*   **Expected Result**: HTTP 状态码 200。响应体为 JSON 格式，包含 `code: 200` 和 `data` 字段，`data` 是一个包含用户对象的数组。

**TC_GetUsers_02**
*   **Test Title**: 正常场景 - 获取用户列表（指定页码）
*   **Preconditions**: 系统中存在多页用户数据。
*   **Test Steps**:
    1.  向 `/users` 发送 GET 请求，并指定 `page` 参数。
*   **Test Data**: `page=2`
*   **Expected Result**: HTTP 状态码 200。响应体为 JSON 格式，包含 `code: 200` 和 `data` 字段，`data` 是第二页的用户数组。

**TC_GetUsers_03**
*   **Test Title**: 边界值 - 页码为最小值
*   **Preconditions**: 系统中存在用户。
*   **Test Steps**:
    1.  向 `/users` 发送 GET 请求，并指定 `page` 参数为最小值。
*   **Test Data**: `page=1`
*   **Expected Result**: HTTP 状态码 200。响应体为 JSON 格式，包含 `code: 200` 和 `data` 字段，`data` 是第一页的用户数组。

**TC_GetUsers_04**
*   **Test Title**: 边界值 - 页码为极大值
*   **Preconditions**: 系统中用户数据量有限。
*   **Test Steps**:
    1.  向 `/users` 发送 GET 请求，并指定一个非常大的 `page` 参数。
*   **Test Data**: `page=999999`
*   **Expected Result**: HTTP 状态码 200。响应体为 JSON 格式，包含 `code: 200` 和 `data` 字段，`data` 为空数组或符合业务逻辑的响应。

**TC_GetUsers_05**
*   **Test Title**: 参数类型错误 - 页码为非整数
*   **Preconditions**: 无
*   **Test Steps**:
    1.  向 `/users` 发送 GET 请求，并指定一个非整数的 `page` 参数。
*   **Test Data**: `page=abc`
*   **Expected Result**: HTTP 状态码 400 或 422（取决于框架实现）。响应体应包含错误信息。

---

### 接口 2: POST /users (创建用户)

**TC_CreateUser_01**
*   **Test Title**: 正常场景 - 创建用户（提供所有字段）
*   **Preconditions**: 提供的邮箱在系统中不存在。
*   **Test Steps**:
    1.  向 `/users` 发送 POST 请求，请求体包含所有字段。
*   **Test Data**:
    ```json
    {
      "name": "赵六",
      "email": "zhaoliu@example.com",
      "age": 30
    }
    ```
*   **Expected Result**: HTTP 状态码 201。响应体为 JSON 格式，包含 `code: 201`、`message: “创建成功”` 和 `data` 字段。`data` 中应包含新创建的用户信息（如 `id`, `name`, `email`）。

**TC_CreateUser_02**
*   **Test Title**: 正常场景 - 创建用户（仅提供必填字段）
*   **Preconditions**: 提供的邮箱在系统中不存在。
*   **Test Steps**:
    1.  向 `/users` 发送 POST 请求，请求体仅包含必填字段。
*   **Test Data**:
    ```json
    {
      "name": "孙七",
      "email": "sunqi@example.com"
    }
    ```
*   **Expected Result**: HTTP 状态码 201。响应体为 JSON 格式，包含 `code: 201`、`message: “创建成功”` 和 `data` 字段。`data` 中应包含新创建的用户信息。

**TC_CreateUser_03**
*   **Test Title**: 缺失参数 - 缺少必填字段 `name`
*   **Preconditions**: 无
*   **Test Steps**:
    1.  向 `/users` 发送 POST 请求，请求体缺少 `name` 字段。
*   **Test Data**:
    ```json
    {
      "email": "test@example.com"
    }
    ```
*   **Expected Result**: HTTP 状态码 400。响应体应包含错误信息，表明缺少必要字段或参数错误。

**TC_CreateUser_04**
*   **Test Title**: 缺失参数 - 缺少必填字段 `email`
*   **Preconditions**: 无
*   **Test Steps**:
    1.  向 `/users` 发送 POST 请求，请求体缺少 `email` 字段。
*   **Test Data**:
    ```json
    {
      "name": "测试用户"
    }
    ```
*   **Expected Result**: HTTP 状态码 400。响应体应包含错误信息，表明缺少必要字段或参数错误。

**TC_CreateUser_05**
*   **Test Title**: 参数格式错误 - `email` 格式无效
*   **Preconditions**: 无
*   **Test Steps**:
    1.  向 `/users` 发送 POST 请求，请求体中 `email` 字段格式不符合邮箱规范。
*   **Test Data**:
    ```json
    {
      "name": "测试用户",
      "email": "invalid-email"
    }
    ```
*   **Expected Result**: HTTP 状态码 400。响应体应包含错误信息，表明邮箱格式无效。

**TC_CreateUser_06**
*   **Test Title**: 参数类型错误 - `age` 字段类型错误
*   **Preconditions**: 无
*   **Test Steps**:
    1.  向 `/users` 发送 POST 请求，请求体中 `age` 字段为字符串类型。
*   **Test Data**:
    ```json
    {
      "name": "测试用户",
      "email": "test@example.com",
      "age": "twenty"
    }
    ```
*   **Expected Result**: HTTP 状态码 400。响应体应包含错误信息，表明参数类型不匹配。

**TC_CreateUser_07**
*   **Test Title**: 边界值 - `age` 为最小值（假设为0）
*   **Preconditions**: 提供的邮箱在系统中不存在。
*   **Test Steps**:
    1.  向 `/users` 发送 POST 请求，请求体中 `age` 字段为最小值。
*   **Test Data**:
    ```json
    {
      "name": "边界用户",
      "email": "boundary@example.com",
      "age": 0
    }
    ```
*   **Expected Result**: HTTP 状态码 201 或 400（取决于业务规则）。若成功，响应体包含新用户信息；若失败，响应体包含相关错误信息。

**TC_CreateUser_08**
*   **Test Title**: 边界值 - `age` 为极大值（假设为150）
*   **Preconditions**: 提供的邮箱在系统中不存在。
*   **Test Steps**:
    1.  向 `/users` 发送 POST 请求，请求体中 `age` 字段为一个极大值。
*   **Test Data**:
    ```json
    {
      "name": "边界用户",
      "email": "boundary2@example.com",
      "age": 150
    }
    ```
*   **Expected Result**: HTTP 状态码 201 或 400（取决于业务规则）。若成功，响应体包含新用户信息；若失败，响应体包含相关错误信息。

---

### 接口 3: GET /users/{userId} (获取用户详情)

**TC_GetUserDetail_01**
*   **Test Title**: 正常场景 - 获取存在的用户详情
*   **Preconditions**: 系统中存在一个 ID 为 1 的用户。
*   **Test Steps**:
    1.  向 `/users/1` 发送 GET 请求。
*   **Test Data**: `userId=1`
*   **Expected Result**: HTTP 状态码 200。响应体为 JSON 格式，包含 `code: 200` 和 `data` 字段。`data` 中应包含该用户的完整信息（如 `id`, `name`, `email`, `age`）。

**TC_GetUserDetail_02**
*   **Test Title**: 异常场景 - 用户ID不存在
*   **Preconditions**: 系统中不存在 ID 为 99999 的用户。
*   **Test Steps**:
    1.  向 `/users/99999` 发送 GET 请求。
*   **Test Data**: `userId=99999`
*   **Expected Result**: HTTP 状态码 404。响应体应包含用户不存在的错误信息。

**TC_GetUserDetail_03**
*   **Test Title**: 参数类型错误 - 用户ID为非数字
*   **Preconditions**: 无
*   **Test Steps**:
    1.  向 `/users/abc` 发送 GET 请求。
*   **Test Data**: `userId=abc`
*   **Expected Result**: HTTP 状态码 400 或 404（取决于路由匹配）。响应体应包含错误信息。

**TC_GetUserDetail_04**
*   **Test Title**: 边界值 - 用户ID为最小值（假设为1）
*   **Preconditions**: 系统中存在 ID 为 1 的用户。
*   **Test Steps**:
    1.  向 `/users/1` 发送 GET 请求。
*   **Test Data**: `userId=1`
*   **Expected Result**: HTTP 状态码 200。成功获取到用户详情。

**TC_GetUserDetail_05**
*   **Test Title**: 边界值 - 用户ID为0或负数
*   **Preconditions**: 无
*   **Test Steps**:
    1.  向 `/users/0` 发送 GET 请求。
*   **Test Data**: `userId=0`
*   **Expected Result**: HTTP 状态码 404 或 400。响应体应包含错误信息。