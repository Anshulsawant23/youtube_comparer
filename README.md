# YOUTUBE COMPARER

A Python command-line program that compares two YouTube channels using the YouTube Data API v3.

## What it does

Given two YouTube channel handles (e.g., `@creator1` and `@creator2`) and a valid YouTube Data API key, this program compares them across three metrics:

- Total subscribers  
- Total views  
- Total number of uploaded videos  

The program:

1. Validates both handles  
   - Must begin with `@`  
   - Between 3 and 30 characters  
   - Must follow YouTube’s handle rules  
   - Cannot be the same channel twice  

2. Uses each handle to retrieve the channel’s unique ID via the YouTube API.  

3. Uses those IDs to make a second API call to fetch channel statistics.  

4. Extracts the relevant data from the JSON response and converts it to integers for comparison.  

5. Compares the channels using three functions:  
   - `compare_subs()`  
   - `compare_views()`  
   - `compare_videos()`  

Differences are expressed in words (e.g., “two million more subscribers”) using the **inflect** library, making large numbers easier to read.

> *Note:* I originally wrote tests for this project during CS50P — I just didn’t port them into this repository yet.


## How to run

1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the program: 
```bash
python youtube_comparer.py
```

3. When prompted, enter your YouTube Data API v3 key.  

4. Enter two valid YouTube handles starting with `@`.



## Getting a free YouTube API key

1. Go to Google Cloud Console and sign in.  
2. Enable YouTube Data API v3 under APIs & Services.  
3. Create credentials and generate an API key.
