#Test case -9 Logout

def test_logout(page):

    # open side menu
    page.click("#react-burger-menu-btn")    #react-burger-menu-btn is element ID.Hamburger Menu(☰)
    page.click("#logout_sidebar_link")

    # Verify user is redirected to login page
    assert page.url == "https://www.saucedemo.com/", "User was not redirected to Login Page after logout"

    # Verify Login button is visible
    assert page.locator("#login-button").is_visible(), "Login button is not visible after logout"

    page.screenshot(path="screenshots/logout.png")



#Test case -10 Product Details

def test_product_details(page):

    # click on the product
    page.click("#item_4_title_link")  # "item_4_title_link" is HTML element ID of the product "Sauce Labs Backpack"

    # Capture product details
    product_title = page.locator(".inventory_details_name").inner_text()  # inventory_details_name is class name of the product title

        #We can also use text_content() for direct text retrieval.
        # product_title = text_content(".inventory_details_name")

        # Validation
    assert product_title == "Sauce Labs Backpack", "Product details do not match"    #if the product title is "Sauce Labs Backpack" then it will pass the test but if the product title is not "Sauce Labs Backpack" then it will fail the test


        # Screenshot
    page.screenshot(path="screenshots/product_details.png")