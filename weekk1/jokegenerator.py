import random

jokes = [
    "Why do Python programmers wear glasses? Because they can't C.",
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "Why do Java developers wear glasses? Because they don't see sharp.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "Why was the JavaScript developer sad? Because he didn't 'null' his feelings.",
    "Why did the Python function break up with the loop? It got tired of going in circles.",
    "What do you call 8 hobbits? A hobbyte.",
    "Why did the computer show up at work late? It had a hard drive.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the developer go broke? Because he used up all his cache."
]

def tell_joke():
    print("Here's a random programming joke for you:\n")
    print(random.choice(jokes))

if __name__ == "__main__":
    tell_joke()