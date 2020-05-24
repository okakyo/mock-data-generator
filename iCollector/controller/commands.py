import argparse


def parseArguments() -> object:
    """
    parseArguments [summary]

    Args:
        - url
        - -p, --pdf
        - a
    Returns:
        object: [description]
    """

    parser = argparse.ArgumentParser(
        description="Scraping scoped imgs in the site"
    )

    parser.add_argument(
        "url", help="set the site URL you want to sraping imgs"
    )
    parser.add_argument(
        "-p",
        "--pdf",
        help="covert all scraped images to a PDF file",
        default=False,
    )
    parser.add_argument("--arg3", required=False)
    parser.add_argument("-a", "--arg4", required=False)

    args = parser.parse_args()

    return args
