import typer
from src.pytdl.pytdl import run

app = typer.Typer()


@app.command()
def url(url: str):
    """
    The URL of the video to download
    """
    run(url)


if __name__ == "__main__":
    app()