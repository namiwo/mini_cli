"""
身長体重を受け取り、BIMを少数第二位で出力するアプリ
"""


def main():
    weight_kg = int(input("体重入力(kg)>"))
    height_cm = int(input("身長入力(cm)>"))

    bmi = weight_kg / ((height_cm / 100) ** 2)
    print("BMIは" + str(round(bmi, 2)) + "です")


if __name__ == '__main__':
    main()