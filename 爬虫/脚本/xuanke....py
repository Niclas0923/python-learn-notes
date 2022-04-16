import asyncio
import pyppeteer as pyp
import time


async def antiAntiCrawler(page):
    await page.setUserAgent('Mozill/5.0 (windows NT 6.1; \
        win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
            chrom/78.0.3904.70 Safari/537.36')
    await page.evaluateOnNewDocument(
        '() =>{ Object.defineProperties(navigator, \
            { webdriver:{ get: () => false } }) }')

async def getOjSourceCode(loginUrl):
    width,height = 1400,800
    userdataDir = "/Users/yanhui/Desktop"
    browser = await pyp.launch(headless = False,
                                args = [f'--window-size={width},{height}'])

    page = await browser.newPage()
    await antiAntiCrawler(page)
    await page.setViewport({'width':width,'height':height})
    await page.goto(loginUrl)

    # 登录
    element = await page.querySelector("#yhm")
    await element.type("2023040327")
    element = await page.querySelector("#mm")
    await element.type("mM11929800")
    element = await page.querySelector("#dl")
    await element.click()                       # 点击登录按钮

    await asyncio.sleep(1)
    page_list = await browser.pages()  # Get all pages
    page = page_list[-1]  # New page at the end

    # 等待标题出现，最多等30000ms
    await page.waitForSelector("body > div.container.padding-150 > div > div.col-md-3.col-sm-4 > div > h3 > span",timeout=30000)

    element = await page.querySelector("#searchBox > div > div.row.search-filter > div > div > div > div > input")
    await element.type("尔雅")

    time.sleep(4) 
    element = await page.querySelector("#searchBox > div > div.row.search-filter > div > div > div > div > input")
    await element.type("尔雅")

    element = await page.querySelector("#searchBox > div > div.row.condition-item > div:nth-child(13) > div > div > ul > li:nth-child(1) > a")
    await element.click()
    
    element = await page.querySelector("#nav_tab > li:nth-child(6) > a")
    await element.click()

    # 查询
    element = await page.querySelector("#searchBox > div > div.row.search-filter > div > div > div > div > span > button.btn.btn-primary.btn-sm")
    await element.click()

    time.sleep(10)
    await browser.close()
    
def main():
    url = "https://jwglxt1.qust.edu.cn/jwglxt/xtgl/login_slogin.html"
    asyncio.get_event_loop().run_until_complete(getOjSourceCode(url))

if __name__ == "__main__":
    main()