import argparse


def getAllArguments() -> object:
    """
    Difinition of the commands in the CLIs Tools

    Arguments
    ---------
    - URLs: str
        - set the site URL Scraping the scoped imgs
    - ispdf: boolean
        - Convert all scraped imgs into a PDF file
    - pdfName: str
        - set the Converted PDF File's name

    """

    parser = argparse.ArgumentParser(
        description="Scraping scoped imgs in the site"
    )

    parser.add_argument(
        "url", help="set the site URL you want to sraping imgs"
    )
    parser.add_argument(
        "-p", "--pdf", help="covert all scraped images to a PDF file"
    )
    parser.add_argument("--arg3", required=False)
    parser.add_argument("-a", "--arg4", required=False)

    args = parser.parse_args()

    return args
