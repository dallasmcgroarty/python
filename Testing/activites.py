def eat(food, is_healthy):
    ending = "because YOLO!"

    if is_healthy:
        ending = "because it's gooood"

    return f"I'm eating {food}, {ending}"

def nap(num_hours):
    if num_hours > 2:
        return "Ugh I overslept and now I'm groggy"
    else:
        return "I'm feeling good after an hour nap"

def is_funny(person):
    if person is "Time":
        return False
