from datetime import datetime

def get_days_from_today(date_str):
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d")
        current_date = datetime.now()
        days_difference = (current_date - input_date).days
        
        return days_difference
    except ValueError:
        return 'Wrong date fromat, please use format YYYY-mm-dd'

input_date_str = "2024-02-20"
days = get_days_from_today(input_date_str)
print(f"Days from {input_date_str} to today: {days}")


import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    if min < 1 or max > 1000 or quantity > (max - min):
        return []
    
    result = set()

    while len(result) < quantity:
        result.add(random.randint(min, max))
    
    return sorted(result)

lottery_nimbers = get_numbers_ticket(min = 2, max = 40, quantity=7)
print(f'lottery numbers: {lottery_nimbers}')


