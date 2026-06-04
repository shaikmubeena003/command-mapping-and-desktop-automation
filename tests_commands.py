from core.validator import validate_request

# Test Case 1
result = validate_request("PLAY", 0.95)
print(result)

# Test Case 2
result = validate_request("PLAY", 0.50)
print(result)

# Test Case 3
result = validate_request("HELLO", 0.95)
print(result)