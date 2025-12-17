import generator
from gtts import gTTS
import os
import json
import datetime
import uuid

def main():
    # 1. ニュース音声を作る
    print("音声を作成中...")
    content = generator.create_content()
    tts = gTTS(text=content, lang='ja')
    tts.save("news.mp3")
    
    # 2. 放送用データ(feed.json)を作る
    # あなたのGitHub URLに合わせて書き換えています
    base_url = "https://Sally0506-glitch.github.io/my-news-feed"
    
    feed_data = [
        {
            "uid": str(uuid.uuid4()),
            "updateDate": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.0Z"),
            "titleText": "今日のニュース",
            "mainText": "今日のニュースをお伝えします。",
            "streamUrl": f"{base_url}/news.mp3", # ここでMP3を指定！
            "redirectionUrl": base_url
        }
    ]
    
    with open("feed.json", "w", encoding="utf-8") as f:
        json.dump(feed_data, f, ensure_ascii=False)
        
    print("✅ news.mp3 と feed.json を生成しました")

if __name__ == "__main__":
    main()

