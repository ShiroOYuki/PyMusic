import yt_dlp
import os
from pydub import AudioSegment
from pydub.utils import which

AudioSegment.converter = which("ffmpeg") 

# https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#embedding-examples

def download(url):
    opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
        'paths': {
            'home': './temp'
        },
        'outtmpl': {
            'default': '%(id)s.%(ext)s'
        }
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print("Title:", info.get("title"))
        filepath = ydl.prepare_filename(info, outtmpl=opts['outtmpl']['default'])
        abs_path = os.path.abspath(filepath)
        m4a_to_mp3(abs_path)
        
def m4a_to_mp3(input_file: str):
    audio = AudioSegment.from_file(input_file, format="m4a")
    
    output_file = input_file.split("\\")
    output_file[-2] = "download"
    output_file[-1] = output_file[-1][:-3] + "mp3"
    output_file = "\\".join(output_file)
    
    audio.export(output_file, format="mp3")
    print(f"[output] {output_file}")
    os.remove(input_file)

        
if __name__ == "__main__":
    # download("https://www.youtube.com/watch?v=t3kOeUsnocg")
    download(input("URL: "))