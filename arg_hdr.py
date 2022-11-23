import argparse
import sys
from hidrostatis import hidrostatis

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--r', type=float, default=0.0,
                        help='Massa jenis zat cair?')
    parser.add_argument('--g', type=float, default=9.8,
                        help='Gravitasi ?')
    parser.add_argument('--h', type=float, default=0.0,
                        help='Kedalaman?')
    parser.add_argument('--hm', type=float, default=0.0,
                        help='Tinggi tabung?')
    parser.add_argument('--op', type=str, default="null",
                        help='Menghitung tekanan hidrostatis (hd) ')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    if args.op == 'null':
        x = 'Masukan operasi yang akan dilakukan'
        return x
    if args.op == 'hd':
        hd=args.r * args.g * args.h
        r1=args.r
        h=args.h
        hm=args.hm
        g=args.g
        hidrostatis(r1,g,h,hm)

if __name__ == '__main__':
    main()