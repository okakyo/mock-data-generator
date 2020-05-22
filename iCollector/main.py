import argparse


def getAllArgs():
    return


def main():

    # TODO: 以下をController からコマンドを設定する場所から用意する
    parser = argparse.ArgumentParser(
        description="Scraping scoped imgs in the site"
    )  # 2. パーサを作る

    # 3. parser.add_argumentで受け取る引数を追加していく
    parser.add_argument(
        "url", help="set the site URL you want to sraping imgs"
    )  # 必須の引数を追加
    parser.add_argument(
        "-p", "--pdf", help="covert all scraped images to a PDF file"
    )
    parser.add_argument("--arg3", required=False)  # オプション引数（指定しなくても良い引数）を追加
    parser.add_argument(
        "-a", "--arg4", required=False
    )  # よく使う引数なら省略形があると使う時に便利

    args = parser.parse_args()  # 4. 引数を解析

    # TODO: 以下を、取得した引数をもとに、どのような動作をするかを定義する
    print("url=" + args.url)
    print("pdfnize=" + args.pdf)
    print(args)


if __name__ == "__main__":
    main()
