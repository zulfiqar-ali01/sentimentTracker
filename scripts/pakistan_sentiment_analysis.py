import json
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from textblob import TextBlob

def simulate_pakistan_twitter_data(query="Imran Khan 9th May", count=1000, start_date="2023-05-07", days=7):
    """Simulate Twitter data for Pakistan 9th May 2023 incident"""
    print(f"Simulating Pakistan Twitter data for: {query}")
    print(f"Focusing on {start_date} to {days} days period")
    
    # Convert start_date string to datetime
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = start_datetime + timedelta(days=days)
    
    tweets = []
    
    # Pakistan-specific text fragments related to 9th May incident
    positive_fragments = [
        "support Imran Khan", "fighting for justice", "true leader", "standing with PTI",
        "democratic rights", "peaceful protest", "voice of people", "against corruption",
        "hope for Pakistan", "real change", "honest politician", "Pakistan Zindabad"
    ]
    
    negative_fragments = [
        "violence unacceptable", "extremist behavior", "destroying property", "law and order",
        "vandalism wrong", "chaos in streets", "damaging Pakistan", "terrorist activities",
        "attacking institutions", "mob mentality", "dangerous precedent", "anarchy"
    ]
    
    neutral_fragments = [
        "following developments", "situation in Pakistan", "9th May incident", 
        "political crisis", "need peaceful solution", "complex situation",
        "monitoring events", "awaiting more information", "political tensions"
    ]
    
    # Pakistani provinces and major cities with population weights
    pakistan_regions = {
        "Punjab": 0.53,      # Most populous province
        "Sindh": 0.23,       # Second most populous
        "KPK": 0.14,         # Khyber Pakhtunkhwa
        "Balochistan": 0.06, # Largest but least populous
        "Islamabad": 0.02,   # Capital territory
        "AJK": 0.02          # Azad Jammu Kashmir
    }
    
    # Sentiment distribution changes over time (May 9th was the peak of violence)
    def get_sentiment_weights(tweet_date):
        if tweet_date.day == 9:  # May 9th - day of incident
            return [0.25, 0.65, 0.10]  # More negative sentiment
        elif tweet_date.day in [10, 11]:  # Days after incident
            return [0.30, 0.55, 0.15]  # Still negative but improving
        else:  # Before and later days
            return [0.45, 0.40, 0.15]  # More balanced
    
    # Generate tweets
    for i in range(count):
        # Random date within range
        random_seconds = random.randint(0, int((end_datetime - start_datetime).total_seconds()))
        tweet_date = start_datetime + timedelta(seconds=random_seconds)
        
        # Get sentiment weights based on date
        sentiment_weights = get_sentiment_weights(tweet_date)
        
        # Randomly select sentiment
        sentiment_type = random.choices(
            ["positive", "negative", "neutral"], 
            weights=sentiment_weights, 
            k=1
        )[0]
        
        # Generate tweet text based on sentiment
        if sentiment_type == "positive":
            text = f"{random.choice(positive_fragments)} #ImranKhan #9thMay #Pakistan"
        elif sentiment_type == "negative":
            text = f"{random.choice(negative_fragments)} #9thMay #Violence #Pakistan"
        else:
            text = f"{random.choice(neutral_fragments)} #Pakistan #9thMay #Politics"
        
        # Random location (Pakistani regions)
        location = random.choices(
            list(pakistan_regions.keys()),
            weights=list(pakistan_regions.values()),
            k=1
        )[0]
        
        # Higher engagement on May 9th due to the incident
        engagement_multiplier = 3 if tweet_date.day == 9 else 1
        
        # Create tweet object
        tweet = {
            "id": i,
            "text": text,
            "created_at": tweet_date.isoformat(),
            "user_location": location,
            "retweet_count": random.randint(0, 500) * engagement_multiplier,
            "favorite_count": random.randint(0, 1000) * engagement_multiplier,
            "reply_count": random.randint(0, 100) * engagement_multiplier,
            "sentiment_type": sentiment_type
        }
        
        tweets.append(tweet)
    
    return tweets

def analyze_pakistan_sentiment(tweets):
    """Analyze sentiment with focus on Pakistan political context"""
    print("Analyzing sentiment for Pakistan political context...")
    
    # Keywords that indicate different sentiments in Pakistani political context
    positive_keywords = ["support", "justice", "leader", "democratic", "peaceful", "hope", "change"]
    negative_keywords = ["violence", "extremist", "vandalism", "chaos", "terrorist", "anarchy", "destroy"]
    
    for tweet in tweets:
        text_lower = tweet["text"].lower()
        
        # Count positive and negative keywords
        positive_count = sum(1 for keyword in positive_keywords if keyword in text_lower)
        negative_count = sum(1 for keyword in negative_keywords if keyword in text_lower)
        
        # Assign sentiment score based on keyword analysis and pre-assigned type
        if tweet["sentiment_type"] == "positive":
            base_score = random.uniform(0.3, 1.0)
            # Boost if contains positive keywords
            tweet["sentiment_score"] = min(1.0, base_score + (positive_count * 0.1))
        elif tweet["sentiment_type"] == "negative":
            base_score = random.uniform(-1.0, -0.3)
            # Make more negative if contains negative keywords
            tweet["sentiment_score"] = max(-1.0, base_score - (negative_count * 0.1))
        else:
            tweet["sentiment_score"] = random.uniform(-0.3, 0.3)
    
    return tweets

def generate_pakistan_timeline(tweets):
    """Generate timeline focusing on May 9th incident"""
    print("Generating Pakistan sentiment timeline...")
    
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
        
        # Format date
        date_obj = datetime.fromisoformat(day)
        display_date = date_obj.strftime("May %d")
        
        timeline_data.append({
            "date": display_date,
            "positive": round(positive / total * 100),
            "negative": round(negative / total * 100),
            "neutral": round(neutral / total * 100),
            "total_tweets": total
        })
    
    return timeline_data

def generate_pakistan_wordcloud(tweets):
    """Generate word cloud for Pakistan political context"""
    print("Generating Pakistan-specific word cloud...")
    
    # Extract and categorize words from tweets
    pakistan_political_words = {
        # Positive sentiment words
        "imrankhan": {"count": 0, "sentiment": "positive"},
        "pti": {"count": 0, "sentiment": "positive"},
        "justice": {"count": 0, "sentiment": "positive"},
        "democracy": {"count": 0, "sentiment": "positive"},
        "support": {"count": 0, "sentiment": "positive"},
        "leader": {"count": 0, "sentiment": "positive"},
        "change": {"count": 0, "sentiment": "positive"},
        "peaceful": {"count": 0, "sentiment": "positive"},
        "rights": {"count": 0, "sentiment": "positive"},
        
        # Negative sentiment words
        "violence": {"count": 0, "sentiment": "negative"},
        "extremism": {"count": 0, "sentiment": "negative"},
        "vandalism": {"count": 0, "sentiment": "negative"},
        "chaos": {"count": 0, "sentiment": "negative"},
        "arrest": {"count": 0, "sentiment": "negative"},
        "corruption": {"count": 0, "sentiment": "negative"},
        "anarchy": {"count": 0, "sentiment": "negative"},
        "destroy": {"count": 0, "sentiment": "negative"},
        
        # Neutral words
        "pakistan": {"count": 0, "sentiment": "neutral"},
        "9thmay": {"count": 0, "sentiment": "neutral"},
        "lahore": {"count": 0, "sentiment": "neutral"},
        "islamabad": {"count": 0, "sentiment": "neutral"},
        "karachi": {"count": 0, "sentiment": "neutral"},
        "politics": {"count": 0, "sentiment": "neutral"},
        "government": {"count": 0, "sentiment": "neutral"},
        "military": {"count": 0, "sentiment": "neutral"}
    }
    
    # Count word occurrences
    for tweet in tweets:
        text_lower = tweet["text"].lower().replace("#", "").replace("@", "")
        words = text_lower.split()
        
        for word in words:
            clean_word = ''.join(c for c in word if c.isalnum())
            if clean_word in pakistan_political_words:
                pakistan_political_words[clean_word]["count"] += 1
    
    # Convert to word cloud format
    wordcloud_data = []
    for word, data in pakistan_political_words.items():
        if data["count"] > 0:
            wordcloud_data.append({
                "text": word.title(),
                "value": data["count"],
                "sentiment": data["sentiment"]
            })
    
    # Sort by frequency
    wordcloud_data.sort(key=lambda x: x["value"], reverse=True)
    
    return wordcloud_data

def generate_pakistan_regions(tweets):
    """Generate region-based sentiment for Pakistani provinces"""
    print("Generating Pakistan regional sentiment data...")
    
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
        
        # Map to region codes
        region_code = get_pakistan_region_code(location)
        
        region_data.append({
            "id": region_code,
            "name": location,
            "sentiment": sentiment_score,
            "mentions": total
        })
    
    # Sort by number of mentions
    region_data.sort(key=lambda x: x["mentions"], reverse=True)
    
    return region_data

def get_pakistan_region_code(region_name):
    """Convert region name to code"""
    region_codes = {
        "Punjab": "PB",
        "Sindh": "SD",
        "KPK": "KP",
        "Balochistan": "BL",
        "Islamabad": "ISB",
        "AJK": "AJK"
    }
    return region_codes.get(region_name, region_name[:3].upper())

def visualize_pakistan_sentiment(tweets):
    """Create visualization specific to Pakistan incident"""
    sentiments = [tweet["sentiment_score"] for tweet in tweets]
    
    plt.figure(figsize=(12, 8))
    
    # Create subplot for sentiment distribution
    plt.subplot(2, 2, 1)
    plt.hist(sentiments, bins=20, color='lightcoral', edgecolor='black', alpha=0.7)
    plt.title('Sentiment Distribution - 9th May Pakistan Incident')
    plt.xlabel('Sentiment Score (-1 to 1)')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # Add statistics
    mean_sentiment = np.mean(sentiments)
    plt.axvline(mean_sentiment, color='red', linestyle='dashed', linewidth=2, 
                label=f'Mean: {mean_sentiment:.2f}')
    plt.legend()
    
    # Create timeline plot
    plt.subplot(2, 2, 2)
    timeline_data = generate_pakistan_timeline(tweets)
    dates = [d["date"] for d in timeline_data]
    positive_pct = [d["positive"] for d in timeline_data]
    negative_pct = [d["negative"] for d in timeline_data]
    
    plt.plot(dates, positive_pct, 'g-', label='Positive %', marker='o')
    plt.plot(dates, negative_pct, 'r-', label='Negative %', marker='s')
    plt.title('Sentiment Timeline')
    plt.xlabel('Date')
    plt.ylabel('Percentage')
    plt.legend()
    plt.xticks(rotation=45)
    
    # Regional sentiment
    plt.subplot(2, 2, 3)
    region_data = generate_pakistan_regions(tweets)
    regions = [r["name"] for r in region_data]
    region_sentiment = [r["sentiment"] for r in region_data]
    
    plt.bar(regions, region_sentiment, color='skyblue', edgecolor='navy')
    plt.title('Regional Sentiment Distribution')
    plt.xlabel('Province/Region')
    plt.ylabel('Positive Sentiment %')
    plt.xticks(rotation=45)
    
    # Word frequency
    plt.subplot(2, 2, 4)
    wordcloud_data = generate_pakistan_wordcloud(tweets)
    top_words = wordcloud_data[:10]
    words = [w["text"] for w in top_words]
    frequencies = [w["value"] for w in top_words]
    colors = ['green' if w["sentiment"] == 'positive' else 'red' if w["sentiment"] == 'negative' else 'gray' for w in top_words]
    
    plt.barh(words, frequencies, color=colors)
    plt.title('Top Words by Frequency')
    plt.xlabel('Frequency')
    
    plt.tight_layout()
    plt.show()

def main():
    print("=== Pakistan Social Media Sentiment Analysis - 9th May 2023 ===")
    
    # Generate data for the week around May 9th, 2023
    tweets = simulate_pakistan_twitter_data(
        query="Imran Khan 9th May violence",
        count=2000,
        start_date="2023-05-07",
        days=7
    )
    
    # Analyze sentiment
    analyzed_tweets = analyze_pakistan_sentiment(tweets)
    
    # Generate timeline
    timeline_data = generate_pakistan_timeline(analyzed_tweets)
    print("\n=== Sentiment Timeline ===")
    for day in timeline_data:
        print(f"{day['date']}: Positive {day['positive']}%, Negative {day['negative']}%, Neutral {day['neutral']}% ({day['total_tweets']} tweets)")
    
    # Generate word cloud data
    wordcloud_data = generate_pakistan_wordcloud(analyzed_tweets)
    print("\n=== Top Political Terms ===")
    for word in wordcloud_data[:15]:
        print(f"{word['text']}: {word['value']} mentions ({word['sentiment']} sentiment)")
    
    # Generate regional data
    region_data = generate_pakistan_regions(analyzed_tweets)
    print("\n=== Regional Sentiment ===")
    for region in region_data:
        print(f"{region['name']}: {region['sentiment']}% positive ({region['mentions']} mentions)")
    
    # Overall statistics
    total_tweets = len(analyzed_tweets)
    positive_tweets = len([t for t in analyzed_tweets if t["sentiment_type"] == "positive"])
    negative_tweets = len([t for t in analyzed_tweets if t["sentiment_type"] == "negative"])
    
    print(f"\n=== Overall Statistics ===")
    print(f"Total tweets analyzed: {total_tweets}")
    print(f"Positive sentiment: {positive_tweets/total_tweets*100:.1f}%")
    print(f"Negative sentiment: {negative_tweets/total_tweets*100:.1f}%")
    print(f"Average sentiment score: {np.mean([t['sentiment_score'] for t in analyzed_tweets]):.2f}")
    
    # Create visualizations
    try:
        visualize_pakistan_sentiment(analyzed_tweets)
    except Exception as e:
        print(f"Could not create visualization: {e}")
    
    print("\n=== Analysis Complete ===")

if __name__ == "__main__":
    main()
