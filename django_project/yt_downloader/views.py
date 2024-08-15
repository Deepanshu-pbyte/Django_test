from django.shortcuts import render
from django.http import HttpResponse
import yt_dlp
import os


def youtube(request):
    print(request.method)
    if request.method == "POST":
        video_url = request.POST.get("link")
        quality = request.POST.get("Quality")
        print("url = ", video_url)
        try:
            ydl_opts = {"format": quality, "outtmpl": output_path}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=True)
            print("Format:",ydl_opts["format"])
            print(f"Video Title: {info_dict['title']}")
        except Exception as e:
            print(f"Error: {e}")
    return render(request, "yindex.html")
