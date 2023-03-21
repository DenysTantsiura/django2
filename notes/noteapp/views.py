from django.shortcuts import redirect, render

from noteapp.forms import NoteForm, TagForm
from noteapp.models import Tag  # notes.noteapp.models


# Create your views here.
def main(request):
    return render(request, 'noteapp/index.html')

def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)  # виконуємо обробку форми
        if form.is_valid():  # перевіряємо валідність введених даних форми функцією
            form.save()  # виконуємо збереження даних форми у базі даних
            return redirect(to='noteapp:main')  # перехід на головну сторінку
        else:  # повторний рендер шаблону- Саме тут спрацює виведення помилки в інструкції {{form.errors.name}} шаблону
            return render(request, 'noteapp/tag.html', {'form': form})

    return render(request, 'noteapp/tag.html', {'form': TagForm()})  # Для GET запиту ми просто виконуємо рендер шаблону

def note(request):
    tags = Tag.objects.all()  # Спочатку шукаємо всі теги, їх назви ми передаємо у шаблон для виведення в тезі select

    if request.method == 'POST':
        form = NoteForm(request.POST)  # збираємо дані з форми
        if form.is_valid():  # перевіряємо їх на валідніст
            new_note = form.save()  # Створюємо нотатку note і зберігаємо результат до бази даних

            # Отримуємо список тегів tags із запиту до БД:
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            # (щоб отримати саме список з елемента форми, ми повинні використовувати метод getlist)
            # (необхідно використовувати SQL оператор IN для перевірки входження тегу в отриманий список. 
            # Django використовує підхід вказівки імені поля name, символу подвійного підкреслення і сам оператор)
            # https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_many/

            # Додаємо теги до нотатки у циклі за допомогою методу add. Перенаправляємо користувача на головну сторінку
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)

            return redirect(to='noteapp:main')
        else:  # рендеримо шаблон із повідомленнями про помилки
            return render(request, 'noteapp/note.html', {"tags": tags, 'form': form})

    # шаблон для створення нотатки, попередньо прокинувши всередину всі існуючі теги tags
    return render(request, 'noteapp/note.html', {"tags": tags, 'form': NoteForm()})
