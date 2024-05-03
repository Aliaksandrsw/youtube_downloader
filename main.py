from pytube import YouTube
import os


def download_video():
    video_url = input("Введите URL видео: ")
    yt = YouTube(video_url)

    print(f"Название видео: {yt.title}")
    print(f"Продолжительность: {yt.length} секунд")

    streams = yt.streams
    video_stream = streams.filter(progressive=True).get_highest_resolution()

    default_path = os.path.join(os.path.expanduser("~"), "Downloads")
    print(f"Папка для загрузки по умолчанию: {default_path}")
    print("Нажмите Enter для использования этой папки или введите путь к другой папке:")

    folder_path = input() or default_path

    print(f"Загрузка видео: {yt.title}")
    video_stream.download(folder_path)
    print("Загрузка завершена!")


if __name__ == "__main__":
    download_video()
