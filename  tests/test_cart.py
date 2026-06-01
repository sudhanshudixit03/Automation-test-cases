import time
def login(page):

    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name","standard_user")

    page.fill("#password","secret_sauce")

    page.click("#login-button")

        #add to cart single product
def test_add_single_product(page):

    login(page)

    page.click("#add-to-cart-sauce-labs-backpack")

    badge = page.locator(".shopping_cart_badge").inner_text()

    assert badge == "1"

    page.click(".shopping_cart_link")

    assert page.locator(".inventory_item_name").is_visible()
    time.sleep(8)
        #   #add to cart multiple product

def test_add_multiple_products(page):

    login(page)

    page.click("#add-to-cart-sauce-labs-backpack")

    page.click("#add-to-cart-sauce-labs-bike-light")

    page.click("#add-to-cart-sauce-labs-bolt-t-shirt")

    badge = page.locator(".shopping_cart_badge").inner_text()

    assert badge == "3"
    time.sleep(8)

    #Remove product from cart
def test_remove_product(page):

    login(page)

    page.click("#add-to-cart-sauce-labs-backpack")

    page.click(".shopping_cart_link")

    page.click("#remove-sauce-labs-backpack")

    assert page.locator(".cart_item").count() == 0
    time.sleep(8)
#sort prices high to low
def test_sort_low_to_high(page):

    login(page)

    page.select_option(".product_sort_container","lohi")

    prices = page.locator(".inventory_item_price").all_inner_texts()

    numeric_prices = []

    for price in prices:
        numeric_prices.append(float(price.replace("$","")))

    assert numeric_prices == sorted(numeric_prices)
    time.sleep(8)