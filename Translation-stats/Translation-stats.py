import re, os, io

# Revise following two defines (language_code and r2g_path) before you start using this program.
# Two-letter codes, represents the target language of translation you're working on.
language_code = "zh"  # Check https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes for yours.
# Path of your R2G folder (WITHOUT A BACKSLASH AT THE END)
# r2g_path      = r"G:\SteamLibrary\steamapps\common\Return 2 Games"
r2g_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))  # In this way, this file should lies in subfolder
                                                                  # of Return 2 Games folder.
launcher_path = r2g_path + r"\lang_{}\launcher.utf8".format(language_code)
main_path = r2g_path + r"\bod_lang_{}_demo\bod_demo_main.utf8".format(language_code)
cards_path = r2g_path + r"\bod_lang_{}_demo\bod_demo_cards.utf8".format(language_code)
gossips_path = r2g_path + r"\bod_lang_{}_demo\bod_demo_gossips.utf8".format(language_code)


# translated_units: load ignore items from ignore.txt
def load_ignores_for(translated_units):
    with open(r"ignore.txt") as f:
        all_text = f.read().split("\n")
        for index, line in enumerate(all_text):
            if line.startswith("# "):
                pass
            elif not line:
                pass
            else:
                translated_units.setdefault(index, re.escape(line))
    return translated_units


script_line_re = r"^\w+\s*=\s*\"(.*?)(?<!\\)\"\s*(#.*)?"
# Made for simplified chinese and traditional chinese. Revise it if you're working on a translation for other language.
translated_units = {"wide character"        : r"[^\x00-\xff]",  # Contains all Chinese characters.
                    "color_mark_begin"      : r"\\\^[a-zA-Z0-9]{6}",
                    "color_mark_end"        : r"\\\^\^",
                    "foo_1"                 : r"\\m\d\.\d",
                    "space"                 : r"\s",
                    "icon_mark"             : r"\\s[a-zA-Z]*[0-9]*[<>?:;=`]?",
                    "several characters"    : r"[/+-=,.:?!>_%~()]|\\\"",
                    "carriage return mark"  : r"\\n",
                    "variable mark"         : r"\\\d",
                    "digit"                 : r"\d",
                    "empty"                 : r""}
translated_units = load_ignores_for(translated_units)
translated_text_re = "^({})+$".format("|".join(x for x in translated_units.values()))
print(translated_text_re)

s = re.compile(script_line_re)
t = re.compile(translated_text_re)
ignore_string_mark = "# Translator: Translated."
ignore = re.compile(re.escape(ignore_string_mark))
print("ignore = ", ignore)

translation_items_count_summary = 0
translated_items_count_summary = 0
file_log = ""
log = ""


def save_file_log(filename, content):
    with io.open(filename, 'w', encoding='utf8') as f:
        f.write(content)


for x in (launcher_path, main_path, cards_path, gossips_path):
    print(x)
    with open(x, encoding='utf-8') as f:
        plain_text = f.read()
        all_text = plain_text.split("\n")
        file_log = list(all_text)
        translation_items_count_in_file = 0
        translated_items_count_in_file = 0
        for index, line in enumerate(all_text):
            script = ""
            result = s.match(line)
            try:
                script = result.group(1)
            except (IndexError, AttributeError):
                file_log[index] = "  " + file_log[index]
                continue
            translation_items_count_in_file += 1
            if ignore.search(line) or t.match(script):
                translated_items_count_in_file += 1
                file_log[index] = "T " + file_log[index]
            else:
                file_log[index] = "N " + file_log[index]
                print(script)
        translated_items_count_in_file += len(re.findall(ignore_string_mark, plain_text))
        log += "* {}: {}% ({}/{})\n".format(re.search(r"(?<=\\)\w*\\\w*\.utf8", x).group(0),
                                            round(translated_items_count_in_file / \
                                                  translation_items_count_in_file * 100),
                                            translated_items_count_in_file,
                                            translation_items_count_in_file)
        translation_items_count_summary += translation_items_count_in_file
        translated_items_count_summary += translated_items_count_in_file
        save_file_log(x + ".log", '\n'.join(file_log))

summary = "* Overall progress: {}% ({}/{})\n".format(
    round(translated_items_count_summary / translation_items_count_summary * 100),
    translated_items_count_summary, translation_items_count_summary)
log = summary + log
f = open('Progress.txt', 'w')
f.write(log)
f.close()

os.startfile("Progress.txt")
