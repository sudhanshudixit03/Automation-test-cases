
#Test Case 7  -Checkout with product in cart
def test_checkout(page):
    # ADD TO CART
    page.click("#add-to-cart-sauce-labs-backpack")
    # OPEN CART
    page.click(".shopping_cart_link")

    # Click checkout button
    page.click("#checkout")

    # enter details
    page.fill("#first-name", "SUDHANSHU")
    page.fill("#last-name", "DIXIT")
    page.fill("#postal-code", "209801")

    # click continue
    page.click("#continue")

    # Finish
    page.click("#finish")

    # validation
    assert page.locator(".complete-header").inner_text() == "Thank you for your order!"


#Test Case 8 -Checkout empty cart
def test_empty_cart_checkout(page):

    page.click(".shopping_cart_link")

    page.click("#checkout")

    page.fill("#first-name","Sudhanshu")
    page.fill("#last-name","Dixit")
    page.fill("#postal-code","226001")

    page.click("#continue")

    assert page.locator(".title").inner_text() == "Checkout: Overview"


    # Screenshot
    page.screenshot(path="screenshots/empty_cart_checkout.png")
