from playwright.sync_api import Page


# Test Case 3 - Add Single Product
def test_add_single_product(page: Page):
    page.click("#add-to-cart-sauce-labs-backpack")

    # open cart
    page.click(".shopping_cart_link")                   # Dot(.) represents class selector in CSS.
                                                         # shopping_cart_link is class name.
    # validation
    assert page.locator("#shopping_cart_container").inner_text() == "1"


# Test Case 4 - Add Multiple Products
def test_add_multiple_products(page: Page):

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#add-to-cart-sauce-labs-bike-light")
    page.click("#add-to-cart-sauce-labs-bolt-t-shirt")

    # validation
    assert page.locator("#shopping_cart_container").inner_text() == "3"


# Test Case 5 - Remove Product
def test_remove_product(page: Page):

    page.click("#add-to-cart-sauce-labs-backpack")

    page.click(".shopping_cart_link")

    page.click("#remove-sauce-labs-backpack")

    assert page.locator(".cart_item").count() == 0


# Test Case 6 - Sort Low To High
def test_sort_low_to_high(page: Page):

    page.select_option(".product_sort_container", "lohi")

    # Capture product prices
    prices = page.locator(".inventory_item_price").all_inner_texts()     # all_inner_texts() captures visible text from
                                                                         # all matched elements and stores them into list format.
    actual_prices = [
        float(price.replace("$", ""))            # Remove dollar symbol and convert string to float  output eg = 7.99
        for price in prices ]                            # FOR Loop iterates through each product-price one by one.

    # Validation
    assert actual_prices == sorted(actual_prices), "Price sorting failed"

    # Take screenshot
    page.screenshot(path="Screenshots/product_sorting.png")

