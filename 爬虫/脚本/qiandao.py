import asyncio
import pyppeteer as pyp
import time
import pyautogui as at

async def antiAntiCrawler(page):
    await page.setUserAgent('Mozill/5.0 (windows NT 6.1; \
        win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
            chrom/78.0.3904.70 Safari/537.36')
    await page.evaluateOnNewDocument(
        '() =>{ Object.defineProperties(navigator, \
            { webdriver:{ get: () => false } }) }')

async def getOjSourceCode(loginUrl):
    width,height = 400,800

    pyp.launcher.DEFAULT_ARGS.remove("--enable-automation")
    browser = await pyp.launch(headless = False,
                                userdataDir = "/Users/yanhui/Desktop",
                                args = [f'--window-size={width},{height}'])

    context = await browser.createIncognitoBrowserContext();
    # 新建标签页
    page = await context.newPage();

    #page = await browser.newPage()
    await antiAntiCrawler(page)
    await page.setViewport({'width':width,'height':height})
    await page.goto(loginUrl)

    # 登录
    time.sleep(1)
    element = await page.querySelector("#username")
    await element.type("2023040327")
    time.sleep(1.3)
    element = await page.querySelector("#ppassword")
    await element.type("mM11929800")
    time.sleep(1.2)
    element = await page.querySelector("#dl")
    await element.click()                       # 点击登录按钮

    # await asyncio.sleep(1)
    # page_list = await browser.pages()  # Get all pages
    # page = page_list[-1]  # New page at the end

    # 等待标题出现，最多等30000ms
    # await page.waitForSelector("#xsjbxx > div.title > p",timeout=30000)
    time.sleep(4)

    # 获取位置
    element = await page.querySelector("#dkxx > div.table-cell > div.block.block-oneline > p > a")
    await element.click()
    time.sleep(40)
    print("1")
    # at.scroll(-15)

    time.sleep(3)

    # 点击提交
    element = await page.querySelector("#dataFormSave")
    await element.click()

    time.sleep(4)
    print("2")
    await browser.close()
    
def main():
    url = "https://bpm.qust.edu.cn/bpmx/platform/form/bpmDataTemplate/editData_xsjkdk.ht?type=WeiXinGzhClient&ticket=ST-2228-c2Uo0nOGFAvcoql1zsJq-zfsoft.com"
    asyncio.get_event_loop().run_until_complete(getOjSourceCode(url))

if __name__ == "__main__":
    main()