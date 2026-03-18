# Auto-generated script
# Created: 2026-03-18T15:37:12.216222
# Account: Account 1

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    print("Script executed successfully!")
