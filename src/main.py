import itertools
import src.sort as sort
import src.wait as wait


def main() -> None:
    main_loop()


def main_loop() -> None:
    for n in itertools.count():
        wait.wait(n)
        sort.simulate()


if __name__ == "__main__":
    main()
