# 说明在 __init__.py
# 推测 默认tweetId不重复
# 推文字段
"""
[{"tweetId": xx, "time": "xx", "userId": xx}]
"""
# 关注字段
"""
{1:{2,3}, 2:{1,3}}
"""
import datetime
from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.twitter = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.twitter.append({"userId": userId, "tweetId": tweetId, "time": datetime.datetime.now()})
        print(self.twitter)
        return self.twitter

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        userIds = self.follows.get(userId)
        if userIds:
            self.userIds = list(userIds)
            self.userIds.append(userId)
        else:
            self.userIds = [userId]
        f = list(filter(self._filter, self.twitter))
        f.sort(key=lambda x: x["time"], reverse=True)
        for i in f[:10]:
            yield i['tweetId']

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if self.follows.get(followerId):
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = {followeeId}
        print(self.follows)
        return self.follows

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if self.follows.get(followerId):
            self.follows[followerId].discard(followeeId)
        print(self.follows)

    def _filter(self, _twitter):
        return _twitter['userId'] in self.userIds


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

obj = Twitter()
obj.postTweet(1,5)
param_2 = obj.getNewsFeed(1)
print(param_2)
for i in param_2:
    print(i)
obj.follow(1,2)
obj.postTweet(2, 6)
obj.getNewsFeed(1)
obj.unfollow(1, 2)
obj.getNewsFeed(1)

