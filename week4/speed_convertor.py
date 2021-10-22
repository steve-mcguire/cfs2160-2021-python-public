
def kph_to_mph(kph):
    mph = kph / 1.6
    return mph

def mph_to_kph(mph):
    return mph * 1.6


print(kph_to_mph(160)) # should be 100
print(mph_to_kph(100)) # should be 160
