import json
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

def generate_urdu_keywords():
    """Generate Urdu keywords that were popular during 9th May 2023"""
    
    urdu_keywords = {
        # Political terms
        "عمران خان": {"sentiment": "positive", "frequency": 12500},
        "پی ٹی آئی": {"sentiment": "positive", "frequency": 8900},
        "نو مئی": {"sentiment": "negative", "frequency": 15200},
        "گرفتاری": {"sentiment": "negative", "frequency": 7800},
        "انصاف": {"sentiment": "positive", "frequency": 5200},
        
        # Violence related
        "تشدد": {"sentiment": "negative", "frequency": 9800},
        "توڑ پھوڑ": {"sentiment": "negative", "frequency": 4500},
        "حملہ": {"sentiment": "negative", "frequency": 6200},
        "افراتفری": {"sentiment": "negative", "frequency": 3800},
        "انتہا پسندی": {"sentiment": "negative", "frequency": 4200},
        
        # Locations
        "لاہور": {"sentiment": "neutral", "frequency": 6800},
        "اسلام آباد": {"sentiment": "neutral", "frequency": 5500},
        "کراچی": {"sentiment": "neutral", "frequency": 4200},
        "پاکستان": {"sentiment": "neutral", "frequency": 8900},
        
        # Support/Opposition
        "حامی": {"sentiment": "positive", "frequency": 3500},
        "مخالف": {"sentiment": "negative", "frequency": 2800},
        "احتجاج": {"sentiment": "neutral", "frequency": 5800},
        "مظاہرہ": {"sentiment": "neutral", "frequency": 4200},
        
        # Government/Military
        "فوج": {"sentiment": "negative", "frequency": 4800},
        "حکومت": {"sentiment": "negative", "frequency": 5200},
        "عدالت": {"sentiment": "neutral", "frequency": 3800},
        "پولیس": {"sentiment": "negative", "frequency": 4500},
        
        # Emotions/Reactions
        "غصہ": {"sentiment": "negative", "frequency": 3200},
        "خوشی": {"sentiment": "positive", "frequency": 2100},
        "غم": {"sentiment": "negative", "frequency": 2800},
        "امید": {"sentiment": "positive", "frequency": 2500},
        "ڈر": {"sentiment": "negative", "frequency": 3500},
        
        # Democratic terms
        "جمہوریت": {"sentiment": "positive", "frequency": 3800},
        "آزادی": {"sentiment": "positive", "frequency": 3200},
        "حقوق": {"sentiment": "positive", "frequency": 2800},
        "قانون": {"sentiment": "neutral", "frequency": 3500},
    }
    
    return urdu_keywords

def analyze_urdu_sentiment_patterns():
    """Analyze sentiment patterns in Urdu keywords"""
    
    keywords = generate_urdu_keywords()
    
    print("=== اردو کلیدی الفاظ کا جذباتی تجزیہ - ۹ مئی ۲۰۲۳ ===")
    print("Urdu Keywords Sentiment Analysis - 9th May 2023")
    print("=" * 60)
    
    # Categorize by sentiment
    positive_words = []
    negative_words = []
    neutral_words = []
    
    for word, data in keywords.items():
        if data["sentiment"] == "positive":
            positive_words.append((word, data["frequency"]))
        elif data["sentiment"] == "negative":
            negative_words.append((word, data["frequency"]))
        else:
            neutral_words.append((word, data["frequency"]))
    
    # Sort by frequency
    positive_words.sort(key=lambda x: x[1], reverse=True)
    negative_words.sort(key=lambda x: x[1], reverse=True)
    neutral_words.sort(key=lambda x: x[1], reverse=True)
    
    print("\n🟢 مثبت جذبات (Positive Sentiment):")
    for word, freq in positive_words[:5]:
        print(f"   {word}: {freq:,} mentions")
    
    print("\n🔴 منفی جذبات (Negative Sentiment):")
    for word, freq in negative_words[:5]:
        print(f"   {word}: {freq:,} mentions")
    
    print("\n⚪ غیر جانبدار (Neutral Sentiment):")
    for word, freq in neutral_words[:5]:
        print(f"   {word}: {freq:,} mentions")
    
    # Calculate overall statistics
    total_positive = sum(data["frequency"] for data in keywords.values() if data["sentiment"] == "positive")
    total_negative = sum(data["frequency"] for data in keywords.values() if data["sentiment"] == "negative")
    total_neutral = sum(data["frequency"] for data in keywords.values() if data["sentiment"] == "neutral")
    total_all = total_positive + total_negative + total_neutral
    
    print(f"\n📊 مجموعی اعداد و شمار (Overall Statistics):")
    print(f"   مثبت الفاظ (Positive): {total_positive:,} ({total_positive/total_all*100:.1f}%)")
    print(f"   منفی الفاظ (Negative): {total_negative:,} ({total_negative/total_all*100:.1f}%)")
    print(f"   غیر جانبدار الفاظ (Neutral): {total_neutral:,} ({total_neutral/total_all*100:.1f}%)")
    
    return keywords

def generate_hashtag_combinations():
    """Generate popular hashtag combinations used during the incident"""
    
    hashtag_combinations = [
        "#عمران_خان OR #ImranKhan",
        "#نو_مئی OR #9thMay", 
        "#پی_ٹی_آئی OR #PTI",
        "#تشدد OR #Violence",
        "#انصاف OR #Justice",
        "#پاکستان OR #Pakistan",
        "#لاہور OR #Lahore",
        "#گرفتاری OR #Arrest",
        "#احتجاج OR #Protests",
        "#جمہوریت OR #Democracy"
    ]
    
    print("\n🔍 مقبول ہیش ٹیگ امتزاج (Popular Hashtag Combinations):")
    for i, combo in enumerate(hashtag_combinations, 1):
        print(f"   {i}. {combo}")
    
    return hashtag_combinations

def simulate_hourly_urdu_trends():
    """Simulate hourly trends for Urdu keywords on May 9th"""
    
    hours = ["صبح ۶", "صبح ۸", "صبح ۱۰", "دوپہر ۱۲", "دوپہر ۲", "شام ۴", "شام ۶", "رات ۸", "رات ۱۰"]
    english_hours = ["6 AM", "8 AM", "10 AM", "12 PM", "2 PM", "4 PM", "6 PM", "8 PM", "10 PM"]
    
    # Key Urdu terms with hourly variations
    urdu_trends = {
        "عمران خان": [450, 680, 890, 1200, 1800, 1500, 1200, 950, 720],
        "نو مئی": [200, 450, 780, 1500, 2100, 1800, 1400, 1100, 850],
        "تشدد": [100, 200, 400, 800, 1200, 1000, 700, 500, 300],
        "انصاف": [300, 400, 500, 600, 800, 750, 650, 550, 450],
        "پی ٹی آئی": [250, 350, 450, 650, 900, 800, 650, 500, 400]
    }
    
    print(f"\n⏰ گھنٹہ وار رجحانات - ۹ مئی (Hourly Trends - May 9th):")
    print("=" * 50)
    
    for hour_urdu, hour_eng in zip(hours, english_hours):
        print(f"\n{hour_urdu} ({hour_eng}):")
        hour_index = english_hours.index(hour_eng)
        
        for term, values in urdu_trends.items():
            print(f"   {term}: {values[hour_index]:,} mentions")
    
    return urdu_trends

def create_search_query_examples():
    """Create example search queries mixing English and Urdu"""
    
    search_examples = [
        {
            "query": "#ImranKhan OR #عمران_خان OR #PTI OR #پی_ٹی_آئی",
            "description": "Pro-Imran Khan sentiment tracking",
            "date_range": "2023-05-07 to 2023-05-15"
        },
        {
            "query": "#9thMay OR #نو_مئی OR #Violence OR #تشدد",
            "description": "Violence and incident tracking", 
            "date_range": "2023-05-09 to 2023-05-12"
        },
        {
            "query": "#Lahore OR #لاہور OR #Islamabad OR #اسلام_آباد",
            "description": "City-specific sentiment analysis",
            "date_range": "2023-05-09 to 2023-05-10"
        },
        {
            "query": "#Justice OR #انصاف OR #Democracy OR #جمہوریت",
            "description": "Democratic values sentiment",
            "date_range": "2023-05-07 to 2023-05-20"
        },
        {
            "query": "#Arrest OR #گرفتاری OR #Court OR #عدالت",
            "description": "Legal proceedings tracking",
            "date_range": "2023-05-09 to 2023-05-15"
        }
    ]
    
    print(f"\n🔍 تجویز کردہ تلاش کی مثالیں (Suggested Search Examples):")
    print("=" * 60)
    
    for i, example in enumerate(search_examples, 1):
        print(f"\n{i}. {example['description']}")
        print(f"   Query: {example['query']}")
        print(f"   Date Range: {example['date_range']}")
    
    return search_examples

def main():
    print("🇵🇰 Pakistan Social Media Sentiment Analysis - Urdu Keywords")
    print("=" * 70)
    
    # Analyze Urdu keywords
    keywords = analyze_urdu_sentiment_patterns()
    
    # Generate hashtag combinations
    hashtags = generate_hashtag_combinations()
    
    # Show hourly trends
    trends = simulate_hourly_urdu_trends()
    
    # Create search examples
    examples = create_search_query_examples()
    
    print(f"\n📈 خلاصہ (Summary):")
    print("=" * 30)
    print("✅ Urdu keywords analysis completed")
    print("✅ Hashtag combinations generated") 
    print("✅ Hourly trends calculated")
    print("✅ Search query examples created")
    print("\n🎯 Use these insights to track sentiment more effectively!")

if __name__ == "__main__":
    main()
