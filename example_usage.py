"""
example_usage.py -- Demonstrates the SocialProofClient SDK.
"""
from client import SocialProofClient

def main():
    client = SocialProofClient()

    product_data = {
        "total_reviews": 847,
        "avg_rating": 4.7,
        "units_sold": 3200,
        "repeat_buyers_pct": 62,
        "verified_purchase_pct": 91,
    }

    reviews = [
        {"rating": 5, "text": "Absolutely love this product! Amazing quality and fast delivery.", "verified": True, "helpful_votes": 45},
        {"rating": 5, "text": "Best purchase I made this year. Highly recommend!", "verified": True, "helpful_votes": 38},
        {"rating": 4, "text": "Great product overall. Packaging could be better but the product itself is fantastic.", "verified": True, "helpful_votes": 22},
        {"rating": 2, "text": "Arrived damaged. Disappointed with the packaging.", "verified": True, "helpful_votes": 8},
        {"rating": 5, "text": "Perfect! Exactly what I needed. Will buy again.", "verified": False, "helpful_votes": 15},
    ]

    print("[Social Proof Aggregator]")
    result = client.aggregate(product_data, reviews, display_format="all")

    print(f"Trust Score: {result['trust_score']}/100")
    w = result["widget"]
    print(f"\nWidget Data:")
    print(f"  Rating: {w['avg_rating']} {w['stars_display']} ({w['avg_rating_label']})")
    print(f"  Reviews: {w['total_reviews']:,} | Sold: {w['units_sold_display']}")
    print(f"  Repeat Buyers: {w['repeat_buyers_pct']}% | Verified: {w['verified_pct']}%")
    print(f"  Rating Distribution:")
    for d in w["rating_distribution"]:
        bar = "#" * int(d["pct"] / 5)
        print(f"    {d['stars']}* {bar:<20} {d['pct']}%")
    print(f"\nTrust Badges: {result['trust_badges']}")
    print(f"\nFeatured Reviews ({len(result['featured_reviews'])}):")
    for rev in result["featured_reviews"]:
        print(f"  [{rev['rating']}*] {str(rev['text'])[:60]}... ({rev['helpful_votes']} helpful)")
    print(f"\nSentiment: {result['sentiment_summary']}")

if __name__ == "__main__":
    main()
