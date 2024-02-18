
MAX_ITER = 10

def check_iter(data:dict) -> bool:
    if data['iter'] < 10:
        data['iter'] += 1
        return True
    else:
        data['iter'] += 1
        return False
    
