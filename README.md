# genpark-social-proof-aggregator-skill

> **GenPark AI Agent Skill** -- Aggregate social proof signals into display-ready review widgets, trust badges, and featured reviews for product pages.

## Features

- Composite trust score (0-100) across rating, review volume, sales, repeat buyers, verified purchases
- Star display formatter and rating distribution calculator
- Trust badge generation: Top Rated, Best Seller, Community Favorite, Verified Purchases
- Featured review selection (highest rated + most helpful)
- Sentiment summary: positive / neutral / negative breakdown
- Flexible output: widget / badge / summary / all

## Quick Start

```python
from client import SocialProofClient

client = SocialProofClient()
result = client.aggregate(
    product_data={"total_reviews": 500, "avg_rating": 4.7, "units_sold": 2000, "repeat_buyers_pct": 55},
    reviews=[{"rating": 5, "text": "Love it!", "verified": True, "helpful_votes": 30}],
)
print(f"Trust Score: {result['trust_score']}")
print(f"Badges: {result['trust_badges']}")
```

## Installation

```bash
python example_usage.py  # No external dependencies
```

---
Built by [GenPark](https://genpark.ai) | [alphaparkinc](https://github.com/alphaparkinc)
