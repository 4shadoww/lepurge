#!/usr/bin/env python3
import mwapi
import user_config

wikipedia = "https://fi.wikipedia.org"

def login():
    global session
    session = mwapi.Session(wikipedia, user_agent="refreshbot")
    session.login(user_config.username, user_config.password)

def param_maker(values):
    if type(values) != list:
        return values

    final_str = ""
    for i in range(len(values)):
        final_str += str(values[i])

        if i < len(values) - 1:
            final_str += "|"

    return final_str

def main():
    login()

    titles = []

    pages = session.get(action="query", list="search", srsearch="\"data.schemaVersion must be a number\"", srlimit=5000, srprop="titlesnippet")
    for page in pages["query"]["search"]:
        print("going to purge %s" % page["title"])
        titles.append(page["title"])

    session.post(action="purge", titles=param_maker(titles), forcelinkupdate=True)


if __name__ == "__main__":
    main()
