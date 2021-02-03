import argparse

from sample_lib import (
    Hoge,
    Fuga
)
from sample_lib.submodule import Piyo


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', choices=['hoge', 'fuga', 'piyo'], default='hoge')
    args = parser.parse_args()

    if args.name == 'hoge':
        x = Hoge()
    elif args.name == 'fuga':
        x = Fuga()
    elif args.name == 'piyo':
        x = Piyo()

    print(x())


if __name__ == '__main__':
    main()
