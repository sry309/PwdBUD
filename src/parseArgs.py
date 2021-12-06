import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d jd -c jingdong -o out.txt")
    parser.add_argument("-d", "--domain",  help="The domain...example: jd")
    parser.add_argument("-c", "--company", help="The company...example: jingdong")
    parser.add_argument("-e", "--element", help="Anyother element...")
    parser.add_argument("-o", "--outfile", help="Output file name")
    return parser.parse_args()

