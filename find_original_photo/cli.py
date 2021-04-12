"""Console script for find_original_photo."""
import sys
import click


@click.group()
def main(args=None):
    """Console script for find_original_photo."""
    click.echo("Replace this message by putting your code into "
               "find_original_photo.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0

@main.command()
def scan(input):
    pass



if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
