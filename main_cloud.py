import generator
from gtts import gTTS
import os

def main():
    # 1. ニュースのテキストを取得
    content = generator.create_content()
    
    # 2. GoogleのAIに読ませて、音声ファイル(news.mp3)にする
    print("音声を作成中...")
    tts = gTTS(text=content, lang='ja')
    tts.save("news.mp3")
    
    print("✅ news.mp3 を生成しました")

if __name__ == "__main__":
    main()
