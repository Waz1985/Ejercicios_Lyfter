import json
import redis


class CacheManager:
    def __init__(self, host, port, password=None, *args, **kwargs):
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            password=password,
            *args,
            **kwargs,
        )

        connection_status = self.redis_client.ping()
        if connection_status:
            print("Redis connection created successfully")

    def store_data(self, key, value, time_to_live=None):
        try:
            if isinstance(value, (dict, list)):
                value = json.dumps(value)

            if time_to_live is None:
                self.redis_client.set(key, value)
                print(f"Key '{key}' created.")
            else:
                self.redis_client.setex(key, time_to_live, value)
                print(f"Key '{key}' created with ttl {time_to_live}.")
        except redis.RedisError as error:
            print(f"An error occurred while storing data in Redis: {error}")
            raise

    def check_key(self, key):
        try:
            key_exists = self.redis_client.exists(key)
            if key_exists:
                ttl = self.redis_client.ttl(key)
                print(f"Key '{key}' exists in Redis with TTL {ttl}.")
                return True, ttl

            print(f"Key '{key}' does not exist in Redis.")
            return False, None
        except redis.RedisError as error:
            print(f"An error occurred while checking a key in Redis: {error}")
            raise

    def get_data(self, key):
        try:
            output = self.redis_client.get(key)
            if output is None:
                print(f"No value found for key '{key}'.")
                return None

            if isinstance(output, bytes):
                output = output.decode("utf-8")

            try:
                result = json.loads(output)
                print(f"JSON value found for key '{key}'.")
                return result
            except json.JSONDecodeError:
                print(f"String value found for key '{key}'.")
                return output

        except redis.RedisError as error:
            print(f"An error occurred while retrieving data from Redis: {error}")
            raise

    def delete_data(self, key):
        try:
            output = self.redis_client.delete(key)
            if output > 0:
                print(f"Key '{key}' and its value have been deleted.")
            else:
                print(f"Key '{key}' not found.")

            return output == 1
        except redis.RedisError as error:
            print(f"An error occurred while deleting data from Redis: {error}")
            raise

    def delete_data_with_pattern(self, pattern):
        try:
            for key in self.redis_client.scan_iter(match=pattern):
                self.delete_data(key)
        except redis.RedisError as error:
            print(f"An error occurred while deleting data from Redis: {error}")
            raise


def product_cache_key(product_id):
    return f"products:{product_id}"


def products_list_cache_key():
    return "products:all"