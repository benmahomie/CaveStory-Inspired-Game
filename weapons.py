class Weapon():
    def __init__(self, dmg, ammo, cooldown, max_bullets_allowed):
        self.dmg = dmg
        self.ammo = ammo
        self.cooldown = cooldown
        self.max_bullets_allowed = max_bullets_allowed

class Polar_Star(Weapon):
    def __init__(self, dmg=10, ammo=None, cooldown=None, max_bullets_allowed=2):
        super().__init__(dmg, ammo, cooldown, max_bullets_allowed)
