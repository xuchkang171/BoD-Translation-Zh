import re, os

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

# script_line_re = "^\w+\s*=\s*\"(.*)\""
script_line_re = "^\w+\s*=\s*\"(.*)\""
# Made for simplified chinese and traditional chinese. Revise it if you're working on a translation for other language.
# Todo: Specific explanation
translated_text_re = "^([^\x00-\xff]|\\\^[a-zA-Z0-9]{6}|\\\^\^|\\m\d\.\d|\s|\\s[a-zA-Z]*[0-9]*[<>?:;=]?|[/+=|\\n]|\\\d|\d|[:,.?!->]|)+$"
s = re.compile(script_line_re)
t = re.compile(translated_text_re)
ignore_string_mark = r"# Translator: All or part of it Won't be translated."

translation_items_count_summary = 0
translated_items_count_summary = 0
log = ""

for x in (launcher_path, main_path, cards_path, gossips_path):
    with open(x, encoding='utf-8') as f:
        plain_text = f.read()
        all_text = plain_text.split("\n")
        translation_items_count_in_file = 0
        translated_items_count_in_file = 0
        for line in all_text:
            script = ""
            result = s.match(line)
            try:
                script = result.group(1)
            except (IndexError, AttributeError):
                continue
            translation_items_count_in_file += 1
            if t.match(script):
                translated_items_count_in_file += 1
        translated_items_count_in_file += len(re.findall(ignore_string_mark, plain_text))
        log += "* {}: {}% ({}/{}) translated in {} lines.\n".format(re.search(r"(?<=\\)\w*\\\w*\.utf8", x).group(0),
                                                                    round(translated_items_count_in_file / \
                                                                          translation_items_count_in_file * 100),
                                                                    translated_items_count_in_file,
                                                                    translation_items_count_in_file,
                                                                    len(all_text))
        translation_items_count_summary += translation_items_count_in_file
        translated_items_count_summary += translated_items_count_in_file

summary = "* Overall progress: {}% ({}/{})\n".format(
    round(translated_items_count_summary / translation_items_count_summary * 100),
    translated_items_count_summary, translation_items_count_summary)
log = summary + log
f = open('Progress.txt', 'w')
f.write(log)
f.close()

os.startfile("Progress.txt")
