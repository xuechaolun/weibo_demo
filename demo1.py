import concurrent.futures
import re
import threading
import time

import requests


def get_data(num, tot=0):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "client-version": "v2.45.20",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://weibo.com/",
        "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "server-version": "v2024.05.16.1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": "KO9dq-AeiktnPTiUO6Xdqju4"
    }
    cookies = {
        "XSRF-TOKEN": "KO9dq-AeiktnPTiUO6Xdqju4",
        "_s_tentry": "weibo.com",
        "appkey": "",
        "Apache": "8967215959824.426.1715927098065",
        "SINAGLOBAL": "8967215959824.426.1715927098065",
        "ULV": "1715927098069:1:1:1:8967215959824.426.1715927098065:",
        "WBtopGlobal_register_version": "2024051714",
        "SUB": "_2A25LQ3LxDeRhGeFH6VIZ8SzLwjuIHXVoIYo5rDV8PUNbmtANLWXFkW9Ne62GiTSZ9A9CJLpx6cfGqJny30Ax_Lhl",
        "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Ovw6YQodEh5FlvMPOrNSI5JpX5KzhUgL.FoM4eo5ReKzN1KM2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMN1Kz71h2ES0.N",
        "ALF": "02_1718521761",
        "WBPSESS": "Dt2hbAUaXfkVprjyrAZT_Kfiknc7B5rJmxOYKsJusafwBcsu5nGIZzZCrFUG1_9ANBwRrv1Sw-7b6ihdRRLwjtDOoIo8KEAg4UZUPeN8_5zvF26vw1zLJJe75GKsjzjXWqTUsfVmA5U4hzysIJuxgossKxMLQ34RoOAOL9_pzxZeQYOUfXPtQxD1QZIwdoRfFwVnfp9mT2LcZXRlthwgFA=="
    }
    url = "https://weibo.com/ajax/feed/unreadfriendstimeline"
    params = {
        "list_id": "100017920812797",
        "refresh": "4",
        "max_id": str(1715922959349985 - num * 15),
        "count": "15"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    for item in response.json()['statuses']:
        text = item['text']
        res = re.findall('<span class=\"expand\">展开</span>', text)
        if len(res) == 0:
            print(tot, item['text_raw'].replace('\n', ''))
        else:
            resp = requests.get(f"https://weibo.com/ajax/statuses/longtext?id={item['mblogid']}", headers=headers,
                                cookies=cookies)
            # print('mblogid:', item['mblogid'])
            print(tot, resp.json()['data']['longTextContent'].replace('\n', ''))
            resp.close()
        tot += 1
    print()
    time.sleep(0.5)
    response.close()
    return tot


if __name__ == '__main__':
    count = 0
    for n in range(10):
        count = get_data(n, count)


