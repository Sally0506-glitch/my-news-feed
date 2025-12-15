import generator
import json
import datetime
import os

def main():
    # 1. ニュースのテキストを取得（いつものやつ）
    content = generator.create_content()
    
    # 2. 現在時刻（UTC形式が必要）
    now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.0Z')
    
    # 3. Alexa用のデータ形式(JSON)に整える
    feed_data = [
        {
            "uid": f"news-{now}",
            "updateDate": now,
            "titleText": "今日の注目ニュース",
            "mainText": content, # ここをAlexaが読み上げる
            "redirectionUrl": "https://news.yahoo.co.jp/"
        }
    ]
    
    # 4. ファイルとして保存 (feed.json)
    # これをGitHub Pagesで公開する
    with open("feed.json", "w", encoding="utf-8") as f:
        json.dump(feed_data, f, ensure_ascii=False, indent=4)
        
    print("✅ feed.json を生成しました")

if __name__ == "__main__":
    main()
