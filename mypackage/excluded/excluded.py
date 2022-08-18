from package1.foo.foo import foo


def main():
    # in mypackage directory
    # run `poetry run python excluded/excluded.py`
    print("this also work", foo())


if __name__ == "__main__":
    main()
