"""
Data Collection Module
Collects news articles from News API for training
"""

#FIRST CHECKNG IF THE API IS WORKING OR NOT 
import config
from newsapi import NewsApiClient

print("Checking API key...")
print(f"API Key exists: {config.NEWS_API_KEY is not None}")
print(f"API Key (first 10 chars): {config.NEWS_API_KEY[:10] if config.NEWS_API_KEY else 'NOT FOUND'}")

import pandas as pd
from newsapi import NewsApiClient
import time
from datetime import datetime, timedelta
import config
import os

class NewsDataCollector:
    def __init__(self, api_key=None):
        self.api_key = api_key or config.NEWS_API_KEY
        if not self.api_key:
            raise ValueError("NEWS_API_KEY not found. Check your .env file")
        
        self.newsapi = NewsApiClient(api_key=self.api_key)
        
    def collect_articles(self, topics=None, articles_per_topic=100, days_back=30):
        """
        Collect news articles from multiple topics
        
        Args:
            topics: List of topics to search
            articles_per_topic: Number of articles per topic
            days_back: How many days back to search
        
        Returns:
            DataFrame with collected articles
        """
        topics = topics or config.TOPICS
        all_articles = []
        
        # Calculate date range
        to_date = datetime.now()
        from_date = to_date - timedelta(days=days_back)
        
        print(f"Collecting articles from {from_date.date()} to {to_date.date()}")
        print(f"Topics: {topics}\n")
        
        for topic in topics:
            print(f"Fetching '{topic}'...", end=" ")
            
            try:
                # Fetch articles
                response = self.newsapi.get_everything(
                    q=topic,
                    language='en',
                    sort_by='relevancy',
                    page_size=min(articles_per_topic, 100),  # API limit
                    from_param=from_date.strftime('%Y-%m-%d'),
                    to=to_date.strftime('%Y-%m-%d')
                )
                
                articles = response.get('articles', [])
                
                # Process articles
                for article in articles:
                    # Combine title, description, and content
                    full_text = f"{article.get('title', '')} {article.get('description', '')} {article.get('content', '')}"
                    
                    all_articles.append({
                        'title': article.get('title', ''),
                        'description': article.get('description', ''),
                        'content': article.get('content', ''),
                        'full_text': full_text,
                        'url': article.get('url', ''),
                        'source': article.get('source', {}).get('name', ''),
                        'published_at': article.get('publishedAt', ''),
                        'topic': topic,
                        'collected_at': datetime.now().isoformat()
                    })
                
                print(f"✓ Got {len(articles)} articles")
                
                # Rate limiting - be nice to API
                time.sleep(1)
                
            except Exception as e:
                print(f"✗ Error: {str(e)}")
                continue
        
        # Create DataFrame
        df = pd.DataFrame(all_articles)
        
        print(f"\n{'='*50}")
        print(f"Total articles collected: {len(df)}")
        print(f"{'='*50}")
        
        return df
    
    def save_data(self, df, filename='raw_news_data.csv'):
        """Save collected data to CSV"""
        filepath = os.path.join(config.DATA_DIR, filename)
        df.to_csv(filepath, index=False)
        print(f"\n✓ Data saved to: {filepath}")
        return filepath

# Main execution
if __name__ == "__main__":
    print("="*50)
    print("NEWS DATA COLLECTOR")
    print("="*50 + "\n")
    
    # Create collector
    collector = NewsDataCollector()
    
    # Collect articles
    df = collector.collect_articles(
        topics=config.TOPICS,
        articles_per_topic=100,
        days_back=30
    )
    
    # Show summary
    print("\nData Summary:")
    print(df.info())
    print("\nArticles per topic:")
    print(df['topic'].value_counts())
    print("\nSample article:")
    print(df[['title', 'topic', 'source']].head())
    
    # Save
    collector.save_data(df)
    
    print("\n✓ Data collection complete!")