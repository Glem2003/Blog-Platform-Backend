# Blog Platform Backend with Markdown Support

## 專案目標
建立一個後端服務，支援創建、查看、更新、刪除文章，並且將 Markdown 內容轉換為 HTML 格式顯示。

## 技術栈
- **後端框架**：Flask
- **Markdown 轉換**：Markdown
- **資料儲存**：JSON 格式
- **API**：RESTful API

## 開發步驟與時間規劃

### 第 1 週：專案規劃與環境設置
- 設計 RESTful API 端點
- 設置專案環境並安裝相關依賴（Flask、Markdown）

### 第 2 週：API 開發與 Markdown 轉換功能
- 創建文章 API（POST /articles）
- 查看文章 API（GET /articles/{id}）
- 更新文章 API（PUT /articles/{id}）

### 第 3 週：錯誤處理、測試和優化
- 錯誤處理和測試
- 優化代碼結構

### 第 4 週：部署與最終測試
- 部署專案到 Heroku 或其他平台
- 測試並確保 API 正常運行

## API 端點設計
- **`GET /articles`** - 獲取所有文章
- **`GET /articles/{id}`** - 根據 ID 獲取單篇文章
- **`POST /articles`** - 創建文章
- **`PUT /articles/{id}`** - 更新文章
- **`DELETE /articles/{id}`** - 刪除文章

## 數據結構設計
```json
{
  "id": 1,
  "title": "Article Title",
  "content": "Markdown content converted to HTML.",
  "created_at": "2024-12-25T12:00:00",
  "updated_at": "2024-12-25T12:00:00"
}
```

## 專案目標
```json
/blog-platform-backend/
├── app.py                # Flask 應用的主程式
├── articles.json         # 儲存文章數據的 JSON 檔案
├── requirements.txt      # 依賴項
└──  README.md             # 專案描述文件
```

## 測試
### 測試每個 API 端點的功能：
- GET /articles
- GET /articles/{id}
- POST /articles
- PUT /articles/{id}
- DELETE /articles/{id}

## 部署
- 使用 Heroku 或其他平台來部署專案。
- 確保 API 能夠處理請求，並返回 JSON 格式的結果。