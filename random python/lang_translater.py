from moviepy.editor import VideoFileClip
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from pydub import AudioSegment
import os
import re

def extract_audio(video_file):
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile("temp.wav")

def speech_to_text(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""

def detect_language(text):
    translator = Translator()
    try:
        lang = translator.detect(text).lang
        return lang
    except:
        print("Language detection failed")
        return "en"

def translate_text(text, lang):
    translator = Translator()
    try:
        translation = translator.translate(text, dest='en')
        return translation.text
    except:
        print("Translation failed")
        return ""

def save_text(text, lang, file_format):
    if file_format == "txt":
        with open("transcript.txt", "w") as f:
            f.write(text)
        if lang != "en":
            with open("translation.txt", "w") as f:
                f.write(translate_text(text, lang))
    elif file_format == "srt":
        with open("transcript.srt", "w") as f:
            f.write("1\n00:00:00,000 --> 00:00:00,000\n" + text + "\n")
        if lang != "en":
            with open("translation.srt", "w") as f:
                f.write("1\n00:00:00,000 --> 00:00:00,000\n" + translate_text(text, lang) + "\n")
    elif file_format == "vtt":
        with open("transcript.vtt", "w") as f:
            f.write("WEBVTT\n\n00:00:00.000 --> 00:00:00.000\n" + text + "\n")
        if lang != "en":
            with open("translation.vtt", "w") as f:
                f.write("WEBVTT\n\n00:00:00.000 --> 00:00:00.000\n" + translate_text(text, lang) + "\n")
    else:
        print("Invalid file format")

def main():
    video_file = input("Enter the video file path: ")
    extract_audio(video_file)
    text = speech_to_text("temp.wav")
    lang = detect_language(text)
    print("Detected language:", LANGUAGES[lang])
    file_format = input("Enter the file format (txt, srt, vtt): ")
    save_text(text, lang, file_format)
    os.remove("temp.wav")

if __name__ == "__main__":
    main()