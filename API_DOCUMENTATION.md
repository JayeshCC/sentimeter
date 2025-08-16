# 🔧 Sentimeter API Documentation

## Overview

The Sentimeter API provides programmatic access to our sentiment analysis capabilities. This RESTful API allows you to integrate sentiment analysis into your applications, websites, or data processing pipelines.

## Base URL

```
https://api.sentimeter.com/v1
```

## Authentication

All API requests require authentication using an API key:

```http
Authorization: Bearer YOUR_API_KEY
```

To get an API key, sign up at [Sentimeter Dashboard](https://dashboard.sentimeter.com).

## Rate Limits

- **Free Tier**: 1,000 requests per day
- **Pro Tier**: 10,000 requests per day
- **Enterprise**: Custom limits

Rate limit headers are included in all responses:
- `X-RateLimit-Limit`: Total requests allowed
- `X-RateLimit-Remaining`: Requests remaining
- `X-RateLimit-Reset`: Unix timestamp when limit resets

## Endpoints

### 1. Analyze Single Text

Analyze sentiment for a single piece of text.

```http
POST /analyze
```

#### Request Body

```json
{
  "text": "string (required)",
  "options": {
    "language": "string (optional, default: 'auto')",
    "detailed": "boolean (optional, default: true)",
    "threshold": "number (optional, default: 0.5)"
  }
}
```

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `text` | string | The text to analyze (max 10,000 characters) |
| `language` | string | Language code ('en', 'es', 'fr', etc.) or 'auto' |
| `detailed` | boolean | Include detailed breakdown in response |
| `threshold` | number | Confidence threshold (0.0 - 1.0) |

#### Response

```json
{
  "id": "analysis_12345",
  "text": "I love this product!",
  "sentiment": "positive",
  "confidence": 0.92,
  "scores": {
    "positive": 0.92,
    "negative": 0.05,
    "neutral": 0.03
  },
  "language": "en",
  "processing_time_ms": 45,
  "detailed": {
    "keywords": ["love", "product"],
    "phrases": [
      {
        "text": "love this product",
        "sentiment": "positive",
        "confidence": 0.95
      }
    ],
    "entities": [],
    "emotions": {
      "joy": 0.85,
      "anger": 0.02,
      "sadness": 0.01,
      "fear": 0.01,
      "surprise": 0.11
    }
  },
  "metadata": {
    "character_count": 19,
    "word_count": 4,
    "sentence_count": 1
  }
}
```

#### Example Request

```bash
curl -X POST https://api.sentimeter.com/v1/analyze \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "I love this product!",
    "options": {
      "language": "en",
      "detailed": true
    }
  }'
```

### 2. Batch Analysis

Analyze multiple texts in a single request.

```http
POST /analyze/batch
```

#### Request Body

```json
{
  "texts": [
    {
      "id": "review_1",
      "text": "Great product!"
    },
    {
      "id": "review_2", 
      "text": "Could be better"
    }
  ],
  "options": {
    "language": "auto",
    "detailed": false
  }
}
```

#### Response

```json
{
  "results": [
    {
      "id": "review_1",
      "text": "Great product!",
      "sentiment": "positive",
      "confidence": 0.88,
      "scores": {
        "positive": 0.88,
        "negative": 0.07,
        "neutral": 0.05
      }
    },
    {
      "id": "review_2",
      "text": "Could be better",
      "sentiment": "negative",
      "confidence": 0.65,
      "scores": {
        "positive": 0.20,
        "negative": 0.65,
        "neutral": 0.15
      }
    }
  ],
  "summary": {
    "total_analyzed": 2,
    "positive_count": 1,
    "negative_count": 1,
    "neutral_count": 0,
    "average_confidence": 0.765
  },
  "processing_time_ms": 78
}
```

### 3. Real-time Stream Analysis

Analyze text in real-time using WebSocket connection.

```javascript
const ws = new WebSocket('wss://api.sentimeter.com/v1/stream');

ws.onopen = function() {
  ws.send(JSON.stringify({
    type: 'auth',
    token: 'YOUR_API_KEY'
  }));
};

ws.onmessage = function(event) {
  const data = JSON.parse(event.data);
  console.log('Sentiment result:', data);
};

// Send text for analysis
ws.send(JSON.stringify({
  type: 'analyze',
  text: 'This is amazing!'
}));
```

### 4. Get Analysis History

Retrieve previously analyzed texts.

```http
GET /history?limit=10&offset=0&sentiment=positive
```

#### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `limit` | number | Number of results (max 100, default 10) |
| `offset` | number | Pagination offset (default 0) |
| `sentiment` | string | Filter by sentiment ('positive', 'negative', 'neutral') |
| `from_date` | string | Start date (ISO 8601 format) |
| `to_date` | string | End date (ISO 8601 format) |

### 5. Account Information

Get account details and usage statistics.

```http
GET /account
```

#### Response

```json
{
  "user_id": "user_12345",
  "plan": "pro",
  "api_calls_today": 856,
  "api_calls_limit": 10000,
  "total_api_calls": 25430,
  "account_created": "2024-01-15T09:30:00Z",
  "last_activity": "2024-01-20T14:22:33Z"
}
```

## Data Flow Diagram

![API Data Flow](https://github.com/user-attachments/assets/1bf9c4ad-af20-44c3-9386-ba8a425c3ea5)

The diagram above shows how data flows through the Sentimeter API:

1. **Client Request** - Your application sends text to analyze
2. **Authentication** - API key is validated
3. **Text Processing** - Text is preprocessed and cleaned
4. **ML Analysis** - Machine learning models analyze sentiment
5. **Response** - Results are returned to your application

## Error Handling

The API uses standard HTTP status codes:

### Common Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Request successful |
| 400 | Bad Request | Invalid request parameters |
| 401 | Unauthorized | Invalid or missing API key |
| 403 | Forbidden | API key doesn't have required permissions |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error occurred |

### Error Response Format

```json
{
  "error": {
    "code": "INVALID_TEXT",
    "message": "Text cannot be empty",
    "details": {
      "parameter": "text",
      "provided": "",
      "expected": "non-empty string"
    }
  },
  "request_id": "req_12345"
}
```

### Common Error Codes

| Code | Description |
|------|-------------|
| `INVALID_API_KEY` | API key is invalid or expired |
| `RATE_LIMIT_EXCEEDED` | Too many requests in time window |
| `TEXT_TOO_LONG` | Text exceeds maximum length |
| `INVALID_LANGUAGE` | Unsupported language code |
| `PROCESSING_ERROR` | Error during sentiment analysis |

## SDK Examples

### JavaScript/Node.js

```javascript
const Sentimeter = require('sentimeter-sdk');

const client = new Sentimeter('YOUR_API_KEY');

// Analyze single text
const result = await client.analyze({
  text: 'I love this product!',
  options: { detailed: true }
});

console.log(result.sentiment); // 'positive'
console.log(result.confidence); // 0.92
```

### Python

```python
from sentimeter import SentimeterClient

client = SentimeterClient(api_key='YOUR_API_KEY')

# Analyze single text
result = client.analyze(
    text='I love this product!',
    options={'detailed': True}
)

print(result.sentiment)  # 'positive'
print(result.confidence)  # 0.92
```

### cURL

```bash
# Analyze text
curl -X POST https://api.sentimeter.com/v1/analyze \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product!"}'
```

## Webhooks

Set up webhooks to receive sentiment analysis results asynchronously.

### Configuration

```http
POST /webhooks
```

```json
{
  "url": "https://your-app.com/webhook",
  "events": ["analysis.completed", "batch.completed"],
  "secret": "your_webhook_secret"
}
```

### Webhook Payload

```json
{
  "event": "analysis.completed",
  "timestamp": "2024-01-20T14:22:33Z",
  "data": {
    "id": "analysis_12345",
    "text": "Sample text",
    "sentiment": "positive",
    "confidence": 0.85
  },
  "signature": "sha256=..."
}
```

## Best Practices

### Performance Optimization

1. **Batch Processing** - Use batch endpoint for multiple texts
2. **Caching** - Cache results for identical texts
3. **Language Detection** - Specify language when known
4. **Connection Pooling** - Reuse HTTP connections

### Accuracy Tips

1. **Text Preprocessing** - Clean text before analysis
2. **Context** - Provide sufficient context for short texts
3. **Language** - Specify correct language for best results
4. **Validation** - Validate critical results manually

### Security

1. **API Key Protection** - Never expose API keys in client-side code
2. **HTTPS** - Always use HTTPS for requests
3. **Rate Limiting** - Implement client-side rate limiting
4. **Webhook Verification** - Verify webhook signatures

## Support

- **Documentation**: [https://docs.sentimeter.com](https://docs.sentimeter.com)
- **Status Page**: [https://status.sentimeter.com](https://status.sentimeter.com)
- **Support Email**: api-support@sentimeter.com
- **GitHub Issues**: [https://github.com/JayeshCC/sentimeter/issues](https://github.com/JayeshCC/sentimeter/issues)

## Changelog

### v1.2.0 (2024-01-20)
- Added emotion detection in detailed analysis
- Improved accuracy for short texts
- Added streaming endpoint

### v1.1.0 (2024-01-15)
- Added batch processing endpoint
- Improved language detection
- Added webhook support

### v1.0.0 (2024-01-01)
- Initial API release
- Basic sentiment analysis
- Multi-language support

---

**Ready to start analyzing sentiment? Get your API key at [Sentimeter Dashboard](https://dashboard.sentimeter.com)!**