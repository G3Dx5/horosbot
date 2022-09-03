#!/usr/bin/env python3

''' Call out to horoscope API and send via SMS to nominated recipient

Step one calls out to the horoscope API and returns the raw json data. A header
is added. The length of the message is calculated and divided into
segements that can be sent as individual messages given the 160 SMS character
limit. Sleep function is used as network slowness can make messages out of
order due to size precendence. Imports sendText from sm modulefor handling
actual sending of the message. Message is sent to the user from the sender
defined in the imported sm variable.
'''

import requests
from sendMessage import sendText
import sys
from time import sleep


def get_horoscope() -> None:
    """ Setup variables, get message from API via json and divide into
    deliverable amounts.

    ** url string can be be modified from "today" to "week" and any starsign
    added as final http element which determines the json content returned.

    """

    try:
        url = 'http://horoscope-api.herokuapp.com/horoscope/today/virgo'
        raw_horoscope = requests.get(url, headers={"Accept": "application/json"}).json()
    except requests.exceptions.HTTPError as connection_error:
        print("Exiting: ", connection_error)
        sys.exit(1)


    sms_limit = 158
    heading = "Your horoscope: "
    horoscope_text = raw_horoscope['horoscope']
    horoscope = heading + horoscope_text
    print(horoscope)
    len_horoscope = len(horoscope)
    number_of_sms_required = len_horoscope / sms_limit
    number_of_sms_required = float(number_of_sms_required)
    print(number_of_sms_required)

    if number_of_sms_required < 1.0:
        first_segment = [horoscope[i: i + sms_limit] for i in range(0, len(horoscope), sms_limit)]
        sendText(first_segment)
        sleep(1.5)

    elif number_of_sms_required > 1.0 and number_of_sms_required < 2.0:
        first_segment, second_segment = [horoscope[i: i + sms_limit] for i in range(0, len(horoscope), sms_limit)]
        sendText(first_segment)
        sleep(1.5)
        sendText(second_segment)

    elif number_of_sms_required > 2.0 and number_of_sms_required < 3.0:
        first_segment, second_segment, third_segment = [horoscope[i: i + sms_limit]for i in range(0, len(horoscope), sms_limit)]
        sendText(first_segment)
        sleep(1.5)
        sendText(second_segment)
        sleep(1.5)
        sendText(third_segment)

    elif number_of_sms_required > 3.0 and number_of_sms_required < 4.0:
        first_segment, second_segment, third_segment, fourth_segment = [horoscope[i: i + sms_limit] for i in range(0, len(horoscope), sms_limit)]
        sendText(first_segment)
        sleep(1.5)
        sendText(second_segment)
        sleep(1.5)
        sendText(third_segment)
        sleep(1.5)
        sendText(fourth_segment)

    elif number_of_sms_required > 4.0 and number_of_sms_required < 5.0:
        first_segment, second_segment, third_segment, fourth_segment, fifth_segment = [horoscope[i: i + sms_limit]for i in range(0, len(horoscope), sms_limit)]
        sendText(first_segment)
        sleep(1.5)
        sendText(second_segment)
        sleep(1.5)
        sendText(third_segment)
        sleep(1.5)
        sendText(fourth_segment)
        sleep(1.5)
        sendText(fifth_segment)

    elif number_of_sms_required > 5.0 and number_of_sms_required < 6.0:
        first_segment, second_segment, third_segment, fourth_segment, fifth_segment, sixth_segment = [horoscope[i: i + sms_limit]for i in range(0, len(horoscope), sms_limit)]
        sendText(first_segment)
        sleep(1.5)
        sendText(second_segment)
        sleep(1.5)
        sendText(third_segment)
        sleep(1.5)
        sendText(fourth_segment)
        sleep(1.5)
        sendText(fifth_segment)
        sleep(1.5)
        sendText(sixth_segment)

    else:
        print("Unable to print")


get_horoscope()
