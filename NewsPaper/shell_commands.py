# Запуск Shell:
# python manage.py shell

# Импорт:
from news.models import *

# Создание двух пользователей:
user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')

# Создание двух объектов модели Author, связанных с пользователями
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# Добавление 4 категорий:
Category.objects.create(name="Спорт")
Category.objects.create(name="Политика")
Category.objects.create(name="Наука")
Category.objects.create(name="Искусство")

# Добавление 2 статей и 1 новости:
post1 = Post.objects.create(author=author1, post_type="article", title="Статья 1", text='Текст статьи 1')
post2 = Post.objects.create(author=author2, post_type="article", title="Статья 2", text='Текст статьи 2')
post3 = Post.objects.create(author=author1, post_type='news', title='Новость 1', text='Текст новости 1')

# Присвоение категорий статьям/новости:
post1.categories.add(Category.objects.get(name="Спорт"))
post1.categories.add(Category.objects.get(name="Политика"))
post2.categories.add(Category.objects.get(name="Наука"))
post3.categories.add(Category.objects.get(name="Искусство"))

# Создание комментариев:
comment1 = Comment.objects.create(post=post1, author=user1, text="Комментарий 1")
comment2 = Comment.objects.create(post=post2, author=user2, text="Комментарий 2")
comment3 = Comment.objects.create(post=post3, author=user1, text="Комментарий 3")
comment4 = Comment.objects.create(post=post1, author=user2, text="Комментарий 4")

# Применение функций like() и dislike() к объектам:
post1.like()
post1.dislike()
comment1.like()
comment1.dislike()

# Обновление рейтингов пользователей:
author1.update_rating()
author2.update_rating()

# Вывод username и рейтинга лучшего пользователя
best_user = Author.objects.all().order_by('-rating').first()
print(best_user.user.username, best_user.rating)
# Результат ---> user1 3

# Вывод информации о лучшей статье:
best_post = Post.objects.all().order_by("-rating").first()
print(best_post.created_at, best_post.author.user.username, best_post.rating, best_post.title, best_post.preview())
# Результат ---> 2024-05-01 14:34:02.230076+00:00 user1 1 Статья 1 Текст статьи 1

# Вывод всех комментариев к лучшей статье:
comments_to_best_post = Comment.objects.filter(post=best_post)
for comment in comments_to_best_post:
    print(comment.created_at, comment.author.username, comment.rating, comment.text)
# Результат ---> 2024-05-01 14:39:40.603638+00:00 user1 1 Комментарий 1
#                2024-05-01 14:43:15.286640+00:00 user2 0 Комментарий 4
