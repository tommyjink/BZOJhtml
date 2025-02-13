from urllib.request import urlopen
from html.parser import HTMLParser
import pandas as pd


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self,
                        tag,
                        attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href' and attr[1].startswith('/p/'):
                    self.links.append('https://hydro.ac' + attr[1])


def get_problem_links(page):
    url = f'https://hydro.ac/p?page={page}'
    try:
        with urlopen(url) as response:
            if response.getcode() == 200:
                html = response.read().decode('utf - 8')
                parser = LinkParser()
                parser.feed(html)
                print(f"哈哈哈哈哈哈哈，第 {page} 页题目链接获取成功")
                return parser.links
            else:
                print(f"呜呜呜呜呜！！！！请求页面 {page} 失败，{response.getcode()}")
    except Exception as e:
        print(f"呜呜呜呜呜！！！！请求页面 {page} 时发生错误: {e}")
    return []


def save_links_to_table():
    all_links = []
    for page in range(1, 708):
        page_links = get_problem_links(page)
        all_links.extend(page_links)
    df = pd.DataFrame({'题目链接': all_links})
    df.to_csv('题目链接表.csv', index=False)
    print('题目链接已成功保存到当前目录下的题目链接表.csv 文件中！')


if __name__ == '__main__':
    save_links_to_table()
