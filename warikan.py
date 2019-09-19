"""
割り勘アプリ
金額と人数を受け取り、割り勘結果を出力するアプリ
例:1500円3人⇒1人あたり500円です。端数は0円です。
"""
def main():
    #入力
    nunber_of_people = int(input("人数>"))
    amount = int(input("金額>"))
    #計算

    payment, remainder = divmod(amount, nunber_of_people)
    #出力
    print("1人あたり" + str(payment) +"円です。端数は" + str(remainder) + "円です。")
    print(f"1人あたり{payment}円です。端数は{remainder}円です。")


if __name__ == '__main__':
    main()