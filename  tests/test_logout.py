def login(page):

    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name","standard_user")

    page.fill("#password","secret_sauce")

    page.click("#login-button")

#logout

def test_logout(page):

    login(page)

    page.click("#react-burger-menu-btn")

    page.click("#logout_sidebar_link")

    assert page.locator("#login-button").is_visible()


#For product details

def test_product_details(page):

    login(page)

    product_name = page.locator(".inventory_item_name").first.inner_text()

    page.locator(".inventory_item_name").first.click()

    detail_name = page.locator(".inventory_details_name").inner_text()

    assert product_name == detail_name