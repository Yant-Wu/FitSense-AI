import data_engine
import os
import re
import ollama

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

def generate_llm_response(user_query, context_data):
    """使用ollama生成回覆"""
    prompt = f"""
    你是一個專業、幽默的 AI 健身教練 FitSense。
    
    【真實數據分析結果】：
    {context_data}
    
    【使用者的問題】：{user_query}
    
    請根據數據回答，若無相關數據則憑常識回答。
    """
    try:
        response = ollama.chat(model="llama3.2", messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']
    except Exception as e:
        return f"連接失敗"



def process_query(user_query):
    
    query = user_query.lower()
    print(f'AI正在思考: {query}')

    intent = detect_intent(query)
    df = data_engine.load_data(FILE_PATH)
    if df is None:
        return '無法讀取資料進行分析'
    df_cleaned = data_engine.clean_data(df)

    if intent == "analyze_data":
        print('進行資料分析...')
        corr = data_engine.analyze_correlation(df_cleaned)
        summary = f"總筆數: {len(df_cleaned)}, 相關係數: {corr:.4f}"
        context = f"數據摘要: {summary}"
        return generate_llm_response(user_query, context)
        
    elif intent == "plot_data":
        data_engine.plot_data(df_cleaned)
        return "圖表已生成！請開啟 'steps_vs_calories.png' 查看。"
        
    elif intent == "predict":
        match = re.search(r'\d+', query)
        if match:
            steps = int(match.group())
            pred_cal = data_engine.predict_calories(df_cleaned, steps)
            context = f"使用者想走 {steps} 步，模型預測消耗 {int(pred_cal)} 卡路里。"
            return generate_llm_response(user_query, context)
        else:
            return "你想預測多少步？請給我一個數字。"
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
    
