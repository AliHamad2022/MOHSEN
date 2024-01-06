import json

def create_json_from_text(input_file, output_file):
    data_list = []

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        cleaned_lines = [line.strip() for line in lines]

        # التكرار بفاصلة 5 أسطر لاستخراج كل سؤال وخياراته
        for i in range(0, len(cleaned_lines), 5):
            # تجاهل الفراغ إذا كان السطر فارغًا
            if not all(cleaned_lines[i:i+5]):
                continue

            question = cleaned_lines[i]
            choices = cleaned_lines[i + 1:i + 5]

            # تجاهل الفراغ إذا كان هناك سطر فارغ
            if not any(choices) or not question:
                continue

            # إنشاء الهيكل البياني لكل سطر
            item = {
                "question": question,
                "choice1": choices[0],
                "choice2": choices[1],
                "choice3": choices[2],
                "choice4": choices[3],
                "answer": "answer"
            }

            # إضافة الهيكل البياني إلى القائمة
            data_list.append(item)

    # حفظ البيانات في ملف JSON
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, ensure_ascii=False, indent=2)

# استخدام الدالة مع اسم ملف الإدخال وملف الإخراج المرغوب
create_json_from_text('t.txt', 's.json')
