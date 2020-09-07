LEDBYNUMBERS = {"1":2,"2":5,"3":5,
        "4":4,"5":5,"6":6,
        "7":3,"8":7,"9":6,
        "0":6};

def calcLeds(inteiroText):
    leds = 0;
    for valor in str(inteiroText):
        leds += LEDBYNUMBERS[valor];
    return leds;

NUMTEST = int(input());

while NUMTEST > 0 : 
    inteiroText = str(input());

    totalLeds = calcLeds(inteiroText);

    print("%s leds" % totalLeds);

    NUMTEST -= 1;