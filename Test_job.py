import requests

AFFISE_URL = 'http://api.cpanomer1.affise.com/3.0/'
OFFERS_URL = '{}partner/offers'.format(AFFISE_URL)
CONVERSION_URL = '{}stats/conversions'.format(AFFISE_URL)
TOKEN = 'e60a98867d363b0d43b9e7c58ec498ed'


def main():
    offer_response = requests.get(OFFERS_URL, headers={'API-Key': TOKEN})
    offer_data = offer_response.json()
    offer = offer_data['offers'][0]
    countries = offer['countries']
    print('Offer', offer['id'], 'data')
    print('Countries available for this offer: ', countries)

    conversion_response = requests.get(CONVERSION_URL, headers={'API-Key': TOKEN}, params={'status': ''})
    conversion_data = conversion_response.json()
    conversion = conversion_data['conversions'][0]
    if conversion['offer_id'] != offer['id']:
        return  # if conversion doesnt belong to the given offer

    print('Conversion location:', conversion['country_name'], conversion['city'])
    print('Possible Click ID:', conversion['cbid'])


if __name__ == '__main__':
    main()
