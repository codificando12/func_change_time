def change_date(day):
    months = {
        'Jan': 'January',
        'Feb': 'February',
        'Mar': 'March',
        'Apr': 'April',
        'May': 'May',
        'Jun': 'June',
        'Jul': 'July',
        'Aug': 'August',
        'Sep':'September',
        'Oct':'October',
        'Nov': 'November',
        'Dec':'December'
    }

    
    day = day.split(" ")
    new_day = [day[1], day[4]]
    new_day[0] = months[new_day[0]]

    return(" ".join(str(date) for date in new_day))

