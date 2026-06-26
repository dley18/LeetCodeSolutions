import heapq

class Twitter:

    def __init__(self):
        self.users = {}
        self.post_count = 0

    def createUser(self, userId):
        self.users[userId] = {}
        self.users[userId]["tweets"] = []
        self.users[userId]["following"] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_count += 1
        if userId in self.users:
            self.users[userId]["tweets"].append([self.post_count, tweetId])
        else:
            self.createUser(userId)
            self.users[userId]["tweets"].append([self.post_count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        if userId in self.users:

            
            for folowee in self.users[userId]["following"]:
                if folowee == userId:
                    continue
                tweets = self.users[folowee]["tweets"]
                for tweet in tweets:
                    heapq.heappush_max(heap, tweet)

            for tweet in self.users[userId]["tweets"]:
                heapq.heappush_max(heap, tweet)
        res = []
        count = 0
        while count < 10 and heap:
            post = heapq.heappop_max(heap)
            res.append(post[1])
            count += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            if followeeId not in self.users[followerId]["following"]:
                self.users[followerId]["following"].append(followeeId)   
        else:
            self.createUser(followerId)
            self.users[followerId]["following"].append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            if followeeId in self.users[followerId]["following"]:
                self.users[followerId]["following"].remove(followeeId)
