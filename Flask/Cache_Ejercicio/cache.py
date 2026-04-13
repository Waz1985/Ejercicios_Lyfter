import json
import redis

from config import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD, CACHE_TTL_SECONDS


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    password=REDIS_PASSWORD,
    decode_responses=True
)


def get_cache(key):
    cached_value = redis_client.get(key)
    if cached_value is None:
        return None
    return json.loads(cached_value)


def set_cache(key, value, ttl=CACHE_TTL_SECONDS):
    redis_client.setex(key, ttl, json.dumps(value))


def delete_cache(key):
    redis_client.delete(key)


def product_cache_key(product_id):
    return f"products:{product_id}"


def products_list_cache_key():
    return "products:all"