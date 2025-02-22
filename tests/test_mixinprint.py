def test_printmixin(capsys, product_samsung):
    print(product_samsung)
    captured = capsys.readouterr()
    assert (
        captured.out.strip().split("\n")[0]
        == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    )
