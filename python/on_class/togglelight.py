def toggle_light(light_on: bool):
    if light_on:
        light_on = False
        print ("Light turned off")
    else:
        light_on = True
        print("Light turned on")
toggle_light(False)