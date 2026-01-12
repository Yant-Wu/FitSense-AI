import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # 進階視覺化套件適合數據分析


def load_data(filepath):
    if os.path.exists(filepath):
        # print('檔案已成功讀取')
        df = pd.read_csv(filepath)
        # print(df.columns)
        # print(df.head(5))
        return df
    else:
        print('確認檔案路徑')
        return None

def clean_data(df):
    original_count = len(df)
    # print(f'原始資料筆數: {original_count}')

    # 資料清洗保留不數到>=100 代表有在動的，.copy避免刪到原本的df
    df_cleaned = df[df['TotalSteps'] >= 100].copy()
    dropped_count = original_count - len(df_cleaned)
    # print(f'刪除不活躍資料筆數: {dropped_count}')
    return df_cleaned

def analyze_correlation(df):
    """開始分析"""
    corr = df['TotalSteps'].corr(df['Calories'])
    # print(f'步數與卡路里相關係數: {corr:.4f}')

    if corr > 0.7:
        print('步數與卡路里高度相關')
    elif corr > 0.3:
        print('步數與卡路里中度相關')
    else:
        print('步數與卡路里低度相關')
    return corr


def plot_data(df):
    """繪製圖表"""
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df, x='TotalSteps', y='Calories', hue='VeryActiveMinutes', palette='viridis')
    plt.title('analysis of Steps vs Calories')
    plt.xlabel('steps')
    plt.ylabel('calories burned')
    plt.savefig('steps_vs_calories.png')
    plt.close()



if __name__ == "__main__":
    FILE_PATH = 'data/mturkfitbit_export_3.12.16-4.11.16/Fitabase Data 3.12.16-4.11.16/dailyActivity_merged.csv'
    
    df = load_data(FILE_PATH)
    if df is not None:
        df_cleaned = clean_data(df)
        analyze_correlation(df_cleaned)
        plot_data(df_cleaned)