import tkinter as tk
from tkinter import ttk

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

root = tk.Tk()

root.geometry('400x2000')

root.title('抽出箇所の修正form')


description_label = tk.Label(root, text="スプレッドシートにある、数値を確認して\n\n各項目の正しい行数を入力してください。", wraplength=350)
description_label.pack(pady=10)  # ラベルをウィンドウの上部に配置


# スクロールバー付きのキャンバスを作成
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

canvas.bind("<MouseWheel>", on_mousewheel)

# GUIウィンドウを他のウィンドウの上に持ち上げ、視覚的に前面に表示
root.lift()

# ユーザーが他のウィンドウを操作しても、このGUIウィンドウは画面の最前面に表示され続ける
root.call('wm', 'attributes', '.', '-topmost', True)

# ユーザーが他のウィンドウに移動した時に、このウィンドウが他のウィンドウに隠れるようになる
root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)

grid_frame = tk.Frame(root)
grid_frame.pack(pady=20)



# エントリーの名称リスト
entry_names = ["Sneaker_data_start", "Sneaker_data_end", "Sneaker_rainbow_data", "Sneaker_count_data_start", "Sneaker_count_data_end", "Sneaker_count_rainbow_data", "Gems_lv1_lv5_data_start", "Gems_lv1_lv5_data_end", "Gems_lv6_data_start", "Gems_lv6_data_end", "Gems_lv7_data_start", "Gems_lv7_data_end", "Gems_lv8_E_L_data_start", "Gems_lv8_E_L_data_end", "Gems_lv8_Resilience_data", "Gems_lv9_Resilience_data", "Gems_count_data_start", "Gems_count_data_end", "Gems_count_lv7_data_start", "Gems_count_lv7_data_end", "Gems_count_lv8_data_start", "Gems_count_lv8_data_end", "Gems_count_lv9_data_start", "Gems_count_lv9_data_end", "Scroll_data1", "Scroll_data2", "Scroll_data3", "Scroll_data4", "Scroll_data5", "Scroll_count_data1", "Scroll_count_data2", "Scroll_count_data3", "Scroll_count_data4", "Scroll_count_data5"]


# 名称をキーとしてエントリーウィジェットを保持する辞書
entries = {}

for i, name in enumerate(entry_names):  # 名称リストをループする
    label = tk.Label(scrollable_frame, text=name)  # 名称に対応するラベルを作成
    label.grid(row=i, column=0, padx=20)  # ラベルを作成
    entry = tk.Entry(scrollable_frame, fg='grey', width=5)
    entry.grid(row=i, column=1, padx=20)
    entries[name] = entry





# 入力する項目　34項目
# Sneaker_data = cleaned_list[:16]
# Sneaker_rainbow_data = cleaned_list[16]
# Sneaker_count_data = cleaned_list[17:33]
# Sneaker_count_rainbow_data = cleaned_list[33]

# Gems_lv1_lv5_data = cleaned_list[34:59]
# Gems_lv6_data = cleaned_list[59:63]
# Gems_lv7_data = cleaned_list[63:67]
# Gems_lv8_E_L_data = cleaned_list[67:69]
# Gems_lv8_Resilience_data = cleaned_list[69]
# Gems_lv9_Resilience_data = cleaned_list[70]

# Gems_count_data = cleaned_list[73:103]
# Gems_count_lv7_data = cleaned_list[103:107]
# Gems_count_lv8_data = cleaned_list[107:111]
# Gems_count_lv9_data = cleaned_list[111:115]

# Scroll_data = [cleaned_list[115], cleaned_list[117], cleaned_list[119], cleaned_list[121], cleaned_list[123]]
# Scroll_count_data = [cleaned_list[116], cleaned_list[118], cleaned_list[120], cleaned_list[122], cleaned_list[124]]

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

canvas.bind("<Button-4>", on_mousewheel)
canvas.bind("<Button-5>", on_mousewheel)

root.mainloop()