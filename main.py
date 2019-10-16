import Entries
import csv
import re
import cld2


def wow_entries(file, entries, lang, limit):
    with open(file, 'r', encoding='utf-8-sig') as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        for line in tsv_reader:
            if line[4] == lang:
                entries.append(Entries.EntryWow(line[0].strip(' '), line[1], line[2], line[3], line[4]))
            if len(entries) > limit:
                break


def fortnite_entries(file, entries, lang, limit):
    with open(file, 'r') as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        for line in tsv_reader:
            lang_details = cld2.detect(line[2])
            if lang_details[2][0][1] == lang:
                entries.append(Entries.EntryFortnite(line[0], line[1], line[2], line[3], lang_details[2][0][1]))
            if len(entries) > limit:
                break


def make_pattern(file):
    words = []
    with open(file, "r") as file:
        for line in file:
            words.append(line.strip('\n'))
    s_pattern = r"\b(" + "|".join(words).strip("|") + r")\b"
    return re.compile(s_pattern, re.IGNORECASE)


def check_entries(pattern_file, file, limit, **kwargs):
    entries = []
    pattern = make_pattern(pattern_file)
    if 'language' not in kwargs:
        kwargs['language'] = 'en'
    if kwargs['game'] == 'fortnite':
        fortnite_entries(file, entries, kwargs['language'], limit)
    elif kwargs['game'] == 'wow':
        wow_entries(file, entries, kwargs['language'], limit)
    for entry in entries:
        if re.search(pattern, entry.get_content()):
            print(entry.get_datetime(), entry.get_author(), entry.get_lang(), entry.get_content())


if __name__ == '__main__':
    check_entries('s_words.txt', 'WoWLog.tsv', 1000, game='wow', language='en')
    check_entries('s_words.txt', 'FortniteLog.tsv', 1000, game='fortnite', language='un')
    check_entries('s_words.txt', 'WoWLog.tsv', 1000, game='wow', language='un')
