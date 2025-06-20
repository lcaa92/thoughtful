
def sort(width, height, length, mass):
    # Check if the package is bulky
    is_bulky = width * height * length >= 1000000
    dimension_limit = 150
    if width >= dimension_limit or height >= dimension_limit or length >= dimension_limit:
        is_bulky = True
        
    # Check if the package is heavy
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    
    if is_bulky or is_heavy:
        return "SPECIAL"

    return "STANDARD"


if __name__ == "__main__":
    import sys
    width, height, length, mass = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    print(sort(width, height, length, mass))