import os
from pytube import YouTube
from pytube.cli import on_progress
from pytube.exceptions import RegexMatchError
from database import create_database, insert_video_metadata, insert_audio_metadata
from moviepy.editor import VideoFileClip

# Function to download a video from a YouTube URL
def download_video(video_url, video_format='mp4'):
    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
    except RegexMatchError:
        print("Invalid YouTube video URL. Skipping...")
        return

    stream = yt.streams.get_highest_resolution()

    if not stream:
        print("No streams found for the video.")
        return

    video_file_path = stream.download(output_path="video_downloads")
    print(f"Downloaded video: {stream.title}")

    if stream.includes_audio_track and stream.mime_type != f'video/{video_format}':
        converted_video_path = video_file_path.replace(".mp4", f".{video_format}")
        video_clip = VideoFileClip(video_file_path)
        codec = "libx264"
        parameters = ['-preset', 'fast', '-crf', '23']
        video_clip.write_videofile(converted_video_path, codec=codec, ffmpeg_params=parameters)
        video_clip.close()
        os.remove(video_file_path)
        print(f"Converted video to {video_format.upper()}: {converted_video_path}")
    else:
        converted_video_path = video_file_path

    video_metadata = (video_url, stream.title, yt.author, yt.length, stream.resolution, video_format)
    insert_video_metadata("link2playback.db", video_metadata)
    print("Video metadata saved to the database.")

# Function to download audio from a YouTube URL
def download_audio(video_url, audio_format='mp3', quality='high'):
    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
    except RegexMatchError:
        print("Invalid YouTube video URL. Skipping...")
        return

    if quality == 'high':
        stream = yt.streams.filter(only_audio=True, abr='128kbps').first()
        quality_tag = 'HQ'
    elif quality == 'low':
        stream = yt.streams.filter(only_audio=True).first()
        quality_tag = 'LQ'
    else:
        stream = yt.streams.filter(only_audio=True, abr='128kbps').first()
        quality_tag = 'HQ'

    audio_file = stream.download(output_path="audio_downloads")
    filename, extension = os.path.splitext(audio_file)
    renamed_audio_file = f"{filename}_{quality_tag}.{audio_format}"
    os.rename(audio_file, renamed_audio_file)
    print(f"Downloaded and converted audio to {quality_tag} {audio_format.upper()}: {renamed_audio_file}")

    audio_metadata = (video_url, yt.title, yt.author, yt.length, quality, audio_format, stream.abr)
    insert_audio_metadata("link2playback.db", audio_metadata)
    print("Audio metadata saved to the database.")

# Function for batch downloading
def batch_download(urls, download_type, format_choice, quality_choice=None):
    for url in urls:
        if download_type == 'a':
            download_audio(url, format_choice, quality_choice)
        elif download_type == 'v':
            download_video(url, format_choice)

# Main function to manage the downloading process
def main():
    create_database("link2playback.db")

    batch_download_choice = input("Do you want to input multiple links for batch download? (yes/no): ").lower()
    if batch_download_choice == 'yes':
        urls = input("Enter the YouTube video URLs separated by a comma: ").split(',')
        urls = [url.strip() for url in urls]

        download_type = input("Download as Audio or Video (A/V)?: ").lower()
        if download_type == 'a':
            format_choice = input("Select audio format (MP3/MP4/WAV/OGG): ").lower()
            quality_choice = input("Select audio quality (High/Low): ").lower()
            batch_download(urls, download_type, format_choice, quality_choice)
        elif download_type == 'v':
            format_choice = input("Select video format (MP4/MOV/AVI/WMV/WEBM/FLV): ").lower()
            batch_download(urls, download_type, format_choice)
        else:
            print("Invalid choice. Please enter 'A' for audio or 'V' for video.")
    else:
        # Single download logic
        video_url = input("Enter the YouTube video URL: ")
        try:
            YouTube(video_url)  # Validate the YouTube video URL
        except RegexMatchError:
            print("Invalid YouTube video URL. Please enter a valid URL.")
            return  # Return or you might use continue in a loop

        choice = input("Download as Audio or Video (A/V)?: ").lower()

        if choice == 'a':
            audio_format = input("Select audio format (MP3/MP4/WAV/OGG): ").lower()
            quality = input("Select audio quality (High/Low): ").lower()
            download_audio(video_url, audio_format, quality)
        elif choice == 'v':
            video_format = input("Select video format (MP4/MOV/AVI/WMV/WEBM/FLV): ").lower()
            download_video(video_url, video_format)
        else:
            print("Invalid choice. Please enter 'A' for audio or 'V' for video.")

if __name__ == "__main__":
    main()