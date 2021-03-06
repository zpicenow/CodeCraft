# -*- coding: utf-8 -*-
"""
* @Author: ziuno
* @Software: PyCharm
* @Time: 2019/3/27 21:05
"""


class Car(object):
    UNDEFINED = 0
    GO_STRAIGHT = 1
    TURN_RIGHT = 3
    TURN_LEFT = 2

    def __init__(self, id, start, end, speed, plan_time):
        self.__id = id
        self.__start = start
        self.__end = end
        self.__speed = speed
        self.__plan_time = plan_time
        self.__remaining_step = 0
        self.__cur_pos = []
        self.__end_pos = []
        self.__has_moved = False
        self.__move_way = [0, 0]
        self.__direction = Car.UNDEFINED

    def reset_cur_end_pos(self, graph):
        self.__cur_pos = graph.get_car_start_pos(self)
        self.__end_pos = graph.get_car_end_pos(self)

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @property
    def move_way(self):
        return self.__move_way

    @move_way.setter
    def move_way(self, move_way):
        self.__move_way = move_way

    @property
    def has_moved(self):
        return self.__has_moved

    @has_moved.setter
    def has_moved(self, has_moved):
        self.__has_moved = has_moved

    @property
    def id(self):
        return self.__id

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    @property
    def speed(self):
        return self.__speed

    @property
    def plan_time(self):
        return self.__plan_time

    @property
    def remaining_step(self):
        return self.__remaining_step

    @remaining_step.setter
    def remaining_step(self, remaining_step):
        self.__remaining_step = remaining_step

    def move_first_step(self, graph):
        pass
# def getCarList():
#     myCarList = []
#
#     car_path = u'../car.txt'
#     mycar = read_txt.read_txt(car_path)
#     for i in mycar:
#         temp = Car(i[0], i[1], i[2], i[3], i[4])
#         myCarList.append(temp)
#
#     return myCarList
