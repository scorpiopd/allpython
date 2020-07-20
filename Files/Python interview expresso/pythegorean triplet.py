"""— Pythagorean Triples consists of three positive integers a, b, and c, such that: a² + b² = c²
 (a and b are cathetus and c is the hypotenuse). An example of a Pythagorean Triplets is 3, 4 and 5
 because 3² + 4² = 5², Calculating this becomes: 9 + 16 = 25 a Pythagorean Triple!"""

triplet = [3,4,5]


def pytriplet(triplet):
    triplet.sort()
    for i in range(len(triplet)):
        for j in range(i + 1, len(triplet)):
            for k in range(j + 1, len(triplet)):
                if triplet[i]**2 + triplet[j]**2 == triplet[k]**2:
                    return True
                else:
                    return False
print(pytriplet(triplet))

