with open('assets/gatsby-short.txt', 'r', encoding="utf-8") as textfile:
    myText = textfile.read()
    words = myText.split(' ')
    font('assets/GimletVariable-VF_TESTING.ttf')
    myFontSize = 1
    for i, word in enumerate(words):
        fontSize(myFontSize)
        w, h = textSize(word)
        displayFontSize = 100/w
        fontSize(displayFontSize)
        text(word, (0, 0))
        translate(0, displayFontSize)
        if i > 10:
            break