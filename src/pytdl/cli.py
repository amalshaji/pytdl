import typer
from .core import run

app = typer.Typer()


@app.command()
def url(url: str):
    """
    The URL of the video to download
    """
    run(url)


def run():
    app()


if __name__ == "__main__":
    run()