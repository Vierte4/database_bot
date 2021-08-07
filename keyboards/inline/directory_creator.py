import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from data.config import files_in_folders, data_base_path

f_and_f_callback = CallbackData("f_and_f", "path")


def show_files_and_folders(directory, id, n=0):
    # Возвращает клавиатуру, построенную на основе файлов в директории, в которой находится программа
    start_n = n
    folders = os.listdir(directory)[n:]
    files = InlineKeyboardMarkup()
    files_in_folders[id] = []
    n = 0
    for file in folders:
        files_in_folders[id].append(file)
        files.add(InlineKeyboardButton(text=f'{file}', callback_data=f_and_f_callback.new(path=n)))
        if n == start_n + 60:
            files.add(
                InlineKeyboardButton(text=f'Ещё', callback_data=f_and_f_callback.new(path='more')))
            files_in_folders[f'{id}nn'] = n
            return files
        n += 1

    if directory != data_base_path:
        files.add(InlineKeyboardButton(text='Назад', callback_data=f_and_f_callback.new(path='back')))
    return files
