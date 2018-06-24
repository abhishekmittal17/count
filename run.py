import sys

def main(*args, **kwargs):
    message = sys.argv[1]

    print('Possible count for ' + message)
    result = possible_decodes(message)
    print(result)


def possible_decodes(message):
    message_length = len(message);

    # Empty message and message with 1 length considered as one count
    if message_length == 0 or message_length == 1:
        return 1

    # As we knows highest number is 26 i.e. z, so we need to process numbers in combination of 1 and 2 digits.
    if int(message[:2]) > 9 and int(message[:2]) < 27:
        return possible_decodes(message[1:]) + possible_decodes(message[2:])
    else:
        return possible_decodes(message[1:])


if __name__ == "__main__":
    main()
