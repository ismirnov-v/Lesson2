school_class_rate = [
    {'school_class': '3b', 'scores': [3, 5, 1, 1, 5, 5, 2, 4, 3, 5]},
    {'school_class': '7a', 'scores': [5, 5, 4, 4, 5, 4, 4, 5, 5, 4]},
    {'school_class': '4e', 'scores': [5, 4, 5, 5, 3, 3, 2, 3, 2, 4]},
    {'school_class': '5c', 'scores': [3, 5, 2, 2, 1, 4, 5, 5, 3]},
    {'school_class': '6d', 'scores': [4, 4, 2, 1, 5, 5, 2, 5, 4]},
]

avg_school_score = 0
qty_score = 0

for school_score in school_class_rate:
    avg_school_score += sum(school_score["scores"])
    qty_score += len(school_score['scores'])

print(f'Средний бал по всей школе равен: {avg_school_score / qty_score}.')

for class_score in school_class_rate:
    avg_class_score = sum(class_score['scores']) / len((class_score['scores']))
    print(f'В классе "{class_score["school_class"]}" средний балл равен: {round(avg_class_score, 2)}')