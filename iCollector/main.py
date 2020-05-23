import argparse
from controller import commands


def main():

    # parsedArgs: validate and parse arguments.
    parsedArgs = commands.parseArguments()
    # 取得したパースをもとに。何を実行するかを管理する
    print(parsedArgs.url)
    pass


if __name__ == "__main__":
    main()
