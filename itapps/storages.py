from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = "cbp32223storage"
    account_key = "5/zvU+A3bt4aNE0V4K1xG/NY0u7NKWryMbtHsyU14zM43PpbrQGuDzg9Os7hX4oESYnkZp8wmzjv+AStfsRRPA=="
    azure_container = "media"
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = "cbp32223storage"
    account_key = "5/zvU+A3bt4aNE0V4K1xG/NY0u7NKWryMbtHsyU14zM43PpbrQGuDzg9Os7hX4oESYnkZp8wmzjv+AStfsRRPA=="
    azure_container = "static"
    expiration_secs = None