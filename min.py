from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout 
import json 
app = QApplication([])                               

notes = {
    'Ласкаво просимо':{
        "текст" :"Це накращий додаток для заміток у світі ",
        "теги" : ["Добро","Інструкція"]
        }


}
with open("notes_data.json","w")as fille:
    json.dump(notes,fille )

notes_win = QWidget()
notes_win.setWindowTitle("Розумні замітки")
notes_win.resize(900,600)

list_notes = QListWidget()
list_notes_label = QLabel("Список заміток")

button_note_create = QPushButton("Створи замітку")
button_note_del = QPushButton("Видали замітку")
button_note_save = QPushButton("Зберегти замітку")

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Ведіть тег...')
field_text = QTextEdit()
button_tag_add = QPushButton("Додати до замітки ")
button_tag_del = QPushButton("Відкріпити від замітки  ")
button_tag_search = QPushButton("Шукати замітки за тегом ")
list_tags = QListWidget()
list_tags_label = QLabel('Список тегів')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_tags_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
 

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)


col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1,stretch=2)
layout_notes.addLayout(col_2,stretch=1)
notes_win.setLayout(layout_notes)
def show_note():
    # отримуємо текст із замітки з виділеною назвою та відображаємо його в полі редагування
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])




# підключення обробки подій
list_notes.itemClicked.connect(show_note)


with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)








notes_win.show()
app.exec_()








































