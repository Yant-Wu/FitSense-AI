import data_engine
import os

def process_query(user_query):
    """NLP處理"""
    query = user_query.lower()
    print(f'AI正在思考: {query}')

    if '分析' in query or 'analyze' in query or '相關' in query:
        print('進行資料分析...')
        df = data_engine.load_data(FILE_PATH)
        if df is not None:
            df_cleaned = data_engine.clean_data(df)
            corr = data_engine.analyze_correlation(df_cleaned)
            return f'步數與卡路里相關係數為 {corr:.4f}'
        else:
            return '無法讀取資料進行分析'
        
    elif "圖" in query or "plot" in query or "畫" in query:
        print('偵測意圖：[繪製圖表]')
        
        df = data_engine.load_data(FILE_PATH)
        if df is not None:
            df_clean = data_engine.clean_data(df)
            data_engine.plot_data(df_clean)
            return "圖表已生成！請開啟 'steps_vs_calories.png' 查看。"

    else:
        return "抱歉，我還在學習中。試試看輸入：'幫我分析資料' 或 '畫圖'。"
 
    





if __name__ == "__main__":
    FILE_PATH = 'data/mturkfitbit_export_3.12.16-4.11.16/Fitabase Data 3.12.16-4.11.16/dailyActivity_merged.csv'
    
    while True:
        try:
            user_input = input('請輸入指令: ')
            if user_input.strip() == "":
                continue
            
            response = process_query(user_input)
            print(f'AI回覆: {response}')
        except KeyboardInterrupt:
            print('\n程式結束')
            break
    
