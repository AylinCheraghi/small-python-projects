#remove emojis from text
import demoji
text = "Good Morning! 🌸🌷"
a1 = demoji.replace(text, "")
print(a1)