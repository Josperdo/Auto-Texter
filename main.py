import os
import config

def get_words(file_path):
    with open('rundown.txt', 'r') as f:
        text = f.readlines()[0]
        words = text.split()
    return words

# def get_lines(file_path):
#    with open('rundown.txt', 'r') as f:
#        text = f.readlines()
#    return text

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "_____"'.format(config.____))

if __name__ == '__main__': # enter phone number into string in format '1234567890'
    phone_number = ''
    words = get_words('rundown.txt')
    for word in words:
        send_message(config.YCUBED_PHONE)