"""
Список задач
В файле todo.txt хранится список дел. Например:
    Сходить в магазин: DONE
    Полить цветы: TODO
    Помыть окна: TODO
    Покормить кота: TODO
    Сделать домашку по Python: TODO
    Поздравить Алису с Днем Рождения: DONE
    Составить список дел: DONE
При запуске программа выводит по одному еще не сделанные дела и спрашивает, выполнено ли оно.
Пользователь отвечает y/n, и программа записывает новый список дел.
"""

with open('todo.txt', 'r', encoding='utf-8') as f_in:
    task_lst = [x.strip().split(': ') for x in f_in]

total_tasks_count = len(task_lst)
done_tasks_count = len([x for x in task_lst if x[1] == "DONE"])

print(f'В списке {total_tasks_count} дел')
print(f'Сделано {done_tasks_count}/{total_tasks_count}')

if done_tasks_count != total_tasks_count:
    print('Давай пройдемся по твоим делам!')
else:
    print('Все дела сделаны!')
    quit()

with open('todo.txt', 'w', encoding='utf-8') as f_out:
    for task in task_lst:
        if task[1] == 'TODO':
            user_input = input(f'{task[0]} – сделано? (y/n)\n').lower()
            task[1] = 'DONE' if user_input == 'y' else 'TODO'

    f_out.write('\n'.join(f'{x[0]}: {x[1]}' for x in task_lst))
