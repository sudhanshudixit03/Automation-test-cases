def login(page):

    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name","standard_user")

    page.fill("#password","secret_sauce")

    page.click("#login-button")

#checkout with single product
def test_checkout(page):

    login(page)

    page.click("#add-to-cart-sauce-labs-backpack")

    page.click(".shopping_cart_link")

    page.click("#checkout")

    page.fill("#first-name","Sudhanshu")

    page.fill("#last-name","Dixit")

    page.fill("#postal-code","226001")

    page.click("#continue")

    page.click("#finish")

    actual = page.locator(".complete-header").inner_text()

    assert actual == "Thank you for your order!"

#checkout empty cart
def test_empty_cart_checkout(page):

    login(page)

    page.click(".shopping_cart_link")

    page.click("#checkout")

    page.fill("#first-name","Sudhanshu")

    page.fill("#last-name","Dixit")

    page.fill("#postal-code","226001")

    page.click("#continue")

    assert page.locator(".title").is_visible()