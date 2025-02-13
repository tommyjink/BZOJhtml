import pdfkit

path_wk = r'/usr/local/bin/wkhtmltopdf' 
config = pdfkit.configuration(wkhtmltopdf = path_wk)
url = 'https://darkbzoj.cc/problem/4799'   
pdfkit.from_url(url, r'pdfkit_test.pdf', configuration=config)  