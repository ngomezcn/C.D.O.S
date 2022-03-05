from dbm.models import discovery_system, tracking_system

class table():
    # Discovery System
    crypto_tracking_platform = discovery_system.CryptoTrackingPlatform
    scraped_token = discovery_system.ScrapedToken
    raw_token_to_review = discovery_system.RawTokenToReview
    
    # Tracking System
    price_tracked_tokens = tracking_system.PriceTrackedTokens