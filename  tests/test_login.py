def test_valid_login(page):

    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")

    page.fill("#password", "secret_sauce")

    page.click("#login-button")

    actual = page.locator(".title").inner_text()

    expected = "Products"

    assert actual == expected