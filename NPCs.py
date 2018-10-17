class Human:

    name = " "
    zone = 0  # Defines the zone in which the npc is at
    trust_level = 0  # Defines the level of trust a specific npc has in the main character
    times_talked_to = 0  # Defines the times that the main character has spoken to a specific npc

    def __init__(self, name, zone, trust_lvl, times_talked_to):
        self.name = name
        self.zone = zone
        self.trust_lvl = trust_lvl
        self.times_talked_to = times_talked_to
