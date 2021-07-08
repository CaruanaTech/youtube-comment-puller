import json
import requests

params = {}
params["part"] = "snippet"  # mandatory
params["textFormat"] = "plainText"  # or html

def get_comments(api_key, vid_id, max_results=False):
    url = "https://www.googleapis.com/youtube/v3/commentThreads?"
    
    params["videoId"] = vid_id
    params["key"] = api_key
    
    if max_results:
        params["maxResults"] = max_results
    
    # url formatting
    i = 0
    for param in params:
        if i == 0:
            url = url + param + '=' + params[param]
            i = i + 1
        else:
            url = url + '&' + param + '=' + params[param]
    
    # hit the API with our new URL
    resp = requests.get(url)
    
    # turn our response into a json
    comments = json.loads(resp.content)
    return comments

def sanitise_comments(comments_json):
    """turn a default youtube API comments thread into usable data by stripping out the useless junk

    Args:
        comments_json (dict): the original JSON from the API

    Returns:
        dict: dictionary with strictly relevant information.
    """
    comments = {}
    i = 0
    for item in comments_json['items']:
        comments[i] = {}
        top_level_comment = item['snippet']['topLevelComment']['snippet']
        
        comments[i]['username'] = top_level_comment['authorDisplayName']
        comments[i]['content'] = top_level_comment['textDisplay']
        comments[i]['timestamp'] = top_level_comment['updatedAt']
        i += 1

    return comments

def json_to_file(input, filename):
    content = json.dumps(input, indent=4, ensure_ascii=False).encode('utf-8')
    with open(f"{filename}.json", "wb") as json_file:
        json_file.write(content)
        json_file.close()