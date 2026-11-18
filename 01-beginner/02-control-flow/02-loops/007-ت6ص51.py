#ت6ص51
no-daneshamozan = {
    'علی احمدی': 95,
    'مریم رضایی': 98,
    'رضا کریمی': 92,
    'سارا حسینی': 98,
    'حسن نیکو': 90,
    'زهرا پوریا': 98
}

nomarat = no-daneshamozan.values()

maxno = max(nomarat)

best_students_names = []
for name, score in student_scores.items():
    if score == max_score:
        best_students_names.append(name)

print(f"بالاترین نمره: {max_score}")
print("دانش‌آموز(ان) با بالاترین نمره:")
for name in best_students_names:
    print(f"- {name}")

