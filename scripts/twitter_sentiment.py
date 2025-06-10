import json
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from textblob import TextBlob

# This is a simulation script since we can't actually connect to Twitter API in this environment
# In a real application, you would use Tweepy to connect to the Twitter API

def simulate_twitter_data(query, count=100, days=7):
    """Simulate Twitter data for a given query"""
    print(f"Simulating Twitter data for query: {query}")
    
    # Generate random dates within the last N days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    tweets = []
    
    # Sample text fragments to create realistic-looking tweets
    positive_fragments = [
        "love this policy", "great initiative", "fully support", "excellent work",
        "promising results", "positive impact", "beneficial for everyone", "impressive progress"
    ]
    
    negative_fragments = [
        "terrible idea", "waste of resources", "strongly oppose", "disappointing results",
        "harmful policy", "negative consequences", "poorly implemented", "concerning development"
    ]
    
    neutral_fragments = [
        "need more information", "waiting to see results", "interesting approach", 
        "following developments", "complex issue", "requires further study"
    ]
    
    # Generate random tweets
    for i in range(count):
        # Randomly select sentiment
        sentiment_type = random.choices(
            ["positive", "negative", "neutral"], 
            weights=[0.6, 0.3, 0.1], 
            k=1
        )[0]
        
        # Generate tweet text based on sentiment
        if sentiment_type == "positive":
            text = f"{query} is {random.choice(positive_fragments)}. #{query.replace(' ', '')}"
        elif sentiment_type == "negative":
            text = f"{query} is {random.choice(negative_fragments)}. #{query.replace(' ', '')}"
        else:
            text = f"{query} is {random.choice(neutral_fragments)}. #{query.replace(' ', '')}"
        
        # Random date within range
        random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
        tweet_date = start_date + timedelta(seconds=random_seconds)
        
        # Random location (US states)
        states = ["CA", "TX", "FL", "NY", "PA", "IL", "OH", "GA", "NC", "MI"]
        location = random.choice(states)
        
        # Create tweet object
        tweet = {
            "id": i,
            "text": text,
            "created_at": tweet_date.isoformat(),
            "user_location": location,
            "retweet_count": random.randint(0, 1000),
            "favorite_count": random.randint(0, 2000),
            "sentiment_type": sentiment_type
        }
        
        tweets.append(tweet)
    
    return tweets

def analyze_sentiment(tweets):
    """Analyze sentiment of tweets using TextBlob"""
    print("Analyzing sentiment of tweets...")
    
    for tweet in tweets:
        # In a real app, we would use TextBlob to analyze sentiment
        # Here we're using the pre-assigned sentiment for simplicity
        if tweet["sentiment_type"] == "positive":
            tweet["sentiment_score"] = random.uniform(0.3, 1.0)
        elif tweet["sentiment_type"] == "negative":
            tweet["sentiment_score"] = random.uniform(-1.0, -0.3)
        else:
            tweet["sentiment_score"] = random.uniform(-0.3, 0.3)
    
    return tweets

def generate_sentiment_timeline(tweets):
    """Generate sentiment timeline data"""
    print("Generating sentiment timeline...")
    
    # Group tweets by day
    tweets_by_day = {}
    for tweet in tweets:
        day = tweet["created_at"].split("T")[0]
        if day not in tweets_by_day:
            tweets_by_day[day] = []
        tweets_by_day[day].append(tweet)
    
    # Calculate sentiment percentages for each day
    timeline_data = []
    for day, day_tweets in sorted(tweets_by_day.items()):
        positive = len([t for t in day_tweets if t["sentiment_type"] == "positive"])
        negative = len([t for t in day_tweets if t["sentiment_type"] == "negative"])
        neutral = len([t for t in day_tweets if t["sentiment_type"] == "neutral"])
        total = len(day_tweets)
        
        timeline_data.append({
            "date": day,
            "positive": round(positive / total * 100),
            "negative": round(negative / total * 100),
            "neutral": round(neutral / total * 100)
        })
    
    return timeline_data

def generate_wordcloud_data(tweets):
    """Generate word cloud data"""
    print("Generating word cloud data...")
    
    # Extract words from tweets
    all_words = []
    for tweet in tweets:
        # Remove hashtags and mentions
        text = tweet["text"].lower()
        words = text.split()
        
        for word in words:
            if len(word) > 3 and not word.startswith("#") and not word.startswith("@"):
                all_words.append({
                    "text": word,
                    "sentiment": tweet["sentiment_type"]
                })
    
    # Count word frequencies
    word_counts = {}
    for word_data in all_words:
        word = word_data["text"]
        sentiment = word_data["sentiment"]
        
        if word not in word_counts:
            word_counts[word] = {
                "count": 0,
                "sentiment_counts": {"positive": 0, "negative": 0, "neutral": 0}
            }
        
        word_counts[word]["count"] += 1
        word_counts[word]["sentiment_counts"][sentiment] += 1
    
    # Convert to format needed for word cloud
    wordcloud_data = []
    for word, data in word_counts.items():
        if data["count"] > 2:  # Filter out rare words
            # Determine dominant sentiment
            sentiments = data["sentiment_counts"]
            dominant_sentiment = max(sentiments, key=sentiments.get)
            
            wordcloud_data.append({
                "text": word,
                "value": data["count"],
                "sentiment": dominant_sentiment
            })
    
    # Sort by frequency
    wordcloud_data.sort(key=lambda x: x["value"], reverse=True)
    
    return wordcloud_data[:50]  # Return top 50 words

def generate_region_data(tweets):
    """Generate region-based sentiment data"""
    print("Generating region data...")
    
    # Group tweets by location
    tweets_by_location = {}
    for tweet in tweets:
        location = tweet["user_location"]
        if location not in tweets_by_location:
            tweets_by_location[location] = []
        tweets_by_location[location].append(tweet)
    
    # Calculate sentiment for each location
    region_data = []
    for location, location_tweets in tweets_by_location.items():
        positive = len([t for t in location_tweets if t["sentiment_type"] == "positive"])
        total = len(location_tweets)
        sentiment_score = round(positive / total * 100)
        
        region_data.append({
            "id": location,
            "name": get_state_name(location),
            "sentiment": sentiment_score,
            "mentions": total
        })
    
    # Sort by number of mentions
    region_data.sort(key=lambda x: x["mentions"], reverse=True)
    
    return region_data

def get_state_name(state_code):
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
        "MI": "Michigan"
    }
    return state_names.get(state_code, state_code)

def visualize_sentiment(tweets):
    """Create a simple visualization of sentiment distribution"""
    sentiments = [tweet["sentiment_score"] for tweet in tweets]
    
    plt.figure(figsize=(10, 6))
    plt.hist(sentiments, bins=20, color='skyblue', edgecolor='black')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment Score (-1 to 1)')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # Calculate statistics
    mean_sentiment = np.mean(sentiments)
    median_sentiment = np.median(sentiments)
    
    # Add vertical lines for mean and median
    plt.axvline(mean_sentiment, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_sentiment:.2f}')
    plt.axvline(median_sentiment, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median_sentiment:.2f}')
    
    plt.legend()
    plt.tight_layout()
    
    # In a real app, we would save this to a file
    # plt.savefig('sentiment_distribution.png')
    
    # For this demo, we'll just display the plot
    plt.show()

def main():
    query = "climate policy"  # Example query
    
    # Simulate Twitter data
    tweets = simulate_twitter_data(query, count=500)
    
    # Analyze sentiment
    analyzed_tweets = analyze_sentiment(tweets)
    
    # Generate timeline data
    timeline_data = generate_sentiment_timeline(analyzed_tweets)
    print("\nSentiment Timeline:")
    for day in timeline_data:
        print(f"{day['date']}: Positive {day['positive']}%, Negative {day['negative']}%, Neutral {day['neutral']}%")
    
    # Generate word cloud data
    wordcloud_data = generate_wordcloud_data(analyzed_tweets)
    print("\nTop Words:")
    for word in wordcloud_data[:10]:
        print(f"{word['text']}: {word['value']} mentions ({word['sentiment']})")
    
    # Generate region data
    region_data = generate_region_data(analyzed_tweets)
    print("\nRegion Sentiment:")
    for region in region_data:
        print(f"{region['name']}: {region['sentiment']}% positive ({region['mentions']} mentions)")
    
    # Visualize sentiment distribution
    try:
        visualize_sentiment(analyzed_tweets)
    except Exception as e:
        print(f"Could not create visualization: {e}")
    
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
