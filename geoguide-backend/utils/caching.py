import redis
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Redis client
redis_client = redis.StrictRedis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    decode_responses=True
)

def cache_set(key, value, expiry=3600):
    """Stores data in Redis cache with an expiry time (default: 1 hour)."""
    redis_client.setex(key, expiry, value)

def cache_get(key):
    """Retrieves data from Redis cache."""
    return redis_client.get(key)

def cache_delete(key):
    """Deletes a cached item from Redis."""
    redis_client.delete(key)

def clear_cache():
    """Clears all cached data."""
    redis_client.flushdb()
