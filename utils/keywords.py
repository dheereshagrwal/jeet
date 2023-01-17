def get_keywords(titles):
    if not titles:
        return None
    try:
        file = open("keywords.txt", "r")
        keywords = file.readlines()
        file.close()
        # remove whitespace from each keyword
        keywords = [x.strip() for x in keywords]
    except:
        print('keywords.txt does not exist, quitting....')
        exit()
    keys = []
    for title in titles:
        for keyword in keywords:
            if keyword.lower() in title.lower():
                keys.append(keyword)
    return keys if keys else None

