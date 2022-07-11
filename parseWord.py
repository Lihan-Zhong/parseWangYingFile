from docx import Document

document = Document("WPME 3&4&5 词根复习资料.docx")

all_paragraphs = document.paragraphs
# print(type(all_paragraphs))
for paragraph in all_paragraphs:
    # runs=paragraph.runs
    # for run in runs:
    #     print(run.text, end="   ")
    # print()
    text=paragraph.text
    if ("–" not in text):
        continue
    else:
        print(text)