# 💡 Sentimeter Examples

This document provides practical examples of how to use Sentimeter for different scenarios.

## 📝 Basic Text Analysis Examples

### Example 1: Customer Review Analysis

**Input Text:**
```
"I absolutely love this new smartphone! The camera quality is outstanding, 
the battery life is impressive, and the user interface is so intuitive. 
Highly recommended!"
```

**Expected Output:**
- **Sentiment**: Positive
- **Confidence**: 95%
- **Key Positive Words**: love, outstanding, impressive, highly recommended
- **Summary**: Strong positive sentiment with multiple positive indicators

### Example 2: Mixed Sentiment Analysis

**Input Text:**
```
"The product design is beautiful and the shipping was fast, but unfortunately 
the build quality seems poor and I'm having connectivity issues."
```

**Expected Output:**
- **Sentiment**: Mixed/Negative
- **Confidence**: 75%
- **Positive Aspects**: beautiful design, fast shipping
- **Negative Aspects**: poor build quality, connectivity issues
- **Summary**: Mixed sentiment with significant negative concerns

### Example 3: Neutral Text Analysis

**Input Text:**
```
"The package arrived on Tuesday. It contains one blue shirt, size medium, 
made of 100% cotton. The receipt is included in the box."
```

**Expected Output:**
- **Sentiment**: Neutral
- **Confidence**: 88%
- **Summary**: Factual information without emotional indicators

## 🔄 API Usage Examples

### Single Text Analysis (cURL)

```bash
curl -X POST https://api.sentimeter.com/v1/analyze \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "This restaurant exceeded my expectations! Amazing food and service.",
    "options": {
      "language": "en",
      "detailed": true
    }
  }'
```

### Batch Analysis (JavaScript)

```javascript
const axios = require('axios');

const analyzeReviews = async () => {
  const reviews = [
    { id: "rev_1", text: "Great product, fast delivery!" },
    { id: "rev_2", text: "Quality could be better for the price" },
    { id: "rev_3", text: "Exactly what I ordered, arrived on time" }
  ];

  try {
    const response = await axios.post('https://api.sentimeter.com/v1/analyze/batch', {
      texts: reviews,
      options: { detailed: false }
    }, {
      headers: {
        'Authorization': 'Bearer YOUR_API_KEY',
        'Content-Type': 'application/json'
      }
    });

    console.log('Batch Analysis Results:', response.data);
  } catch (error) {
    console.error('Error:', error.response.data);
  }
};

analyzeReviews();
```

### Python Integration

```python
import requests
import json

class SentimentAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.sentimeter.com/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def analyze_text(self, text, language="auto"):
        payload = {
            "text": text,
            "options": {
                "language": language,
                "detailed": True
            }
        }
        
        response = requests.post(
            f"{self.base_url}/analyze",
            headers=self.headers,
            json=payload
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API Error: {response.status_code}")

# Usage
analyzer = SentimentAnalyzer("YOUR_API_KEY")
result = analyzer.analyze_text("I'm thrilled with this purchase!")
print(f"Sentiment: {result['sentiment']}")
print(f"Confidence: {result['confidence']}")
```

## 🎯 Real-World Use Cases

### Use Case 1: E-commerce Review Monitoring

**Scenario**: Monitor product reviews in real-time to identify dissatisfied customers

```python
def monitor_reviews():
    analyzer = SentimentAnalyzer("YOUR_API_KEY")
    
    # Simulate new review
    new_review = "This product broke after just one week. Very disappointed!"
    
    result = analyzer.analyze_text(new_review)
    
    if result['sentiment'] == 'negative' and result['confidence'] > 0.8:
        # Alert customer service team
        send_alert({
            'review_text': new_review,
            'sentiment_score': result['confidence'],
            'action_required': 'Contact customer immediately'
        })
        
    return result
```

### Use Case 2: Social Media Brand Monitoring

**Scenario**: Track mentions of your brand on social media

```javascript
const monitorBrandMentions = async (mentions) => {
  const results = [];
  
  for (const mention of mentions) {
    const analysis = await fetch('https://api.sentimeter.com/v1/analyze', {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer YOUR_API_KEY',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        text: mention.text,
        options: { language: 'auto' }
      })
    });
    
    const sentiment = await analysis.json();
    
    results.push({
      platform: mention.platform,
      user: mention.user,
      text: mention.text,
      sentiment: sentiment.sentiment,
      confidence: sentiment.confidence,
      timestamp: mention.timestamp
    });
  }
  
  // Generate brand sentiment report
  return generateBrandReport(results);
};
```

### Use Case 3: Customer Support Ticket Prioritization

**Scenario**: Automatically prioritize support tickets based on sentiment

```python
def prioritize_support_tickets(tickets):
    analyzer = SentimentAnalyzer("YOUR_API_KEY")
    prioritized_tickets = []
    
    for ticket in tickets:
        # Analyze ticket content
        sentiment_result = analyzer.analyze_text(ticket['description'])
        
        # Calculate priority score
        priority_score = calculate_priority(
            sentiment=sentiment_result['sentiment'],
            confidence=sentiment_result['confidence'],
            customer_tier=ticket['customer_tier']
        )
        
        ticket['priority_score'] = priority_score
        ticket['sentiment_analysis'] = sentiment_result
        prioritized_tickets.append(ticket)
    
    # Sort by priority (highest first)
    return sorted(prioritized_tickets, 
                 key=lambda x: x['priority_score'], 
                 reverse=True)

def calculate_priority(sentiment, confidence, customer_tier):
    base_score = 50
    
    # Negative sentiment increases priority
    if sentiment == 'negative':
        base_score += confidence * 40
    elif sentiment == 'positive':
        base_score -= confidence * 10
    
    # VIP customers get higher priority
    if customer_tier == 'VIP':
        base_score += 30
    elif customer_tier == 'Premium':
        base_score += 15
    
    return min(base_score, 100)  # Cap at 100
```

## 📊 Data Visualization Examples

### Creating Sentiment Charts

```python
import matplotlib.pyplot as plt
import pandas as pd

def create_sentiment_chart(analysis_results):
    # Extract data
    sentiments = [result['sentiment'] for result in analysis_results]
    confidences = [result['confidence'] for result in analysis_results]
    
    # Create DataFrame
    df = pd.DataFrame({
        'sentiment': sentiments,
        'confidence': confidences
    })
    
    # Create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Sentiment distribution
    sentiment_counts = df['sentiment'].value_counts()
    ax1.pie(sentiment_counts.values, labels=sentiment_counts.index, autopct='%1.1f%%')
    ax1.set_title('Sentiment Distribution')
    
    # Confidence distribution
    ax2.hist(df['confidence'], bins=20, alpha=0.7)
    ax2.set_xlabel('Confidence Score')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Confidence Distribution')
    
    plt.tight_layout()
    plt.show()
```

### Real-time Dashboard

```javascript
// Real-time sentiment dashboard using Chart.js
class SentimentDashboard {
    constructor(apiKey) {
        this.apiKey = apiKey;
        this.sentimentData = {
            positive: 0,
            negative: 0,
            neutral: 0
        };
        this.initChart();
    }
    
    async analyzeBatch(texts) {
        const response = await fetch('https://api.sentimeter.com/v1/analyze/batch', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${this.apiKey}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                texts: texts.map((text, index) => ({ id: index, text }))
            })
        });
        
        const results = await response.json();
        this.updateChart(results.results);
    }
    
    updateChart(results) {
        // Reset counters
        this.sentimentData = { positive: 0, negative: 0, neutral: 0 };
        
        // Count sentiments
        results.forEach(result => {
            this.sentimentData[result.sentiment]++;
        });
        
        // Update chart
        this.chart.data.datasets[0].data = [
            this.sentimentData.positive,
            this.sentimentData.negative,
            this.sentimentData.neutral
        ];
        this.chart.update();
    }
    
    initChart() {
        const ctx = document.getElementById('sentimentChart').getContext('2d');
        this.chart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Positive', 'Negative', 'Neutral'],
                datasets: [{
                    data: [0, 0, 0],
                    backgroundColor: ['#4CAF50', '#F44336', '#9E9E9E']
                }]
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Real-time Sentiment Analysis'
                }
            }
        });
    }
}
```

## 🔧 Integration Patterns

### Webhook Integration

```python
from flask import Flask, request, jsonify
import hmac
import hashlib

app = Flask(__name__)
WEBHOOK_SECRET = "your_webhook_secret"

@app.route('/webhook/sentiment', methods=['POST'])
def handle_sentiment_webhook():
    # Verify webhook signature
    signature = request.headers.get('X-Sentimeter-Signature')
    if not verify_webhook_signature(request.data, signature):
        return jsonify({'error': 'Invalid signature'}), 401
    
    # Process sentiment data
    data = request.json
    
    if data['event'] == 'analysis.completed':
        result = data['data']
        
        # Take action based on sentiment
        if result['sentiment'] == 'negative' and result['confidence'] > 0.8:
            trigger_alert(result)
        elif result['sentiment'] == 'positive' and result['confidence'] > 0.9:
            trigger_positive_action(result)
    
    return jsonify({'status': 'processed'})

def verify_webhook_signature(payload, signature):
    expected_signature = hmac.new(
        WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(f"sha256={expected_signature}", signature)
```

### Stream Processing

```python
import asyncio
import websockets
import json

async def stream_sentiment_analysis():
    uri = "wss://api.sentimeter.com/v1/stream"
    
    async with websockets.connect(uri) as websocket:
        # Authenticate
        await websocket.send(json.dumps({
            'type': 'auth',
            'token': 'YOUR_API_KEY'
        }))
        
        # Stream text for analysis
        texts_to_analyze = [
            "This is amazing!",
            "Not what I expected...",
            "Pretty good overall"
        ]
        
        for text in texts_to_analyze:
            await websocket.send(json.dumps({
                'type': 'analyze',
                'text': text
            }))
            
            # Receive result
            response = await websocket.recv()
            result = json.loads(response)
            print(f"Text: '{text}' -> {result['sentiment']} ({result['confidence']:.2f})")

# Run the stream
asyncio.run(stream_sentiment_analysis())
```

## 🚨 Error Handling Examples

### Robust Error Handling

```python
import time
import random
from typing import Optional, Dict, Any

class SentimeterClient:
    def __init__(self, api_key: str, max_retries: int = 3):
        self.api_key = api_key
        self.max_retries = max_retries
        self.base_url = "https://api.sentimeter.com/v1"
    
    def analyze_with_retry(self, text: str) -> Optional[Dict[Any, Any]]:
        for attempt in range(self.max_retries):
            try:
                result = self._make_request(text)
                return result
                
            except RateLimitError:
                if attempt < self.max_retries - 1:
                    wait_time = (2 ** attempt) + random.uniform(0, 1)
                    print(f"Rate limit hit, waiting {wait_time:.2f} seconds...")
                    time.sleep(wait_time)
                else:
                    raise
                    
            except TemporaryError:
                if attempt < self.max_retries - 1:
                    wait_time = (2 ** attempt)
                    print(f"Temporary error, retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    raise
                    
            except PermanentError:
                # Don't retry permanent errors
                raise
        
        return None
    
    def _make_request(self, text: str) -> Dict[Any, Any]:
        # Simulated API request logic
        # In real implementation, use requests library
        pass

# Custom exceptions
class SentimeterError(Exception):
    pass

class RateLimitError(SentimeterError):
    pass

class TemporaryError(SentimeterError):
    pass

class PermanentError(SentimeterError):
    pass
```

---

These examples should help you get started with Sentimeter! For more detailed information, check out our [User Manual](../USER_MANUAL.md) and [API Documentation](../API_DOCUMENTATION.md).

**Happy sentiment analyzing! 🎉**