def response(hey_bob):
    
    answer = "Whatever."

    if hey_bob.rstrip().endswith("?"):
        answer = "Sure."

    if hey_bob.isupper():
        answer = "Whoa, chill out!"

    if hey_bob.isupper() and hey_bob.rstrip().endswith("?"):
        answer = "Calm down, I know what I'm doing!"

    if hey_bob.isspace() or not hey_bob:
        answer = "Fine. Be that way!"

    return answer