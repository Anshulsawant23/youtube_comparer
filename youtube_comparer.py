import requests
import json
import sys
import re
import inflect
def main():


#asking user for an API key
    api=input("Kindly enter your Youtube Data API V3  key.-")
    if not api:
        sys.exit("Please enter a valid API key.")

#asking user for youtube channel handles
    creator_1=input("Who is your favourite Youtuber? Enter his handle please.-")
    creator_2=input(f"{creator_1}, great choice! Let's compare him to another youtuber. Enter the handle of the other youtuber-")
    x=creator_1.replace("@","")
    y=creator_2.replace("@","")
#creating an engine
    engine=inflect.engine()

#checking validity of handles
    if not (3<len(x)<30 and 3<len(y)<30):
        sys.exit("Please re-run and enter a valid youtube handle between 3 and 30 characters!")
    if creator_1==creator_2:
        sys.exit("Please enter different youtubers!")

    match=re.match(r"^@[A-Za-z0-9._-]+$", creator_1)
    if not match:
        sys.exit("Please re-run and enter a valid youtube channel handle")
    match_1=re.match(r"^@[A-Za-z0-9._-]+$", creator_2)
    if not match_1:
        sys.exit("Please re-run and enter a valid youtube channel handle")

#sending request for getting channel id of creator 1
    try:
        c1_request_forid=requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q="+creator_1+"&maxResults=1&key="+api)
        c1_response_forid=c1_request_forid.json()
        c1_id=c1_response_forid["items"][0]["id"]["channelId"]



#sending request for getting channel id of creaotr 1
        c2_request_forid=requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q="+creator_2+"&maxResults=1&key="+api)
        c2_response_forid=c2_request_forid.json()
        c2_id= c2_response_forid["items"][0]["id"]["channelId"]
    except (KeyError, IndexError, ValueError):
        sys.exit("Something went wrong. Please ensure that you have entered the right API key and Youtuber handles.")


#getting more detailed data for both channels using the channel id we got
    try:
        c1_request_for_data=requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id="+c1_id+"&key="+api)
        c1_data=c1_request_for_data.json()
        c2_request_for_data=requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id="+c2_id+"&key="+api)
        c2_data=c2_request_for_data.json()
    except (KeyError, IndexError):
        sys.exit("Something went wrong. Maybe the data for this account is not public. Please try with another channel")


#getting subscriber data
    c1_subs = c1_data["items"][0]["statistics"]["subscriberCount"]
    c1_subs=int(c1_subs)
    c2_subs = c2_data["items"][0]["statistics"]["subscriberCount"]
    c2_subs=int(c2_subs)

#getting views data
    c1_views = c1_data["items"][0]["statistics"]["viewCount"]
    c1_views=int(c1_views)
    c2_views = c2_data["items"][0]["statistics"]["viewCount"]
    c2_views=int(c2_views)


#getting data on number of videos
    c1_vid=c1_data["items"][0]["statistics"]["videoCount"]
    c1_vid=int(c1_vid)
    c2_vid=c2_data["items"][0]["statistics"]["videoCount"]
    c2_vid=int(c2_vid)


    print(compare_subs(c1_subs, c2_subs, creator_1, creator_2, engine))
    print(compare_views(c1_views, c2_views, creator_1, creator_2, engine))
    print(compare_videos(c1_vid, c2_vid, creator_1, creator_2, engine))


def compare_subs(c1_subs, c2_subs, creator_1, creator_2, engine):


    if c1_subs>c2_subs:
        return f"{creator_1} has {engine.number_to_words(c1_subs-c2_subs)} more subscribers than {creator_2}"
    elif c2_subs>c1_subs:
        return f"{creator_2} has {engine.number_to_words(c2_subs-c1_subs)} more subscribers than {creator_1}"
    else:
        return f"Wow! Both {creator_1} and {creator_2} have the same number of subscribers. What a coincidence!"

def compare_views(c1_views, c2_views,  creator_1, creator_2, engine):

    if c1_views>c2_views:
        return f"{creator_1} has {engine.number_to_words(c1_views-c2_views)} more views than {creator_2}"
    elif c2_views>c1_views:
        return f"{creator_2} has {engine.number_to_words(c2_views-c1_views)} more views than {creator_1}"
    else:
        return f"Wow! Both {creator_1} and {creator_2} have the same number of views. What a coincidence!"

def compare_videos(c1_vid, c2_vid,  creator_1, creator_2, engine):
    if c1_vid>c2_vid:
        return f"{creator_1} has made {engine.number_to_words(c1_vid-c2_vid)} more videos than {creator_2}"
    if c2_vid>c1_vid:
        return f"{creator_2} has made {engine.number_to_words(c2_vid-c1_vid)} more videos than {creator_1}"
    else:
        return f"Wow! Both {creator_1} and {creator_2} have made the same number of videos!"
if __name__=="__main__":
    main()
