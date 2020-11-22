import requests
from tqdm import tqdm


def download_file(url, filename):
    """
    Helper method handling downloading large files from `url` to `filename`. Returns a pointer to `filename`.
    """
    chunkSize = 1024
    r = requests.get(url, stream=True)
    with open(filename, "wb") as f:
        pbar = tqdm(
            desc=filename,
            unit="B",
            total=int(r.headers["Content-Length"]),
            ncols=100,
            unit_scale=True,
            unit_divisor=1024,
        )
        for chunk in r.iter_content(chunk_size=chunkSize):
            if chunk:  # filter out keep-alive new chunks
                pbar.update(len(chunk))
                f.write(chunk)