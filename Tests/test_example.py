import re
from playwright.sync_api import Page, expect

BaseURL="https://tweakers.net/"

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_tweakers_Pricewatch_Iphone(page: Page):
    page.goto(BaseURL)

    page.get_by_role("button", name="Akkoord").click()
    page.get_by_role("link", name="Pricewatch").click()
    page.get_by_placeholder("Zoek een product").fill("iphone 16")
    page.get_by_placeholder("Zoek een product").press("Enter")

    # Controle aantal records
    #expect(page.locator(".pageIndex")).to_contain_text("1.324 uitvoeringen - Pagina 1 van 14")

 #   page.locator("iframe[title=\"https\\:\\/\\/webmodules\\.klaverblad\\.nl\\/Pakket\\?langid\\=43\\&sid\\=250461665\\&styleid\\=AfD46jKRL6bHvgBDEjKRL\\*\\*\\*\\*w\\=\\=_AM4h\\*cg\\=\"]").content_frame().get_by_text("Ik begrijp deze uitleg en vul").click()
 #   page.get_by_text("Ik begrijp deze uitleg en vul").click()