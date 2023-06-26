import os
import telebot
from pydub import AudioSegment
import speech_recognition
import config.env_config as env_cfg

token = env_cfg.token
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def say_hi(message):
    bot.send_message(message.chat.id, 'Привет, ' + message.chat.first_name)


def oga2wav(filename):
    new_filename = filename.replace('.oga', '.wav')
    audio = AudioSegment.from_file(filename)
    audio.export(new_filename, format='wav')
    return new_filename


def recognize_speech(oga_filename):
    wav_filename = oga2wav(oga_filename)
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.WavFile(wav_filename) as source:
        wav_audio = recognizer.record(source)

    text = recognizer.recognize_google(wav_audio, language='ru')

    if os.path.exists(oga_filename):
        os.remove(oga_filename)
    
    if os.path.exists(wav_filename):
        os.remove(wav_filename)
    
    return text

def download_file(bot, file_id):
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    filename = file_id + file_info.file_path
    filename = filename.replace('/', '_')

    with open(filename, 'wb') as file:
        file.write(downloaded_file)
    return filename

@bot.message_handler(content_types=['voice'])
def transcript(message):
    filename = download_file(bot, message.voice.file_id)
    text = recognize_speech(filename)
    bot.send_message(message.chat.id, text)

bot.polling()