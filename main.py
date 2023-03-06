import PySimpleGUI as sg
from pytube import YouTube


def main_window() -> sg.PySimpleGUI.Window:
    layout = [
        [sg.T("YouTube link:"), sg.I(size=50, key="--LINK--")],
        [sg.B("Fetch")],
        [sg.T(key="--TITLE--")],
        [sg.Listbox([], size=(90, 8), key="--DL--")],
        [sg.B("Download"), sg.B("Exit")],
        [sg.T("Version 0.0.1 - 2023-03-06 - https://github.com/paluigi/youtube_downloader")]
    ]
    window = sg.Window("YouTube Downloader", layout)

    return window


window = main_window()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "Fetch":
        try:
            yt = YouTube(values.get("--LINK--", "INVALID"))
            window["--TITLE--"].update(yt.title)
            window["--DL--"].update(yt.streams)
        except:
            sg.Popup("ERROR!", "Invalid link")
    if event == "Download":
        try:
            itag = values.get("--DL--")[0].itag
            folder = sg.PopupGetFolder("Where to save?")
            stream = yt.streams.get_by_itag(itag)
            stream.download(output_path=folder)
        except:
            sg.Popup("ERROR!", "Insert a link and select the version to download")

window.close()