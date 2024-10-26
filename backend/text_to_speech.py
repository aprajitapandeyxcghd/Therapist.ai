from gtts import gTTS
import os

def generate_voice_response(text, avatar):
    tts = gTTS(text=text, lang='en')
    audio_file = f"static/{avatar}_response.mp3"
    tts.save(audio_file)
    return audio_file
