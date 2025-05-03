from .dod250 import DOD250SVG
from .double_muff import DoubleMuffSVG
from .dual250 import Dual250SVG

def main():
    # generate svg
    items = [
        (DOD250SVG, './build/dod250.svg')
        (DoubleMuffSVG, './build/doublemuff.svg')
        (Dual250SVG, './build/dual250.svg')
    ]

    # write to file
    for cls, path in items:
        decal = cls()
        with open(path, 'w') as f:
            f.write(decal.build())


if __name__ == '__main__':
    main()