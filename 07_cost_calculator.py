requests = 100_000
tokens_per_request = 400
cached_share = 0.25
regular_price_per_million = 0.10
cached_price_per_million = 0.01
all_tokens = requests * tokens_per_request
cached_tokens = all_tokens * cached_share
regular_tokens = all_tokens - cached_tokens
estimate = (regular_tokens / 1_000_000 * regular_price_per_million
            + cached_tokens / 1_000_000 * cached_price_per_million)


print(f"Requests: {requests:,}")
print(f"Input tokens: {all_tokens:,}")
print(f"Estimated Decisions input charges: ${estimate:.2f}")

