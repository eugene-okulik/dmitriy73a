import json
import re

from playwright.sync_api import Page, Route, expect


def test_task(page: Page):
    def changing_response(route: Route):
        response = route.fetch()
        body = response.json()

        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = "яблокофон 17 про"

        body = json.dumps(body)
        route.fulfill(response=response, body=body)

    page.route(re.compile("api/digital-mat"), changing_response)
    page.goto("https://www.apple.com/shop/buy-iphone")
    iphone = page.locator(".rf-hcard-content-title").first
    iphone.click()
    title = page.locator("#rf-digitalmat-overlay-label-0").first
    expect(title).to_have_text("яблокофон 17 про")
