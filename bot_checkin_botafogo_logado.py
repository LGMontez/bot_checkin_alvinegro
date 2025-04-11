import os
import time
import requests
import snscrape.modules.twitter as sntwitter

# Variáveis de ambiente
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
USUARIO_TWITTER = os.getenv('USUARIO_TWITTER')
PALAVRAS_CHAVE = ['check-in', 'alvinegro']

import time
import requests
import snscrape.modules.twitter as sntwitter

# Armazena tweets já enviados
tweets_enviados = set()

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensagem
    }
    response = requests.post(url, data=payload)
    if response.ok:
        print("📤 Enviado para o Telegram com sucesso!")
    else:
        print("❌ Erro ao enviar para o Telegram:", response.text)

def verificar_tweets():
    print("🔍 Verificando novos tweets...")
    for tweet in sntwitter.TwitterUserScraper(USUARIO_TWITTER).get_items():
        if tweet.id in tweets_enviados:
            continue
        conteudo = tweet.content.lower()
        if all(palavra in conteudo for palavra in PALAVRAS_CHAVE):
            mensagem = f"✅ Check-in detectado!\n\nTweet: {tweet.content}\n\n🔗 https://twitter.com/{USUARIO_TWITTER}/status/{tweet.id}"
# Loop contínuo a cada 5 minutos
while True:
    try:
        verificar_tweets()
    except Exception as e:
        print("⚠️ Erro ao verificar tweets:", e)
    time.sleep(300)  # Espera 5 minutos
