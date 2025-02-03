from tiercut import tierCut

def getTier(mmr):
    tierCutResult = tierCut()
    demigodCut = tierCutResult[1]
    eternityCut = tierCutResult[0]
    if 0 <= mmr < 250:
        return "아이언4"
    elif 250 <= mmr < 500:
        return "아이언3"
    elif 500 <= mmr < 750:
        return "아이언2"
    elif 750 <= mmr < 1000:
        return "아이언1"
    elif 1000 <= mmr < 1250:
        return "브론즈4"
    elif 1250 <= mmr < 1500:
        return "브론즈3"
    elif 1500 <= mmr < 1750:
        return "브론즈2"
    elif 1750 <= mmr < 2000:
        return "브론즈1"
    elif 2000 <= mmr < 2250:
        return "실버4"
    elif 2250 <= mmr < 2500:
        return "실버3"
    elif 2500 <= mmr < 2750:
        return "실버2"
    elif 2750 <= mmr < 3000:
        return "실버1"
    elif 3000 <= mmr < 3250:
        return "골드4"
    elif 3250 <= mmr < 3500:
        return "골드3"
    elif 3500 <= mmr < 3750:
        return "골드2"
    elif 3750 <= mmr < 4000:
        return "골드1"
    elif 4000 <= mmr < 4250:
        return "플래티넘4"
    elif 4250 <= mmr < 4500:
        return "플래티넘3"
    elif 4500 <= mmr < 4750:
        return "플래티넘2"
    elif 4750 <= mmr < 5000:
        return "플래티넘1"
    elif 5000 <= mmr < 5250:
        return "다이아몬드4"
    elif 5250 <= mmr < 5500:
        return "다이아몬드3"
    elif 5500 <= mmr < 5750:
        return "다이아몬드2"
    elif 5750 <= mmr < 6000:
        return "다이아몬드1"
    elif 6000 <= mmr < demigodCut:
        return "미스릴"
    elif demigodCut <= mmr < eternityCut:
        return "데미갓"
    else:
        return "이터니티"

    
    
    
    