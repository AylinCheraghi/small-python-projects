#remove emojis from text

import demoji
demoji.download_codes()

text = "Good Morning! 🌸🌷"
a1 = demoji.replace(text, "")
print(a1)

#Replace Emojis with Descriptive Text
text = "Happy birthday! 🎂🎈"
a1 = demoji.replace(text)
print(a1)