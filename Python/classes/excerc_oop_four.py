class Head:
    def __init__(self):
        pass

class Hand:
    def __init__(self, side):
        self.side = side   # "right" or "left"

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Feet:
    def __init__(self, side):
        self.side = side   # "right" or "left"

class Leg:
    def __init__(self, feet):
        self.feet = feet

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Human:
    def __init__(self, torso):
        self.torso = torso
        print("A new human has been created.")


head = Head()

right_hand = Hand("right")
left_hand = Hand("left")

right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

right_feet = Feet("right")
left_feet = Feet("left")

right_leg = Leg(right_feet)
left_leg = Leg(left_feet)

torso = Torso(head, right_arm, left_arm, right_leg, left_leg)

human1 = Human(torso)
