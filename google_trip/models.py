from django.db import models
from django.db.models import SET_NULL, CASCADE, PROTECT
from django.conf import settings
from django.urls import reverse


class TypeOfAttraction(models.Model):
    class Meta:
        db_table = 'types_of_attraction'
        verbose_name = 'Вид достопримечательности'
        verbose_name_plural = 'Виды достопримечательностей'

    name = models.CharField(verbose_name='Название',
                            max_length=50)

    def __str__(self):
        return f'{self.name}'


class TypeOfRestaurant(models.Model):
    class Meta:
        db_table = 'types_of_restaurant'
        verbose_name = 'Тип ресторана'
        verbose_name_plural = 'Типы ресторанов'

    name = models.CharField(verbose_name='Название',
                            max_length=50)

    def __str__(self):
        return f'{self.name}'


class TypeOfHotel(models.Model):
    class Meta:
        db_table = 'types_of_hotels'
        verbose_name = 'Тип отеля'
        verbose_name_plural = 'Типы отелей'

    name = models.CharField(verbose_name='Название',
                            max_length=50)

    def __str__(self):
        return f'{self.name}'


class LevelOfPrice(models.Model):
    class Meta:
        db_table = 'levels_of_price'
        verbose_name = 'Уровень цены'
        verbose_name_plural = 'Уровни цены'

    level = models.IntegerField(verbose_name='Уровень',
                                null=True)

    def __str__(self):
        return f'{self.name}'


class Country(models.Model):
    class Meta:
        db_table = 'сountries'
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    name = models.CharField(verbose_name='Название',
                            max_length=200,
                            unique=True)
    photo = models.ImageField(verbose_name='Изображение',
                              upload_to=settings.MEDIA_COUNTRY_IMAGE_DIR,
                              null=True)

    def __str__(self):
        return f'{self.name}'


class Region(models.Model):
    class Meta:
        db_table = 'regions'
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    name = models.CharField(verbose_name='Название',
                            max_length=200)
    country = models.ForeignKey(Country,
                                verbose_name='Страна',
                                null=True,
                                on_delete=SET_NULL)
    states = models.ManyToManyField('State')

    def __str__(self):
        return f'{self.name}'


class State(models.Model):
    class Meta:
        db_table = 'states'
        verbose_name = 'Штат'
        verbose_name_plural = 'Штаты'

    name = models.CharField(verbose_name='Название',
                            max_length=200)
    country = models.ForeignKey(Country,
                                verbose_name='Страна',
                                null=True,
                                on_delete=SET_NULL)

    def __str__(self):
        return f'{self.name}'


class County(models.Model):
    class Meta:
        db_table = 'counties'
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    name = models.CharField(verbose_name='Название',
                            max_length=200)
    country = models.ForeignKey(Country,
                                verbose_name='Страна',
                                null=True,
                                on_delete=SET_NULL)
    region = models.ForeignKey(Region,
                               verbose_name='Регион',
                               null=True,
                               on_delete=SET_NULL)
    state = models.ForeignKey(State,
                              verbose_name='Штат',
                              null=True,
                              on_delete=SET_NULL)

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    class Meta:
        db_table = 'cities'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    name = models.CharField(verbose_name='Город',
                            max_length=200)
    country = models.ForeignKey(Country,
                                verbose_name='Страна',
                                null=True,
                                on_delete=SET_NULL)
    region = models.ForeignKey(Region,
                               verbose_name='Регион',
                               null=True,
                               on_delete=SET_NULL)
    state = models.ForeignKey(State,
                              verbose_name='Штат',
                              null=True,
                              on_delete=SET_NULL)
    county = models.ForeignKey(County,
                               verbose_name='Район',
                               null=True,
                               on_delete=SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Town(models.Model):
    class Meta:
        db_table = 'towns'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    name = models.CharField(verbose_name='Город',
                            max_length=200)
    country = models.ForeignKey(Country,
                                verbose_name='Страна',
                                null=True,
                                on_delete=SET_NULL)
    region = models.ForeignKey(Region,
                               verbose_name='Регион',
                               null=True,
                               on_delete=SET_NULL)
    state = models.ForeignKey(State,
                              verbose_name='Штат',
                              null=True,
                              on_delete=SET_NULL)
    county = models.ForeignKey(County,
                               verbose_name='Район',
                               null=True,
                               on_delete=SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Village(models.Model):
    class Meta:
        db_table = 'villages'
        verbose_name = 'Деревня'
        verbose_name_plural = 'Деревни'

    name = models.CharField(verbose_name='Город',
                            max_length=200)
    country = models.ForeignKey(Country,
                                verbose_name='Страна',
                                null=True,
                                on_delete=SET_NULL)
    region = models.ForeignKey(Region,
                               verbose_name='Регион',
                               null=True,
                               on_delete=SET_NULL)
    state = models.ForeignKey(State,
                              verbose_name='Штат',
                              null=True,
                              on_delete=SET_NULL)
    county = models.ForeignKey(County,
                               verbose_name='Район',
                               null=True,
                               on_delete=SET_NULL)

    def __str__(self):
        return f'{self.name}'


class TouristAttraction(models.Model):
    """Достопримечательности"""

    class Meta:
        db_table = 'tourist_attractions'
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'

    name = models.CharField(verbose_name='Название',
                            max_length=200)
    cid = models.CharField(verbose_name='Идентификатор',
                           max_length=30,
                           unique=True)
    rating = models.DecimalField(verbose_name='Рейтинг',
                                 max_digits=4,
                                 decimal_places=3)
    number_of_review = models.PositiveIntegerField(
        verbose_name='Число отзывов')
    rating_5 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 5',
        null=True)
    rating_4 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 4',
        null=True)
    rating_3 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 3',
        null=True)
    rating_2 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 2',
        null=True)
    rating_1 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 1',
        null=True)
    update_at = models.DateTimeField(verbose_name='Обновлено',
                                     auto_now=True)
    latitude = models.DecimalField(verbose_name='Широта',
                                   max_digits=9,
                                   decimal_places=7)
    longitude = models.DecimalField(verbose_name='Долгота',
                                    max_digits=10,
                                    decimal_places=7)
    photo = models.ImageField(
        verbose_name='Изображение',
        upload_to=settings.MEDIA_TOURIST_ATTRACTIONS_IMAGE_DIR,
        null=True)
    type_of_attraction = models.ForeignKey(TypeOfAttraction,
                                           on_delete=CASCADE)
    country = models.ForeignKey(Country,
                                verbose_name='Страна',
                                null=True,
                                on_delete=SET_NULL)
    region = models.ForeignKey(Region,
                               verbose_name='Регион',
                               null=True,
                               on_delete=SET_NULL)
    state = models.ForeignKey(State,
                              verbose_name='Штат',
                              null=True,
                              on_delete=SET_NULL)
    county = models.ForeignKey(County,
                               verbose_name='Район',
                               null=True,
                               on_delete=SET_NULL)
    city = models.ForeignKey(City,
                             verbose_name='Город',
                             null=True,
                             on_delete=SET_NULL)
    town = models.ForeignKey(Town,
                             verbose_name='Город',
                             null=True,
                             on_delete=SET_NULL)
    village = models.ForeignKey(Village,
                                verbose_name='Деревня',
                                null=True,
                                on_delete=SET_NULL)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('view_attraction', kwargs={'pk': self.pk})


class Hotel(models.Model):
    """Отели"""

    class Meta:
        db_table = 'hotels'
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    name = models.CharField(verbose_name='Название',
                            max_length=200)
    cid = models.CharField(verbose_name='Идентификатор',
                           max_length=30, unique=True)
    rating = models.DecimalField(verbose_name='Рейтинг',
                                 max_digits=4,
                                 decimal_places=3)
    number_of_review = models.PositiveIntegerField(
        verbose_name='Число отзывов')
    rating_5 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 5',
        null=True)
    rating_4 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 4',
        null=True)
    rating_3 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 3',
        null=True)
    rating_2 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 2',
        null=True)
    rating_1 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 1',
        null=True)
    update_at = models.DateTimeField(auto_now=True)
    latitude = models.DecimalField(verbose_name='Широта',
                                   max_digits=9,
                                   decimal_places=7)
    longitude = models.DecimalField(verbose_name='Долгота',
                                    max_digits=10,
                                    decimal_places=7)
    photo = models.ImageField(
        verbose_name='Изображение',
        upload_to=settings.MEDIA_TOURIST_HOTELS_IMAGE_DIR,
        null=True)
    type_of_hotel = models.ForeignKey(TypeOfHotel,
                                      null=True,
                                      on_delete=CASCADE)
    country = models.ForeignKey(Country,
                                verbose_name='Страна',
                                null=True,
                                on_delete=SET_NULL)
    region = models.ForeignKey(Region,
                               verbose_name='Регион',
                               null=True,
                               on_delete=SET_NULL)
    state = models.ForeignKey(State,
                              verbose_name='Штат',
                              null=True,
                              on_delete=SET_NULL)
    county = models.ForeignKey(County,
                               verbose_name='Район',
                               null=True,
                               on_delete=SET_NULL)
    city = models.ForeignKey(City,
                             verbose_name='Город',
                             null=True,
                             on_delete=SET_NULL)
    town = models.ForeignKey(Town,
                             verbose_name='Город',
                             null=True,
                             on_delete=SET_NULL)
    village = models.ForeignKey(Village,
                                verbose_name='Деревня',
                                null=True,
                                on_delete=SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Restaurant(models.Model):
    """Рестораны"""

    class Meta:
        db_table = 'restaurants'
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

    name = models.CharField(verbose_name='Название',
                            max_length=200)
    cid = models.CharField(verbose_name='Идентификатор',
                           max_length=30,
                           unique=True)
    rating = models.DecimalField(verbose_name='Рейтинг',
                                 max_digits=4,
                                 decimal_places=3)
    number_of_review = models.PositiveIntegerField(
        verbose_name='Число отзывов')
    rating_5 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 5',
        null=True)
    rating_4 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 4',
        null=True)
    rating_3 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 3',
        null=True)
    rating_2 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 2',
        null=True)
    rating_1 = models.PositiveIntegerField(
        verbose_name='Число отзывов c оценкой 1',
        null=True)
    update_at = models.DateTimeField(auto_now=True)
    latitude = models.DecimalField(verbose_name='Широта',
                                   max_digits=9,
                                   decimal_places=7)
    longitude = models.DecimalField(verbose_name='Долгота',
                                    max_digits=10,
                                    decimal_places=7)
    photo = models.ImageField(
        verbose_name='Изображение',
        upload_to=settings.MEDIA_TOURIST_RESTAURANTS_IMAGE_DIR,
        null=True)
    level_of_price = models.ForeignKey(LevelOfPrice,
                                       null=True,
                                       on_delete=PROTECT)
    type_of_restaurant = models.ForeignKey(TypeOfRestaurant,
                                           on_delete=CASCADE)
    country = models.ForeignKey(Country,
                                verbose_name='Страна',
                                null=True,
                                on_delete=SET_NULL)
    region = models.ForeignKey(Region,
                               verbose_name='Регион',
                               null=True,
                               on_delete=SET_NULL)
    state = models.ForeignKey(State,
                              verbose_name='Штат',
                              null=True,
                              on_delete=SET_NULL)
    county = models.ForeignKey(County,
                               verbose_name='Район',
                               null=True,
                               on_delete=SET_NULL)
    city = models.ForeignKey(City,
                             verbose_name='Город',
                             null=True,
                             on_delete=SET_NULL)
    town = models.ForeignKey(Town,
                             verbose_name='Город',
                             null=True,
                             on_delete=SET_NULL)
    village = models.ForeignKey(Village,
                                verbose_name='Деревня',
                                null=True,
                                on_delete=SET_NULL)

    def __str__(self):
        return f'{self.name}'


class PriceOfHotel(models.Model):
    class Meta:
        db_table = 'prices_of_hotel'
        verbose_name = 'Цена на отель'
        verbose_name_plural = 'Цены на отели'

    hotel = models.ForeignKey(Hotel,
                              on_delete=CASCADE)
    price = models.IntegerField(verbose_name='Цена',
                                null=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.hotel} - {self.price}'
