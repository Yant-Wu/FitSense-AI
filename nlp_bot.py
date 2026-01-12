import data_engine
import os
import re

FILE_PATH = 'data/mturkfitbit_export_3.12.16-4.11.16/Fitabase Data 3.12.16-4.11.16/dailyActivity_merged.csv'

INTENT = {
    "analyze_data": ["分析", "analyze", "相關", "correlation", "數據", "統計"],
    "plot_data": ["圖", "plot", "畫", "chart", "視覺化"],
    "predict": ["預測", "predict", "要是", "如果"]
}

def detect_intent(query):
    """偵測使用者意圖"""
    for intent, keywords in INTENT.items():
        if any(keyword in query for keyword in keywords):
            return intent
    return None

def process_query(user_query):
    """NLP處理"""
    query = user_query.lower()
    print(f'AI正在思考: {query}')

    intent = detect_intent(query)
    if intent == "analyze_data":
        print('進行資料分析...')
        df = data_engine.load_data(FILE_PATH)
        if df is not None:
            df_cleaned = data_engine.clean_data(df)
            corr = data_engine.analyze_correlation(df_cleaned)
            return f'步數與卡路里相關係數為 {corr:.4f}'
        else:
            return '無法讀取資料進行分析'
        
    elif intent == "plot_data":
        print('偵測意圖：[繪製圖表]')
        
        df = data_engine.load_data(FILE_PATH)
        if df is not None:
            df_clean = data_engine.clean_data(df)
            data_engine.plot_data(df_clean)
            return "圖表已生成！請開啟 'steps_vs_calories.png' 查看。"
        
    elif intent == "predict":
        print('偵測意圖：[預測卡路里]')
        match = re.search(r'\d+', query)
        if match:
            steps_input = int(match.group())
            if steps_input <= 100:
                return "步數應大於100才能進行預測。"
            
            df = data_engine.load_data(FILE_PATH)
            if df is not None:
                df_clean = data_engine.clean_data(df)
                predicted_val = data_engine.predict_calories(df_clean, steps_input)
                return f'如果你走了 {steps_input} 步，預計會燃燒約 {predicted_val:.2f} 卡路里。'
        else:
            return "你想預測多少步請輸入數字，例如：預測 20000 步"


    else:
        return "抱歉，我還在學習中。試試看輸入：'幫我分析資料' 或 '畫圖'。"
 


if __name__ == "__main__":
    while True:
        try:
            print('==============================================')
            user_input = input('請輸入指令: ')
            if user_input.strip() == "":
                continue
            
            response = process_query(user_input)
            print(f'AI回覆: {response}')
        except KeyboardInterrupt:
            print('\n程式結束')
            break
    
