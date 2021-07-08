from utils import get_comments, sanitise_comments, json_to_file
from config import API_KEY
import sys

args = sys.argv

if len(args) == 1:
    print("please enter a youtube video ID (such as 6yUKtPIRa5M).")
    sys.exit(1)

youtube_url = sys.argv[1]
result = get_comments(API_KEY, youtube_url)

if "error" in result:
    print(result['error']['message'])
    sys.exit(1)

else:
    output = sanitise_comments(result)
    json_to_file(output, youtube_url)
    
input("grabbing done, press any key to exit...")