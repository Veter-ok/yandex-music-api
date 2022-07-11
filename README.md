# Yandex Music API

[![GitHub issues](https://img.shields.io/github/issues/Veter-ok/yandex-music-api)](https://github.com/Veter-ok/yandex-music-api/issues) [![GitHub forks](https://img.shields.io/github/forks/Veter-ok/yandex-music-api)](https://github.com/Veter-ok/yandex-music-api/network) [![GitHub stars](https://img.shields.io/github/stars/Veter-ok/yandex-music-api)](https://github.com/Veter-ok/yandex-music-api/stargazers) [![GitHub license](https://img.shields.io/github/license/Veter-ok/yandex-music-api)](https://github.com/Veter-ok/yandex-music-api)

> #### Данная API является неофициальной

Данная API создана для получения доступа к некоторым данным пользователей ***без регестрации***. Из-за отсутствия регестрации, библиотека получает ограниченное количество данных.

## Начало работы

Для начала работы импортируем библиотеку и создаём экземпляр класс для получения данных. В качестве аргумента передаём имя пользователя:

```
from yandex_music_api import Client

client = Client("имя пользователя")
```

Так для получения списка плейлистов необходмо воспользоваться методом *get_playlists()*

```
from yandex_music_api import Client

client = Client("имя пользователя")
playlists = client.get_playlists()
```

В примере выше в переменной *playlists,* будет хранится массив из объектов вида:

```
{
    name: "имя плейлиста",
    url: "ссылка на плейлист"
}
```

Для получение песен из плейлиста необходмо воспользоваться методом *get_tracks_from_playlist()* и в качестве аргумента передать ссылку на плейлист.

```
from yandex_music_api import Client

client = Client("имя пользователя")
playlists = client.get_playlists()
tracks = client.get_tracks_from_playlist(playlists[0]['url'])
```

В примере выше в переменной *tracks*, будет хранится массив из объектов вида:

```
{
    name: "название песни",
    artist: "имя исполнителя"
}
```

Для получения треков, которые были отмечены как "нравится" используем метод *get_tracks()*

```
from yandex_music_api import Client

client = Client("имя пользователя")
tracks = client.get_tracks()
```

Метод вернёт массив из объектов того же вида, что и метод get_tracks_from_playlist()

Для получения данных о любимых исполнителях, необходимо использовать метод *get_artists()*

```
from yandex_music_api import Client

client = Client("имя пользователя")
playlists = client.get_artists()
```

Метод вернёт массив из объектов вида:

```
{
    name: "имя исполнителя",
    genres: "жанр исполнителя"
}
```

## Сохранение данных

**Все выше перечисленные методы** обладают аргументами ***path*** и **filename** позволяющие сохранять данные в ***.txt*** файл

path - путь по которому сохранять файл (по умолчанию None)

filename - имя файла для сохранения

```
from yandex_music_api import Client

client = Client("имя пользователя")
playlists = client.get_playlists(path="data/", filename="playlists")
```

Выше приведенный код сохранит список плейлистов в файл **/data/playlists.txt**

## Итог

Поздравляю Вы дочитали до конца документацию

Надеюсь данная библиотека пригодится Вам в работе
