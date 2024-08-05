"""https://www.codewars.com/kata/52742f58faf5485cae000b9a"""


def format_duration(seconds):
    if seconds == 0:
        return "now"

    result = []

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    duration = {'year': years, 'day': days, 'hour': hours, 'minute': minutes, 'second': seconds}

    for element, amount in duration.items():
        if amount:
            element_string = f'{amount} {element}'
            if amount > 1:
                element_string += 's'
            result.append(element_string)

    if len(result) > 1:
        result.append(result.pop(-2) + ' and ' + result.pop())

    return ', '.join(result)
