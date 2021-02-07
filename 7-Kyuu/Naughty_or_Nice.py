# Santa is coming to town and he needs your help finding out who's been naughty or nice. You will be given an entire year of JSON data following this format:

# {
#     January: {
#         '1': 'Naughty','2': 'Naughty', ..., '31': 'Nice'
#     },
#     February: {
#         '1': 'Nice','2': 'Naughty', ..., '28': 'Nice'
#     },
#     ...
#     December: {
#         '1': 'Nice','2': 'Nice', ..., '31': 'Naughty'
#     }
# }
# Your function should return "Naughty!" or "Nice!" depending on the total number of occurrences in a given year (whichever one is greater). If both are equal, return "Nice!"

def naughty_or_nice(data):
    bad = 0
    good = 0
    for month in data.keys():
        for behavior in data[month].values():
            if behavior is "Naughty":
                bad += 1
            elif behavior is "Nice":
                good += 1
    if good >= bad:
        return "Nice!"
    else:
        return "Naughty!"
