# FitSense AI (Powered by Pandas & LLM) 🏋️‍♂️📊

> **基於 Python 與 NLP 的智慧運動數據分析助理**
> *An Intelligent Sports Data Assistant built with Python, Pandas, and AI-First workflow.*

## 📖 專案簡介 (Project Overview)
FitSense AI 是一個結合 **數據分析 (Data Analysis)** 與 **自然語言理解 (NLP)** 的後端系統。
解決了傳統運動數據儀表板「只能看、不能問」的痛點。使用者可以透過自然語言查詢（例如：「我這週哪天效率最好？」），系統會自動清洗數據、計算關鍵指標，並回傳可視化的分析結果。

本專案使用真實世界的 **Kaggle FitBit Dataset** 進行開發，並採用 **AI-First** 的模式進行高效率編碼。

## 🚀 核心功能 (Key Features)

### 1. 自動化數據清洗 (Data Cleaning Pipeline)
- [x] 自動偵測並填補空值 (Handling NaN with Mean/Interpolation)
- [x] 異常值過濾 (Outlier Detection)：自動剔除無效的穿戴裝置數據
- [x] 資料格式標準化 (DateTime Normalization)

### 2. 多維度量化分析 (Quantitative Analysis)
- [x] **燃脂效率計算**：分析步數與熱量消耗的相關係數 (Correlation Analysis)
- [x] **行為模式識別**：自動標記 "Active" (活躍) 與 "Sedentary" (久坐) 日期
- [ ] **趨勢預測**：基於歷史數據的簡單回歸分析 (Regression - *開發中*)

### 3. AI 語意理解與 API 服務 (NLP & Backend)
- [ ] **FastAPI 串接**：提供 RESTful API 供前端呼叫 (*開發中*)
- [ ] **意圖識別 (Intent Classification)**：解析使用者查詢意圖 (如：查詢統計、比較數據) (*開發中*)

## 🛠️ 技術堆疊 (Tech Stack)

| Category | Tools / Libraries |
|----------|-------------------|
| **Language** | Python 3.10+ |
| **Data Processing** | `pandas`, `numpy` |
| **Visualization** | `matplotlib`, `seaborn` |
| **Backend API** | `FastAPI`, `Uvicorn` (Planned) |
| **NLP** | `jieba`, `scikit-learn` (Planned) |
| **Dev Tools** | VS Code / Google Colab |

## 🤖 AI 工具協作 (AI-Assisted Development)
本專案展示了如何利用 AI 工具加速工程開發（符合 JD 要求）：
- **Cursor / GitHub Copilot**：輔助生成 80% 的 Boilerplate Code 與 Pandas 語法。
- **ChatGPT / Claude**：擔任 Pair Programmer，進行 Code Review 與架構優化。

## 📊 系統架構 (Architecture)

    [ User Query ] 
        ⬇️
    [ API Gateway (FastAPI) ]
        ⬇️
    [ NLP Parser (意圖分析) ] ➡️ [ Data Engine (Pandas 清洗與計算) ]
                                        ⬇️
                                [ JSON Response / Charts ]

## 📈 成果展示 (Demo)
*(此處將放置你的 `week_analysis.png` 截圖與 Postman API 測試截圖)*

---
*Created by Yen-Ting Wu | 2026*