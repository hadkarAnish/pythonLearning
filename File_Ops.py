from urllib import request

# yahoo finance doesnt allow for download for web crawlers anymore
# tslaURL = 'https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1511792914&period2=1514384914&interval=1d&events=history&crumb=SgeNRIL3qiV'
SAMPLE_CSV = 'https://www.ibm.com/support/knowledgecenter/SVU13_7.2.1/com.ibm.ismsaas.doc/reference/LicenseImportSample.csv?view=kc'

def get_historical_prices(csv_URL):
    response = request.urlopen(csv_URL)
    csv = response.read()
    csv_string = str(csv)
    lines_in_download = csv_string.split("\\n")
    destination_URL = r'test.csv'
    file = open(destination_URL, "w")
    for line in lines_in_download:
        file.write(line + "\n")
    file.close()


get_historical_prices(SAMPLE_CSV)
