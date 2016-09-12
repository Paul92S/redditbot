import praw 
import time

r = praw.Reddit(user_agent = "Reddit bot by Pablo /u/Puerto")
r.login()

wordList = ['harambe', 'black', 'R.I.P']
cache = []

def run_bot():
	print("Fetching subreddit...")
	subreddit = r.get_subreddit("test")
	print("Fetching Comments...")
	comments = subreddit.get_comments(limit=25)
	for comment in comments:
		comment_text = comment.body.lower()
		isMatch = any(string in comment_text for string in wordList)
		if comment.id not in cache and isMatch:
			print("A Match found")
			comment.reply(':,(')
			print("Reply success")
			cache.append(comment.id)
        print("comments loops is finished, sleep timer activated")


while True:
	run_bot()
	time.sleep(10)
