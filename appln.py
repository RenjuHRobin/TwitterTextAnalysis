
def main_method(): 
	
    print("Starting the program")
    print("Enter value of n " )
    n = int(input())
    client = Client() #new object created
    alltweets = client.read_tweets('D:/Courses/SSDI/twitter/JUSTICE1.txt',n)
	print("The program is complete")


class Tweet:

	def __init__(self, user_name, tweet_time, tweet_text, retweet_count, no_of_followers):
		self.user_name = user_name
		self.tweet_time = tweet_time
		self.tweet_text = tweet_text
		self.retweet_count = retweet_count
		self.no_of_followers = no_of_followers

	def __str__(self):
		return "{user_name = %s, tweet_time = %s, tweet_text = %s, retweet_count = %s, no_of_followers = %s}"%(self.user_name, self.tweet_time, self.tweet_text, self.retweet_count, self.no_of_followers)


class Client:
	def read_tweets(self, file_name,n):
		fo = open(file_name, "r")
		print ("Name of the file: ", fo.name)
		tweet_list = []
		for line in fo:
			tweet_list.append(self.extract_tweet(line))
		
		self.display_users_maximum_followers(tweet_list,n)
		self.display_tweets_maximum_retweetcount(tweet_list,n)
		fo.close	
		print("file read complete")

	def extract_tweet(self, line):
		list = line.split()
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
