from clock_hand import ClockHand

class Timer:

    def __init__(self):
        self.secs = ClockHand(60)
        self.hunds = ClockHand(100)

    def advance(self):
        # implement the advance method here
        self.hunds.advance()

        if (self.hunds.get_value() == 0):
            self.secs.advance()

    def __str__(self):
        # implement the string representation here
        return str(self.secs) + ":" + str(self.hunds)
