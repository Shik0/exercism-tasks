def convert(number):

    sounds = {3: "Pling", 5: "Plang", 7: "Plong"}

    sound = ""

    for i in range(3,9,2):
        if number % i == 0:
            sound += sounds.get(i)

    return sound if sound else str(number)
