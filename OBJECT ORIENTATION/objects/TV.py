class TV:
    def __init__(self):
        self.channel = 1  # Default channel is 1
        self.volumeLevel = 1  # Default volume level is 1
        self.on = False  # Default TV is off

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    #method to display current channel
    def getChannel(self):
        return self.channel

    #method to change the channel
    def setChannel(self, channel):
        #de tv moet aanstaan en de channel die de gebruiker kiest moet tussen het mogelijke bereik liggen
        if self.on and 1 <= self.channel <= 120:
            self.channel = channel

    def getVolumeLevel(self):
        return self.volumeLevel

    def setVolume(self, volumeLevel):
        if self.on and 1 <= self.volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    #er ligt een bovengrens zodat de channel niet boven het mogelijke gaat
    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1

    #er ligt een ondergrens
    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    #er ligt een bovengrens
    def volumeUp(self):
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    #er ligt een ondergrens
    def volumeDown(self):
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1