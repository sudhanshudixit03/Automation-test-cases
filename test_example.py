from playwright.sync_api import Page



def test_playwrightBasics(page: Page):
    page.goto("https://www.rahulshettyacademy.com")