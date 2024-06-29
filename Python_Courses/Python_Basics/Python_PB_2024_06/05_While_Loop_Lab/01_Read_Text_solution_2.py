# Напишете програма, която чете текст от конзолата(стринг)
# и го принтира, докато не получи командата "Stop".

while True:
    text = input()

    if text == "Stop":
        break

    print(text)
