Python script set designed to call out to online horoscope API.  Script grabs horoscope text then divides returned text into 158 character section.  Each section is then sent in order to a user by utilising a globalSMS user / API account.

The sendMessage.py module allows the user to change between horoscope modes (daily vs weekly) and the starsign (leo, virgo etc.) and is imported by horos.py. sendMessage also allows the alias of the sender to be set.  For example the recipient can recieve the SMS messages from "my great horoscope guru", if that is set in the sendMessage module.   

Example usage: python3 horos.py
   
GaDayas November 2020.
