#!/usr/bin/env python3
import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import time
import sys

os.system('clear')

b = """
yt-tr ns ript
    X  .
   X t .
    .  .
    .  .
    .  .
    .  .

yt-transcript

Youtube Transcript
"""
print(b)

a = input("Masukan Youtube ID : ")

transcript = YouTubeTranscriptApi.get_transcript(a)

animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")

formatter = JSONFormatter()

json_formatted = JSONFormatter().format_transcript(transcript, indent=2)

with open('ts.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)
print("~ Sukses ~")
print()
print("\033[36mCek File ts.json")
print()
print("\033[37m~ Keluar ~")
print()
