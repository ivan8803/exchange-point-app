from decimal import Decimal

def process_currency_req(req):
    """
    functions for processing currency data from an external server

    Parameters:
    req (class 'requests.models.Response'): Data received from external server

    Returns:
    currency (dict: country (str):exchange_rate (decimal)): returns a dictionary of country exchange rates
    """

    data = req.text.split("\n")
    currency = dict()

    for line in data[2:]:
        if (len(line) > 0):
            temp = line.split('|')
            try:
                amount = Decimal(temp[2])
                rate = Decimal(temp[4].replace(',', '.'))
                rate /= amount
            except (ValueError):
                raise Exception("An error occurred while reading the currency data")
                
            currency.setdefault(temp[3], rate)
    
    return currency