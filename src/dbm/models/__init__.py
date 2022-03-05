from dbm.models import price_tracking_system, token_discovery_system

class tables():
    # Discovery System
    crypto_tracking_platform = token_discovery_system.CryptoTrackingPlatform
    scraped_token = token_discovery_system.ScrapedToken
    raw_token_to_review = token_discovery_system.RawTokenToReview
    
    # Tracking System
    price_tracked_tokens = price_tracking_system.PriceTrackedTokens
    price_tracking_platforms = price_tracking_system.PriceTrackingPlatforms