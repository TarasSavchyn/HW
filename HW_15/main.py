from argparse import ArgumentParser


def args_parser() -> None:
    parser = ArgumentParser(description="Very good decoder.")
    parser.add_argument(
        "-f", help="input -f if you want read only first line", action="store_true"
    )  # зробив типу по простому, якщо є флажок то рахуємо тільки першу строку
    parser.add_argument("file_name", help="input file_name", type=str)
    args = parser.parse_args()

    with open(args.file_name) as file:
        if args.f:
            print(len(file.readline().split()))
        else:
            print(len(file.read().split()))


if __name__ == "__main__":
    args_parser()
