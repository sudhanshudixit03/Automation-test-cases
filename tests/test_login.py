#Test case 1 -Valid login
def test_valid_login(page):

    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name","standard_user")

    page.fill("#password","secret_sauce")

    page.click("#login-button")

    actual = page.locator(".title").inner_text()

    expected = "Products"

    assert actual == expected


#Test case 2 -Invalid login
def test_invalid_login(page):

    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name","wrong")

    page.fill("#password","wrong")

    page.click("#login-button")

    error = page.locator("[data-test='error']").inner_text()

    assert "Username and password do not match" in error