def convert_to_mph(kph: "Speed in kph") -> "MPH":
    return kph / 1.6


print(convert_to_mph(100))
print(convert_to_mph(160))

print(convert_to_mph.__annotations__)

