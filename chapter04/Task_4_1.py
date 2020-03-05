# The program displays a string of numbers with the specified start, end , and step

start = int(input('Enter origin\n'))
end = int(input('Enter the end of the countdown\n'))
interval = int(input('Enter the interval\n'))

for i in range(start, end+1, interval):
    print(i, end=' ')
