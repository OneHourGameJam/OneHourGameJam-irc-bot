import urllib.request
import time
import json

def update_db():
    print("Updating DB")

    entries = []

    entries_total = 0

    with urllib.request.urlopen('http://ludumdare.com/compo/ludum-dare-35/?action=preview') as page:
        for i in range(415):
            page.readline()
        entries_str = page.readline().decode('utf-8')
        entries_start = entries_str.find('<h2>All Entries (') + len('<h2>All Entries (')
        entries_end = entries_str.find(')</h2>')
        entries_total = int(entries_str[entries_start:entries_end])
        #print(entries_total)

    for entry_index in range(0, entries_total - 24, 24):
        with urllib.request.urlopen('http://ludumdare.com/compo/ludum-dare-35/?action=preview&start=' + str(entry_index)) as page:
            for i in range(415):
                page.readline()
            entries_str = page.readline().decode("utf-8")  # type: str
            # find the url
            for entry in entries_str.split("&uid=")[1:]:
                uid_start = 0
                uid_end = entry.find("'><img ")
                name_start = entry.find('<i>') + 3
                name_end = entry.find('</i>')
                author_start = name_end + 10
                author_end = entry.find('</a>')

                uid = entry[uid_start: uid_end]
                name = entry[name_start: name_end]
                author = entry[author_start: author_end]

                entries.append({"name": name, "author": author, "uid": uid})

        # if ludum dare complains, add a delay between page queries:
        # time.sleep(0.5)

    f = open('entries.json', 'w')
    f.write(json.dumps({"entries": entries}, indent=4))
    print("Scrapped %s entries" % str(len(entries)))
    return len(entries)
