# 1_figures
В примере из лекций с наследованием класса "квадрат" от класса "прямоугольник" нарушался принцип подстановки Барбары Лисков.  
Исправлено нарушение принципа с помощью добавления свойств для класса "квадрат".  
Для демонстрации корректной работы создается объект класса "Square", затем производится попытка изменить поле width - вызывается сеттер (для которого определено свойство), и меняются оба поля width и height. После этого сравниваются поля width и height, чтобы убедиться, что не нарушилось равенство сторон квадрата.  
Команда: Богданова Елизавета 5130201/20101, Якунин Дмитрий 5130201/20101, Луговенко Полина 5130201/20102  
