
def calculate_brightness(img):
    # Write your code here
    if not img: return -1
    if not len(img): return -1
    
    total = 0
    lengths = list(map(len, img))
    if len(set(lengths)) != 1: return -1

    for i in range(len(img)):
        if any(p < 0 or p > 255 for p in img[i]):
            return -1
        total += sum(img[i])
    
    return total / sum(lengths)