import pysrt
import pysubs2
import srt
import string

srt_file = "d:\youtuber\dongjiang\english\ep10_the_reservoir_kayaking\ep10_en_ko.srt"

with open(srt_file, "rt", encoding="utf-8") as f:
    subs = list(srt.parse(f))
    for sub in subs:
        if not sub.content.strip:
            del sub
            continue
        while len(sub.content) > 0 and (
            sub.content[0] in string.punctuation
            or not sub.content[0].strip()
        ):
            sub.content = sub.content[1:]

        if "\n" in sub.content:
            lines = sub.content.split("\n")
            if not lines[1] or (lines[1] in string.punctuation and len(lines[1]) == 1):
                sub.content = lines[0]

output_file = srt_file[:-4] + "_modified.srt"
with open(output_file, "w", encoding="UTF-8") as f:
    f.write(srt.compose(subs))

