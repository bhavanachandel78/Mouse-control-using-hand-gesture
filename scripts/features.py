from math import hypot

def extract_features(lmList):
    if len(lmList) == 0:
        return None

    # Thumb tip
    x1, y1 = lmList[4][1], lmList[4][2]

    # Index tip
    x2, y2 = lmList[8][1], lmList[8][2]

    # Middle tip
    x3, y3 = lmList[12][1], lmList[12][2]

    # Distance features
    dist_thumb_index = hypot(x2 - x1, y2 - y1)
    dist_index_middle = hypot(x3 - x2, y3 - y2)

    # Finger states
    index_up = 1 if lmList[8][2] < lmList[6][2] else 0
    middle_up = 1 if lmList[12][2] < lmList[10][2] else 0
    
    # Thumb direction
    thumb_up = 1 if lmList[4][2] < lmList[3][2] else 0
    thumb_down = 1 if lmList[4][2] > lmList[3][2] else 0

    return [dist_thumb_index, dist_index_middle, index_up, middle_up, thumb_up, thumb_down]