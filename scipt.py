import pandas as pd
import lxml
import gspread


url = 'https://confluence.hflabs.ru/pages/viewpage.action?pageId=1181220999'

tables = pd.read_html(url, encoding='utf-8')
ts = tables[0]
ts_values = ts.values.tolist()

gc = gspread.service_account()
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1MwzMhmEC0-ggDENuQYemoZuFkpGl81eknjRGAi5GvM8/edit?usp=sharing')

worksheet = sh.add_worksheet(title="worksheet", rows=100, cols=20)
worksheet.update('A1', 'HTTP-код ответа')
worksheet.update('B1', 'Описание')
sh.values_append('worksheet', {'valueInputOption': 'RAW'}, {'values': ts_values})