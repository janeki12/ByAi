import sys
import google.generativeai as genai

# API anahtarını ayarla buraya
api_key:str = 'buraya api koy' 
genai.configure(api_key=api_key)

generation_config = {
    'temperature': 0.9,
    'top_p': 1,
    'top_k': 1,
    'max_output_tokens': 1024,
}

model = genai.GenerativeModel(model_name='models/gemini-1.5-flash',
                             generation_config=generation_config,
                             safety_settings={'HARASSMENT': 'block_none'})

def start_new_conversation():
    """Yeni bir konuşma başlatır ve geçmişi temizler."""
    global convo
    convo = model.start_chat(history=[])

start_new_conversation()

def generate_post_description():
    message = "Instagram için otomatik bir gönderi açıklaması yaz ve altına bolca hashtag ekle. ornek. anin tadini cikart, bugun harika bir gun, ve benzeri seyler olsun. hashtagleri olustur. sadece bir gonderi icin ver."
    convo.send_message(message)
    response = convo.last.text
    return response.strip()
  
def generate_comment():
    message = "Instagram için bir yorum oluştur."
    convo.send_message(message)
    response = convo.last.text
    return response.strip()

def generate_hashtags():
    message = "Instagram için bolca hashtag oluştur."
    convo.send_message(message)
    response = convo.last.text
    return response.strip()

def main():
    if len(sys.argv) < 2:
        print("Lütfen bir komut verin: 'gonderi', 'yorum' veya 'hashtag'.")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "gonderi":
        print(generate_post_description())
    elif command == "yorum":
        print(generate_comment())
    elif command == "hashtag":
        print(generate_hashtags())
    else:
        print("Geçersiz komut. 'gonderi', 'yorum' veya 'hashtag' komutlarını kullanın.")

if __name__ == "__main__":
    main()
