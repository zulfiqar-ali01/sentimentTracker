import json
import random
from datetime import datetime, timedelta
import numpy as np
from collections import Counter

class PakistanSentimentProcessor:
    """Process Pakistan-specific sentiment data for 9th May 2023 incident"""
    
    def __init__(self, incident_date="2023-05-09"):
        self.incident_date = datetime.strptime(incident_date, "%Y-%m-%d")
        self.data = self._generate_pakistan_data()
        self.processed_data = {
            "overview": {},
            "timeline": [],
            "wordcloud": [],
            "regions": []
        }
    
    def _generate_pakistan_data(self, count=5000, days=14):
        """Generate Pakistan-specific Twitter data around May 9th incident"""
        print(f"Generating Pakistan data for 9th May 2023 incident with {count} tweets over {days} days")
        
        tweets = []
        start_date = self.incident_date - timedelta(days=7)  # Week before
        end_date = self.incident_date + timedelta(days=7)    # Week after
        
        # Pakistani provinces and cities with realistic distribution
        pakistan_locations = {
            "Punjab": 0.35,
            "Sindh": 0.25,
            "Islamabad": 0.15,
            "KPK": 0.12,
            "Lahore": 0.08,
            "Karachi": 0.03,
            "Balochistan": 0.02
        }
        
        # Keywords related to the incident
        imran_khan_keywords = ["imran", "khan", "pti", "chairman", "leader"]
        violence_keywords = ["violence", "vandalism", "attack", "destroy", "burn"]
        political_keywords = ["arrest", "court", "justice", "democracy", "corruption"]
        
        for i in range(count):
            # Random date within range
            random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
            tweet_date = start_date + timedelta(seconds=random_seconds)
            
            # Sentiment distribution changes based on proximity to May 9th
            days_from_incident = abs((tweet_date - self.incident_date).days)
            
            if days_from_incident == 0:  # May 9th - day of incident
                sentiment_weights = [0.20, 0.70, 0.10]  # Very negative
            elif days_from_incident <= 2:  # Days immediately after
                sentiment_weights = [0.25, 0.60, 0.15]  # Still very negative
            elif days_from_incident <= 5:  # Rest of the week
                sentiment_weights = [0.35, 0.50, 0.15]  # Moderately negative
            else:  # Before incident or later
                sentiment_weights = [0.50, 0.35, 0.15]  # More balanced
            
            # Random sentiment
            sentiment_type = random.choices(
                ["positive", "negative", "neutral"], 
                weights=sentiment_weights, 
                k=1
            )[0]
            
            # Generate realistic sentiment score
            if sentiment_type == "positive":
                sentiment_score = random.uniform(0.2, 0.9)
            elif sentiment_type == "negative":
                sentiment_score = random.uniform(-0.9, -0.2)
            else:
                sentiment_score = random.uniform(-0.2, 0.2)
            
            # Random location
            location = random.choices(
                list(pakistan_locations.keys()),
                weights=list(pakistan_locations.values()),
                k=1
            )[0]
            
            # Higher engagement on and around May 9th
            engagement_multiplier = max(1, 5 - days_from_incident) if days_from_incident <= 4 else 1
            
            # Generate keywords for the tweet
            tweet_keywords = []
            if random.random() < 0.7:  # 70% chance of Imran Khan mention
                tweet_keywords.extend(random.sample(imran_khan_keywords, random.randint(1, 2)))
            if random.random() < 0.4 and sentiment_type == "negative":  # Violence keywords in negative tweets
                tweet_keywords.extend(random.sample(violence_keywords, random.randint(1, 2)))
            if random.random() < 0.5:  # Political keywords
                tweet_keywords.extend(random.sample(political_keywords, random.randint(1, 2)))
            
            # Create tweet object
            tweet = {
                "id": i,
                "text": f"Tweet about {' '.join(tweet_keywords)} #9thMay #Pakistan #ImranKhan",
                "created_at": tweet_date.isoformat(),
                "user_location": location,
                "retweet_count": int(np.random.exponential(10) * engagement_multiplier),
                "favorite_count": int(np.random.exponential(20) * engagement_multiplier),
                "reply_count": int(np.random.exponential(5) * engagement_multiplier),
                "sentiment_type": sentiment_type,
                "sentiment_score": sentiment_score,
                "keywords": tweet_keywords
            }
            
            tweets.append(tweet)
        
        return tweets
    
    def process_pakistan_data(self):
        """Process Pakistan-specific data"""
        print(f"Processing {len(self.data)} Pakistan tweets")
        
        self._process_pakistan_overview()
        self._process_pakistan_timeline()
        self._process_pakistan_wordcloud()
        self._process_pakistan_regions()
        
        return self.processed_data
    
    def _process_pakistan_overview(self):
        """Process overview metrics for Pakistan incident"""
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
        
        # Overall sentiment (lower due to incident)
        overall_sentiment = positive_pct
        
        # Calculate engagement
        total_retweets = sum(tweet.get("retweet_count", 0) for tweet in self.data)
        total_likes = sum(tweet.get("favorite_count", 0) for tweet in self.data)
        total_replies = sum(tweet.get("reply_count", 0) for tweet in self.data)
        total_engagement = total_retweets + total_likes + total_replies
        
        # Estimate reach (Pakistan population context)
        avg_followers = 300  # Lower average for Pakistan
        potential_reach = round(total_tweets * avg_followers / 1000000, 1)
        
        # Trend analysis (comparing before and after May 9th)
        may_9_tweets = [t for t in self.data if t["created_at"].startswith("2023-05-09")]
        before_may_9 = [t for t in self.data if t["created_at"] < "2023-05-09"]
        after_may_9 = [t for t in self.data if t["created_at"] > "2023-05-09"]
        
        if before_may_9 and after_may_9:
            before_positive = sum(1 for t in before_may_9 if t["sentiment_type"] == "positive") / len(before_may_9)
            after_positive = sum(1 for t in after_may_9 if t["sentiment_type"] == "positive") / len(after_may_9)
            trend = "up" if after_positive > before_positive else "down"
        else:
            trend = "down"  # Default to down due to incident
        
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
        
        print(f"Pakistan Overview - Overall sentiment: {overall_sentiment}% positive")
        print(f"Total mentions: {total_tweets}, Engagement: {total_engagement}")
    
    def _process_pakistan_timeline(self):
        """Process timeline data focusing on May 9th incident"""
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
            
            # Format date for display
            date_obj = datetime.fromisoformat(day)
            display_date = date_obj.strftime("May %d")
            
            timeline_data.append({
                "date": display_date,
                "positive": round(positive / total * 100),
                "negative": round(negative / total * 100),
                "neutral": round(neutral / total * 100)
            })
        
        self.processed_data["timeline"] = timeline_data
        print(f"Generated Pakistan timeline data for {len(timeline_data)} days")
    
    def _process_pakistan_wordcloud(self):
        """Process word cloud data for Pakistan political context"""
        # Pakistan-specific political terms
        pakistan_terms = {
            # Pro-Imran Khan terms
            "ImranKhan": {"count": 0, "sentiment": "positive"},
            "PTI": {"count": 0, "sentiment": "positive"},
            "Justice": {"count": 0, "sentiment": "positive"},
            "Democracy": {"count": 0, "sentiment": "positive"},
            "Leader": {"count": 0, "sentiment": "positive"},
            "Support": {"count": 0, "sentiment": "positive"},
            "Rights": {"count": 0, "sentiment": "positive"},
            "Peaceful": {"count": 0, "sentiment": "positive"},
            
            # Negative incident terms
            "Violence": {"count": 0, "sentiment": "negative"},
            "Extremism": {"count": 0, "sentiment": "negative"},
            "Vandalism": {"count": 0, "sentiment": "negative"},
            "Arrest": {"count": 0, "sentiment": "negative"},
            "Chaos": {"count": 0, "sentiment": "negative"},
            "Destruction": {"count": 0, "sentiment": "negative"},
            "Anarchy": {"count": 0, "sentiment": "negative"},
            "Attack": {"count": 0, "sentiment": "negative"},
            
            # Neutral terms
            "Pakistan": {"count": 0, "sentiment": "neutral"},
            "9thMay": {"count": 0, "sentiment": "neutral"},
            "Lahore": {"count": 0, "sentiment": "neutral"},
            "Islamabad": {"count": 0, "sentiment": "neutral"},
            "Politics": {"count": 0, "sentiment": "neutral"},
            "Government": {"count": 0, "sentiment": "neutral"},
            "Military": {"count": 0, "sentiment": "neutral"},
            "Court": {"count": 0, "sentiment": "neutral"}
        }
        
        # Simulate word counts based on the incident
        for term, data in pakistan_terms.items():
            if term in ["ImranKhan", "PTI"]:
                data["count"] = random.randint(800, 1200)  # High mentions
            elif term in ["Violence", "9thMay", "Pakistan"]:
                data["count"] = random.randint(600, 900)   # High incident-related
            elif term in ["Arrest", "Chaos", "Extremism"]:
                data["count"] = random.randint(400, 600)   # Medium negative
            elif term in ["Justice", "Democracy", "Support"]:
                data["count"] = random.randint(300, 500)   # Medium positive
            else:
                data["count"] = random.randint(100, 300)   # Lower mentions
        
        # Convert to word cloud format
        wordcloud_data = []
        for term, data in pakistan_terms.items():
            wordcloud_data.append({
                "text": term,
                "value": data["count"],
                "sentiment": data["sentiment"]
            })
        
        # Sort by frequency
        wordcloud_data.sort(key=lambda x: x["value"], reverse=True)
        
        self.processed_data["wordcloud"] = wordcloud_data
        print(f"Generated Pakistan word cloud with {len(wordcloud_data)} terms")
    
    def _process_pakistan_regions(self):
        """Process region-based sentiment for Pakistani provinces"""
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
            if location == "Unknown" or len(location_tweets) < 10:
                continue
                
            positive = sum(1 for t in location_tweets if t["sentiment_type"] == "positive")
            total = len(location_tweets)
            sentiment_score = round(positive / total * 100)
            
            # Get region code
            region_code = self._get_pakistan_region_code(location)
            
            region_data.append({
                "id": region_code,
                "name": location,
                "sentiment": sentiment_score,
                "mentions": total
            })
        
        # Sort by number of mentions
        region_data.sort(key=lambda x: x["mentions"], reverse=True)
        
        self.processed_data["regions"] = region_data
        print(f"Generated Pakistan region data for {len(region_data)} regions")
    
    def _get_pakistan_region_code(self, region_name):
        """Convert Pakistani region name to code"""
        region_codes = {
            "Punjab": "PB",
            "Sindh": "SD",
            "KPK": "KP",
            "Balochistan": "BL",
            "Islamabad": "ISB",
            "Lahore": "LHR",
            "Karachi": "KHI"
        }
        return region_codes.get(region_name, region_name[:3].upper())

def main():
    print("=== Pakistan Sentiment Data Processor - 9th May 2023 ===")
    
    # Initialize processor for Pakistan incident
    processor = PakistanSentimentProcessor(incident_date="2023-05-09")
    
    # Process the data
    results = processor.process_pakistan_data()
    
    # Display results
    print("\n=== Pakistan Overview Results ===")
    overview = results['overview']
    print(f"Overall sentiment: {overview['overall']}% positive")
    print(f"Total mentions: {overview['totalMentions']:,}")
    print(f"Positive: {overview['positivePercentage']}%, Negative: {overview['negativePercentage']}%, Neutral: {overview['neutralPercentage']}%")
    print(f"Total engagement: {overview['engagement']:,}")
    print(f"Estimated reach: {overview['reachInMillions']}M people")
    print(f"Sentiment trend: {overview['trending']}")
    
    print("\n=== Pakistan Timeline (Key Days) ===")
    for day in results['timeline']:
        if "May 9" in day['date'] or "May 8" in day['date'] or "May 10" in day['date']:
            print(f"{day['date']}: Positive {day['positive']}%, Negative {day['negative']}%, Neutral {day['neutral']}%")
    
    print("\n=== Top Pakistan Political Terms ===")
    for word in results['wordcloud'][:10]:
        print(f"{word['text']}: {word['value']:,} mentions ({word['sentiment']} sentiment)")
    
    print("\n=== Pakistan Regional Sentiment ===")
    for region in results['regions'][:5]:
        print(f"{region['name']}: {region['sentiment']}% positive ({region['mentions']:,} mentions)")
    
    print("\n=== Pakistan Analysis Complete ===")

if __name__ == "__main__":
    main()
