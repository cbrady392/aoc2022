

def get_input():
    output = []
    with open('input.txt') as f:
        output = [line.strip() for line in f.readlines()]
    return output

points = {
        'X': {
            'p': 1,
            'A': 3,
            'B': 0,
            'C': 6
            },
        'Y': {
            'p': 2,
            'A': 6,
            'B': 3,
            'C': 0
            },
        'Z': {
            'p': 3,
            'A': 0,
            'B': 6,
            'C': 3,
            }
        }

points2 = {
        'X': {
            'p': 0,
            'A': 3,
            'B': 1,
            'C': 2
            },
        'Y': {
            'p': 3,
            'A': 1,
            'B': 2,
            'C': 3
            },
        'Z': {
            'p': 6,
            'A': 2,
            'B': 3,
            'C': 1
            }
        }
def main():
   score = 0
   score2 = 0
   for play in get_input():
       opp, you = play.split(' ')
       score += points[you]['p'] + points[you][opp]
       score2 += points2[you]['p'] + points2[you][opp]
   print(score, score2)

if __name__ == '__main__':
    main()
