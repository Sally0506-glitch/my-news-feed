import requests
from bs4 import BeautifulSoup
import datetime

def create_content():
    print("ニュースを取得中(RSS)...")
    # Yahoo!ニュースの主要トピックスRSS（ここは構造が変わらないので安定しています）
    url = "https://news.yahoo.co.jp/rss/topics/top-picks.xml"
    
    try:
        response = requests.get(url)
        # RSSはXML形式なのでxmlパーサーを使います
        soup = BeautifulSoup(response.content, features="xml")
        
        # ニュースのアイテムを取得
        items = soup.find_all("item")
        
        today = datetime.datetime.now().strftime("%m月%d日")
        text = f"おはようございます。{today}の注目ニュースです。\n\n"
        
        # 上位5件を取得
        count = 0
        for item in items:
            if count >= 5:
                break
            title = item.title.text
            text += f"{count+1}: {title}\n"
            count += 1
            
        text += "\n以上です。今日も一日頑張りましょう！"
        return text

    except Exception as e:
        return f"ニュース取得エラー: {e}"

if __name__ == "__main__":
    print(create_content())
