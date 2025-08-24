import bs4
import requests

getPriceFromAmazon(amazonURL):
    res = requests.get(amazonURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.select('#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole)')
    print(elems)
    print(elems[0])
    print(elems[0].text)
    print(elems[0].text.strip())
    return elems[0].text.strip()

price = getPriceFromAmazon('https://www.amazon.in/Lenovo-IdeaPad-WUXGA-OLED-400Nits-83DA0049IN/dp/B0CSPG1TJZ/ref=sr_1_2_sspa?dib=eyJ2IjoiMSJ9.MPce8Qww_PLm1vjSYITkhRcpkBhQzvwW4oN1ZZSjivzaccfRI6g6rjXtskOAMmfyW4BfUhG3WoqLnRZ-85eZSflGWBE_B1vKQqx0PnvE-8KMKQcETEaI_teWj4J3u6fuxnlVei72BWkjLq4KwbEdTciyqCu_CJYX9JqUwu66srqoX7cCeyRt9DGlA6ov0f7MMVTNb1lvegFcdXKvnGhPV35FJ1roje5W_yxGC0FDuJg.EGVxfITl9hCsljYBhFcGrHbI2FdnCO_dZYTakoMbXSY&dib_tag=se&keywords=asus+zephyrus+g14&nsdOptOutParam=true&qid=1736771731&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1')
print('The price is ' + price)

