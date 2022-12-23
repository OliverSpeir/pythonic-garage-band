class Band:
    def __init__(self, name, members=False):
        self.name = name
        self.members = members or []

    def __repr__(self):
        return self.members

    def play_solos(self):
        return [x.play_solo() for x in self.members]


class Musician:
    def __init__(self, name, instrument, solo):
        self.name = name
        self.instrument = instrument
        self.solo = solo

    def __str__(self):
        return self.name

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar", "face melting guitar solo")


    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums", "rattle boom crash")

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass", "bom bom buh bom")

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

