import typer
from .core import run

app = typer.Typer()


@app.command()
def cli(url: str) -> None:
    """
    The URL of the video to download
    """
    run(url)


if __name__ == "__main__":
    app()