class Fish:
    rod_length = "7.6"
    reel_size = "5000"
    line = "30 lb"
    lure = "metal jig"

    def __init__(self,lure):
        self.lure = lure
    def __str__(self):
        return f"Fishing setup rod_lenght:{self.rod_length}: reel_size:{self.reel_size} line:{self.line} lure:{self.lure}"




myFish = Fish("chino 15gr")

print(myFish)

