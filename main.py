import os
import pdfkit
import pandas as pd


def generate_pdfs():
    path_wk = r'/usr/local/bin/wkhtmltopdf'
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    try:
        with open('题目链接表.csv', 'r', encoding='utf - 8') as file:
            for line in file:
                url = line.strip()
                file_name_part = url.split('/')[-1]
                pdf_name = f'pdf_{file_name_part}.pdf'
                # 检查文件是否已存在
                if os.path.exists(pdf_name):
                    print(f'跳过 {pdf_name}，文件已存在')
                    continue
                try:
                    pdfkit.from_url(url, pdf_name, configuration=config)
                    print(f'哈哈哈哈哈成功爬取 {pdf_name}')
                except Exception as e:
                    print(f'呜呜呜呜呜爬取失败 {pdf_name}: {e}')
    except FileNotFoundError:
        print('题目链接表.csv 文件未找到')


if __name__ == '__main__':
    generate_pdfs()