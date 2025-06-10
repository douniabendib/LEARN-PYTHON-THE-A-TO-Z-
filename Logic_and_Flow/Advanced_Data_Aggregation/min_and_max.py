"""
You are given two lists: temperatures containing daily temperatures 
in Fahrenheit, and humidity containing daily humidity percentages. 
Your task is to write a program that:

Finds and prints the highest and lowest temperature from the 
temperatures list using max() and min().
Finds and prints the highest and lowest humidity from the humidity 
list using max() and min().
"""
temperatures = [72, 68, 75, 80, 65, 70, 78]
humidity = [60, 55, 65, 70, 50, 58, 62]

print(f"Highest temperature: {max(temperatures)}°F")
print(f"Lowest temperature: {min(temperatures)}°F")
print(f"Highest humidity: {max(humidity)}%")
print(f"Lowest humidity: {min(humidity)}%")
