# 2024/5/17 10:56
from playwright.sync_api import sync_playwright


def sync():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=['--disable-blink-features=AutomationControlled'])
        page = browser.new_page()
        page.goto('https://weibo.com')

        page.pause()
        # 手动登录
        # 就是卡在登录账号的那一步上了，人家还暗示了好几次，你没get到，只能是说缘分不够足

        count = 0

        # 模拟下滑
        for i in range(20):
            all_ele = page.query_selector_all('//div[@class="detail_wbtext_4CRf9"]')
            for e in all_ele:
                # expand_ele = e.query_selector('//span[@class="expand"]')
                # if expand_ele:
                #     print('need click expand!')
                #     # 等待控件加载
                #     expand_ele.click()
                print(count, e.text_content())
                count += 1

            # 页面向下滚动到i*1000
            page.evaluate(f'window.scrollTo(0, {i * 2000})')
            page.wait_for_load_state('networkidle')

        browser.close()


if __name__ == '__main__':
    sync()
