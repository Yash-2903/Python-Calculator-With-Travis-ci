from collections import Counter


def mode(data):
    try:
        total = len(data)
        count = Counter(data)
        modeValue = [k for k, v in count.items() if v == count.most_common(1)[0][1]]

        if len(modeValue) == total:
            return "Mode not found."

        else:
            return modeValue

    except ValueError:
        print("ERROR!  That is an empty array.  Try again")
