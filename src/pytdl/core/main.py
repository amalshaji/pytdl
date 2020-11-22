import json
import requests
from yaspin import yaspin
import urllib.parse as urlparse
from colorama import init, Fore

# from pytdl import download_file
# from pytdl import generate_options

from .download import download_file
from .select import generate_options

init(autoreset=True)

endpoint = (
    lambda id: f"https://www.youtube.com/get_video_info?video_id={id}&el=embedded&ps=default"
)


def run(url: str):
    """
    Assuming all the valid urls of type
    https://www.youtube.com/watch?v=-hsSAdIQufM,
    get the ID by replacing the constant text with ""
    """
    with yaspin(text="Getting Video information", color="cyan") as sp:
        if not url.startswith("https://www.youtube.com/watch?v="):
            sp.write(f"{Fore.RED}[Error] Enter a valid YouTube URL")
            return
        video_id = url.replace("https://www.youtube.com/watch?v=", "")
        sp.write(f"✔️ Video ID: {video_id}")

        sp.text = "Getting Video Metadata"
        x = requests.get(endpoint(video_id))
        sp.write("✔️ Received Video Metadata")

        sp.text = "Decoding Video Metadata"
        x = x.content.decode("utf-8")
        d = urlparse.parse_qs(x).get("player_response")
        d = json.loads(d[0])

        video_title = d["microformat"]["playerMicroformatRenderer"]["title"][
            "simpleText"
        ]
        sp.write(f"✔️ Video Title: {video_title}")

        sp.text = "Getting Video formats"
        f1 = d["streamingData"]["adaptiveFormats"]
        f2 = d["streamingData"]["formats"]

        formats = {}

        for i in [f1, f2]:
            for f in i:
                quality = f.get("quality")
                url = f.get("url")
                size = int(f.get("contentLength", 0)) / 1024 / 1024
                tt = f.get("mimeType").split(";")[0].split("/")
                type = tt[0]
                format = tt[1]

                name = f"{quality:^6} - {type:^5} - {format:^5} - {round(size)}MB"
                formats[name] = url

        sp.ok()

        answer = generate_options(formats).get("Choose download format")
        file_format = answer.split("-")[-2]
        filename = f"{video_title.lower().replace(' ', '_')}.{file_format.strip()}"

        download_file(formats[answer], filename)

        sp.write(f"✔️ Download Complete, Filename: {filename}")