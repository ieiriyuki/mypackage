from foo import bar


def test_addone():
    print("start test_addone")
    assert bar.add_one(4) == 5
