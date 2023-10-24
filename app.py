from flask import Flask, render_template, request
import gspread
from google.oauth2.service_account import Credentials



# お決まりの文句
# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
# ダウンロードしたjsonファイル名をクレデンシャル変数に設定。
credentials = Credentials.from_service_account_file("skilful-ethos-402603-4adec231668c.json", scopes=scope)
# OAuth2の資格情報を使用してGoogle APIにログイン。
gc = gspread.authorize(credentials)
# スプレッドシートIDを変数に格納する。
SPREADSHEET_KEY = "1-IC_cpdm3sQMdyCwxgIhzHzZScGP1PGkAja5jTNuY2Q"
# スプレッドシート（ブック）を開く
workbook = gc.open_by_key(SPREADSHEET_KEY)

workbook = gc.open_by_key(SPREADSHEET_KEY)
# シートの一覧を取得する。（リスト形式）
worksheets = workbook.worksheets()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # スプレッドシート　https://docs.google.com/spreadsheets/d/1-IC_cpdm3sQMdyCwxgIhzHzZScGP1PGkAja5jTNuY2Q/edit?usp=sharing
        # シートID　（のちに.envに記入　1-IC_cpdm3sQMdyCwxgIhzHzZScGP1PGkAja5jTNuY2Q）

        # シートを開く
        worksheet = workbook.worksheet("シート1")

        row = len(worksheet.col_values(1)) + 1

        # セルA1に”test value”という文字列を代入する。
        worksheet.update_cell(row, 1, request.form["q"])

        print(worksheet.col_values(1))
        return render_template("fake_google.html")

    return render_template("fake_google.html")


if __name__ == "__main__":
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
