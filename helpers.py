
def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    sub = ""
    matches = []

    # create a list of the a substrings.
    i = 0
    j = n
    aList = []

    # create a list of all possible substring of n length in a
    while(j <= len(a) + 1):

        sub = a[i:j]

        aList.append(sub)

        i += 1
        j += 1

    # Check each b substring to see if it is also an a substring.
    i = 0
    j = n

    while(j <= len(b) + 1):

        sub = b[i:j]

        if sub not in matches and sub in aList and len(sub) == n:

            matches.append(sub)

        i += 1
        j += 1

    return matches
