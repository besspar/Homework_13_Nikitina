import json


def get_hashtags():
    with open("posts.json", "r") as posts_file:
        posts = json.load(posts_file)

    hashtag_list = []
    post_letters = ''
    for item in posts:
        post_text = item['content']

        post_words = post_text.split()
        for word in post_words:
            if word.startswith("#"):
                hashtag_list.append(word)

    set_of_hashtags = set(hashtag_list)
    hashtag_list = list(set_of_hashtags)

    final_list = []
    for hashtag in hashtag_list:
        if hashtag.startswith("#"):
            final_list.append(hashtag[1:len(hashtag)])

    final_list.sort()
    return final_list


def get_posts(tag):
    with open("posts.json", "r") as posts_file:
        posts = json.load(posts_file)

    posts_list = []
    for item in posts:
        if ("#"+tag) in item['content']:
            posts_list.append(item)

    return posts_list


def add_post(path, content):
    with open("posts.json", "r") as posts_file:
        posts = json.load(posts_file)

    path = "/" + path
    posts_content = {"pic": path, "content": content}

    posts.append(posts_content)

    with open("posts.json", "w") as posts_file:
        json.dump(posts, posts_file, ensure_ascii=False, indent=4)


s = get_hashtags()
print (s)