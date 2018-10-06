#!/usr/bin/python3


# https://www.journaldev.com/17752/python-main-function - To run a python file from main method

# This is the view for the project
def main_method(): 
	#This could be any name. Its the if below that decides what runs first
    print("Starting the program")
    # Read input n : uncomment below two lines
    print("Enter value of n " )
    n = int(input())
    client = Client() #new object created
    alltweets = client.read_tweets('D:/Courses/SSDI/twitter/JUSTICE.txt',n)
	
    #Now write the code to perform all logic
    print("The program is complete")


#The Data model for the project
#The class represents a single Tweet. So making name singular.
class Tweet:

	#All classes have a function called __init__(), which is always executed when the class is being initiated.
	#Its their constructor
	#'self' in python = 'this' in java. It does not have to be named self , 
	#you can call it whatever you like, but it has to be the first parameter of any function in the class
	def __init__(self, user_name, tweet_time, tweet_text, retweet_count, no_of_followers):
		self.user_name = user_name
		self.tweet_time = tweet_time
		self.tweet_text = tweet_text
		self.retweet_count = retweet_count
		self.no_of_followers = no_of_followers

	#This is the pythons toString() method	
	def __str__(self):
		return "{user_name = %s, tweet_time = %s, tweet_text = %s, retweet_count = %s, no_of_followers = %s}"%(self.user_name, self.tweet_time, self.tweet_text, self.retweet_count, self.no_of_followers)


# The controller for the project
class Client:
	def read_tweets(self, file_name,n):
		# # Open the file with read only permit
		# http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/
		fo = open(file_name, "r")
		print ("Name of the file: ", fo.name)
		tweet_list = []
		for line in fo:
			tweet_list.append(self.extract_tweet(line))
		
		self.display_users_maximum_followers(tweet_list,n)
		self.display_tweets_maximum_retweetcount(tweet_list,n)
		#print (tweet_list[:n])
		#for x in tweet_list and i < n:
		#	print(x.no_of_followers)
		#	i+= 1
			
		# Close opened file
		fo.close	
		print("file read complete")

	def extract_tweet(self, line):
		list = line.split()
		# Sample split entry 
		# ['Over45StillFly', '[28/Sep/2018:22:44:51', ']', '"RT', '@claireatki:', 'A', 'nation', 'riveted...20.4', 'million', 'people', 'watched', 'ABC,', 'CBS,', 'NBC,', 'Fox', 'News,', 'CNN', 'and', 'MSNBC', 'yesterday,', 'says', 'Nielsen."', '621', '26']
		# 1st entry is user_name
		# 2nd entry is date
		# 3rd entry is ] - drop it
		# 2nlast entry is  retweet_count
		# last entry is no of followers
		#Left over in list is the tweet
		user_name = list.pop(0) #pop will remove and return the element at specific index
		tweet_time = list.pop(0)
		#clean the [ at beginning of tweet_time
		tweet_time = tweet_time.replace("[","")
		no_of_followers = list.pop() # by default pop will remove last element in list (like stack)
		retweet_count = list.pop()
		#join remaining list members to get a tweet
		tweet_text = " ".join(list)
		tweet = Tweet(user_name, tweet_time, tweet_text, retweet_count, no_of_followers)
		#print(tweet)
		return tweet

	def display_users_maximum_followers(self,tweet_list,n):
		tweet_list.sort(key = lambda x: int(x.no_of_followers),reverse=True)
		
		print("Sorting performed with number of followers")
		for x in tweet_list:
			print(x.no_of_followers)
		
		print("Printing Top "+str(n)+" Users with maximum followers")
		print ([x.user_name for x in tweet_list[:n]])
		
	def display_tweets_maximum_retweetcount(self,tweet_list,n):
		tweet_list.sort(key = lambda x: int(x.retweet_count),reverse=True)
		
		print("Sorting performed by maximum retweet count")
		for tweet_element in tweet_list:
			print(tweet_element.retweet_count)
		
		print("Printing Top "+str(n)+" Tweets with maximum retweet count")
		print ([x.tweet_text for x in tweet_list[:n]])
		
if __name__ == '__main__':
    main_method() 

# In case of formatting space tab problems check https://pythoniter.appspot.com/
