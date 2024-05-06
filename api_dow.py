from googleapiclient.discovery import build


API_KEY = 'Ваш API'


def download_video(video_id):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()
    video_title = response['items'][0]['snippet']['title']

    request = youtube.videos().list(
        part="contentDetails",
        id=video_id
    )
    response = request.execute()
    video_url = "https://www.youtube.com/watch?v=" + video_id
    print(f"Загрузка видео: {video_title} ({video_url})")


if __name__ == "__main__":
    video_id = "VIDEO_ID"
    download_video(video_id)
