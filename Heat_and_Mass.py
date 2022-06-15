print ("""What do you want to find?
If you want to find heat, print h; 
if -- specific heat, print sh;
if -- mass, print m.""")
find = input(str()) 

# region heat
if find == "h":
    print("Enter specific heat:")
    specific_heat = float(input())
    print("Enter mass:")
    mass = float(input())
    heat = mass * specific_heat
    print(heat)
#endregion
# region specific heat
if find == "sh":
    print("Enter heat:")
    heat = float(input())
    print("Enter mass:")
    mass = float(input())
    specific_heat = heat / mass
    print(specific_heat)
#endregion
# region mass
if find == "m":
    print("Enter heat:")
    heat = float(input())
    print("Enter specific heat:")
    specific_heat = float(input())
    mass = heat / specific_heat
    print(specific_heat)
#endregion

