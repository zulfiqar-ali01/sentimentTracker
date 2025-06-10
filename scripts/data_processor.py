import json
import random
from datetime import datetime, timedelta
import numpy as np
from collections import Counter

class SentimentDataProcessor:
    """Process and analyze Twitter sentiment data"""
    
    def __init__(self, query=None, data=None):
        """Initialize with either a query to generate data or existing data"""
        self.query = query
        
        if data:
            self.data = data
        elif query:
            self.data = self._generate_sample_data()
        else:
            self.data = []
            
        self.processed_data = {
            "overview": {},
            "timeline": [],
            "wordcloud": [],
            "regions": []
        }
    
    def _generate_sample_data(self, count=1000, days=30):
        """Generate sample Twitter data for demonstration"""
        print(f"Generating sample data for '{self.query}' with {count} tweets over {days} days")
        
        tweets = []
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Define sentiment distribution
        sentiment_weights = [0.65, 0.23, 0.12]  # positive, negative, neutral
        
        # US states with population-weighted distribution
        states = {
            "CA": 0.12, "TX": 0.09, "FL": 0.07, "NY": 0.06, "PA": 0.04,
            "IL": 0.04, "OH": 0.04, "GA": 0.03, "NC": 0.03, "MI": 0.03,
            "NJ": 0.03, "VA": 0.03, "WA": 0.02, "AZ": 0.02, "MA": 0.02,
            "Other": 0.33
        }
        
        for i in range(count):
            # Random date within range
            random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
            tweet_date = start_date + timedelta(seconds=random_seconds)
            
            # Random sentiment
            sentiment_type = random.choices(
                ["positive", "negative", "neutral"], 
                weights=sentiment_weights, 
                k=1
            )[0]
            
            # Random sentiment score based on type
            if sentiment_type == "positive":
                sentiment_score = random.uniform(0.3, 1.0)
            elif sentiment_type == "negative":
                sentiment_score = random.uniform(-1.0, -0.3)
            else:
                sentiment_score = random.uniform(-0.3, 0.3)
            
            # Random location
            location = random.choices(
                list(states.keys()),
                weights=list(states.values()),
                k=1
            )[0]
            
            # Random engagement metrics
            retweets = int(np.random.exponential(5))
            likes = int(np.random.exponential(10))
            replies = int(np.random.exponential(2))
            
            # Create tweet object
            tweet = {
                "id": i,
                "text": f"Sample tweet about {self.query} with {sentiment_type} sentiment",
                "created_at": tweet_date.isoformat(),
                "user_location": location,
                "retweet_count": retweets,
                "favorite_count": likes,
                "reply_count": replies,
                "sentiment_type": sentiment_type,
                "sentiment_score": sentiment_score
            }
            
            tweets.append(tweet)
        
        return tweets
    
    def process_data(self):
        """Process the data and generate all required metrics"""
        if not self.data:
            print("No data to process")
            return self.processed_data
        
        print(f"Processing {len(self.data)} tweets")
        
        # Process overview metrics
        self._process_overview()
        
        # Process timeline data
        self._process_timeline()
        
        # Process word cloud data
        self._process_wordcloud()
        
        # Process region data
        self._process_regions()
        
        return self.processed_data
    
    def _process_overview(self):
        """Process overview metrics"""
        total_tweets = len(self.data)
        
        # Count sentiment types
        sentiment_counts = Counter(tweet["sentiment_type"] for tweet in self.data)
        positive_count = sentiment_counts.get("positive", 0)
        negative_count = sentiment_counts.get("negative", 0)
        neutral_count = sentiment_counts.get("neutral", 0)
        
        # Calculate percentages
        positive_pct = round((positive_count / total_tweets) * 100)
        negative_pct = round((negative_count / total_tweets) * 100)
        neutral_pct = round((neutral_count / total_tweets) * 100)
        
        # Calculate overall sentiment score (0-100)
        overall_sentiment = round(positive_pct)
        
        # Calculate engagement metrics
        total_retweets = sum(tweet.get("retweet_count", 0) for tweet in self.data)
        total_likes = sum(tweet.get("favorite_count", 0) for tweet in self.data)
        total_replies = sum(tweet.get("reply_count", 0) for tweet in self.data)
        total_engagement = total_retweets + total_likes + total_replies
        
        # Estimate reach (very rough estimate)
        avg_followers = 500  # Assumption
        potential_reach = round(total_tweets * avg_followers / 1000000, 1)  # In millions
        
        # Determine trend (comparing first half to second half)
        mid_point = len(self.data) // 2
        first_half = self.data[:mid_point]
        second_half = self.data[mid_point:]
        
        first_half_positive = sum(1 for t in first_half if t["sentiment_type"] == "positive") / len(first_half)
        second_half_positive = sum(1 for t in second_half if t["sentiment_type"] == "positive") / len(second_half)
        
        trend = "up" if second_half_positive > first_half_positive else "down"
        
        # Store overview data
        self.processed_data["overview"] = {
            "overall": overall_sentiment,
            "totalMentions": total_tweets,
            "positivePercentage": positive_pct,
            "negativePercentage": negative_pct,
            "neutralPercentage": neutral_pct,
            "engagement": total_engagement,
            "reachInMillions": potential_reach,
            "trending": trend
        }
        
        print(f"Overall sentiment: {overall_sentiment}% positive")
    
    def _process_timeline(self):
        """Process timeline data"""
        # Group tweets by day
        tweets_by_day = {}
        for tweet in self.data:
            day = tweet["created_at"].split("T")[0]
            if day not in tweets_by_day:
                tweets_by_day[day] = []
            tweets_by_day[day].append(tweet)
        
        # Calculate sentiment percentages for each day
        timeline_data = []
        for day, day_tweets in sorted(tweets_by_day.items()):
            positive = sum(1 for t in day_tweets if t["sentiment_type"] == "positive")
            negative = sum(1 for t in day_tweets if t["sentiment_type"] == "negative")
            neutral = sum(1 for t in day_tweets if t["sentiment_type"] == "neutral")
            total = len(day_tweets)
            
            # Format date for display (Jun 1, Jun 2, etc.)
            display_date = datetime.fromisoformat(day).strftime("%b %d")
            
            timeline_data.append({
                "date": display_date,
                "positive": round(positive / total * 100),
                "negative": round(negative / total * 100),
                "neutral": round(neutral / total * 100)
            })
        
        self.processed_data["timeline"] = timeline_data
        print(f"Generated timeline data for {len(timeline_data)} days")
    
    def _process_wordcloud(self):
        """Process word cloud data"""
        # In a real app, we would extract words from tweets
        # Here we'll generate sample words related to the query
        
        # Sample words for different sentiments
        positive_words = [
            "support", "great", "excellent", "beneficial", "progress",
            "innovative", "success", "effective", "helpful", "positive",
            "advantage", "opportunity", "solution", "improvement", "achievement"
        ]
        
        negative_words = [
            "concern", "problem", "issue", "failure", "risk",
            "challenge", "difficult", "costly", "ineffective", "negative",
            "disadvantage", "threat", "obstacle", "drawback", "limitation"
        ]
        
        neutral_words = [
            "policy", "implementation", "strategy", "approach", "initiative",
            "program", "plan", "development", "change", "impact",
            "result", "effect", "outcome", "process", "system"
        ]
        
        # Generate word cloud data
        wordcloud_data = []
        
        # Add positive words
        for word in positive_words:
            wordcloud_data.append({
                "text": word,
                "value": random.randint(20, 50),
                "sentiment": "positive"
            })
        
        # Add negative words
        for word in negative_words:
            wordcloud_data.append({
                "text": word,
                "value": random.randint(15, 40),
                "sentiment": "negative"
            })
        
        # Add neutral words
        for word in neutral_words:
            wordcloud_data.append({
                "text": word,
                "value": random.randint(25, 60),
                "sentiment": "neutral"
            })
        
        # Sort by value (frequency)
        wordcloud_data.sort(key=lambda x: x["value"], reverse=True)
        
        self.processed_data["wordcloud"] = wordcloud_data
        print(f"Generated word cloud data with {len(wordcloud_data)} terms")
    
    def _process_regions(self):
        """Process region-based sentiment data"""
        # Group tweets by location
        tweets_by_location = {}
        for tweet in self.data:
            location = tweet.get("user_location", "Unknown")
            if location not in tweets_by_location:
                tweets_by_location[location] = []
            tweets_by_location[location].append(tweet)
        
        # Calculate sentiment for each location
        region_data = []
        for location, location_tweets in tweets_by_location.items():
            if location == "Unknown" or len(location_tweets) < 5:
                continue
                
            positive = sum(1 for t in location_tweets if t["sentiment_type"] == "positive")
            total = len(location_tweets)
            sentiment_score = round(positive / total * 100)
            
            # Get full state name
            state_name = self._get_state_name(location)
            
            region_data.append({
                "id": location,
                "name": state_name,
                "sentiment": sentiment_score,
                "mentions": total
            })
        
        # Sort by number of mentions
        region_data.sort(key=lambda x: x["mentions"], reverse=True)
        
        self.processed_data["regions"] = region_data
        print(f"Generated region data for {len(region_data)} regions")
    
    def _get_state_name(self, state_code):
        """Convert state code to full name"""
        state_names = {
            "CA": "California",
            "TX": "Texas",
            "FL": "Florida",
            "NY": "New York",
            "PA": "Pennsylvania",
            "IL": "Illinois",
            "OH": "Ohio",
            "GA": "Georgia",
            "NC": "North Carolina",
            "MI": "Michigan",
            "NJ": "New Jersey",
            "VA": "Virginia",
            "WA": "Washington",
            "AZ": "Arizona",
            "MA": "Massachusetts"
        }
        return state_names.get(state_code, state_code)

def main():
    # Example usage
    processor = SentimentDataProcessor(query="climate policy")
    results = processor.process_data()
    
    # Print some sample results
    print("\nOverview:")
    print(f"Overall sentiment: {results['overview']['overall']}% positive")
    print(f"Total mentions: {results['overview']['totalMentions']}")
    print(f"Trending: {results['overview']['trending']}")
    
    print("\nTimeline (first 3 days):")
    for day in results['timeline'][:3]:
        print(f"{day['date']}: Positive {day['positive']}%, Negative {day['negative']}%, Neutral {day['neutral']}%")
    
    print("\nTop words (first 5):")
    for word in results['wordcloud'][:5]:
        print(f"{word['text']}: {word['value']} mentions ({word['sentiment']})")
    
    print("\nTop regions (first 3):")
    for region in results['regions'][:3]:
        print(f"{region['name']}: {region['sentiment']}% positive ({region['mentions']} mentions)")

if __name__ == "__main__":
    main()
