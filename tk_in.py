import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube


def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)


def download_video():
    url = url_entry.get()
    folder_path = folder_entry.get()

    try:
        yt = YouTube(url)
        streams = yt.streams
        video_stream = streams.filter(progressive=True).get_highest_resolution()

        messagebox.showinfo("Загрузка", f"Загрузка видео: {yt.title}")
        video_stream.download(folder_path)
        messagebox.showinfo("Завершено", "Загрузка завершена!")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))


root = tk.Tk()
root.title("Загрузчик видео с YouTube")

url_label = tk.Label(root, text="URL видео:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

folder_label = tk.Label(root, text="Папка для загрузки:")
folder_label.pack()

folder_entry = tk.Entry(root, width=30)
folder_entry.pack()

browse_button = tk.Button(root, text="Обзор", command=browse_folder)
browse_button.pack(side=tk.LEFT, padx=5)

download_button = tk.Button(root, text="Загрузить", command=download_video)
download_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
