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


def main():
    assert format_duration(0) == "now"
    assert format_duration(1) == "1 second"
    assert format_duration(62) == "1 minute and 2 seconds"
    assert format_duration(120) == "2 minutes"
    assert format_duration(3600) == "1 hour"
    assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"
    assert format_duration(15731080) == "182 days, 1 hour, 44 minutes and 40 seconds"
    assert format_duration(132030240) == "4 years, 68 days, 3 hours and 4 minutes"
    assert format_duration(205851834) == "6 years, 192 days, 13 hours, 3 minutes and 54 seconds"
    assert format_duration(253374061) == "8 years, 12 days, 13 hours, 41 minutes and 1 second"
    assert format_duration(242062374) == "7 years, 246 days, 15 hours, 32 minutes and 54 seconds"
    assert format_duration(101956166) == "3 years, 85 days, 1 hour, 9 minutes and 26 seconds"
    assert format_duration(33243586) == "1 year, 19 days, 18 hours, 19 minutes and 46 seconds"


if __name__ == '__main__':
    main()

