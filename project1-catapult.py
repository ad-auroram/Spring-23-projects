import math
def main ():
    #ask for distance and angle
    distance = eval(input("Distance to professor (m): "))
    angle = eval(input("Angle of elevation (degrees): "))
    #convert degrees to radians
    theta = math.radians(angle)
    #defining x
    x = math.sqrt((0.065 * 9.8 * distance) / (25 * math.sin(2 * theta)))

    print("You need to pull back", x , "meters to deliver the egg.")

main()