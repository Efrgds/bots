# from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.fsm.state import StatesGroup, State


class Answer(StatesGroup):
    waiting_for_answer = State
