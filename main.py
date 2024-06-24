# -*- coding: utf-8 -*-
"""
Модуль для управления заметками через командную строку.
Этот модуль предоставляет функции для добавления, просмотра, поиска,
удаления и перечисления заметок в базе данных с использованием SQLAlchemy.
"""

import argparse
from database import Database
from models import Note

# Инициализация базы данных
db = Database()


def add_note(title, content):
    """
    Добавляет новую заметку в базу данных.
    """
    session = db.get_session()
    note = Note(title=title, content=content)
    session.add(note)
    session.commit()
    session.close()
    print(f"Заметка '{title}' добавлена.")


def view_note(note_id):
    """
    Отображает содержание заметки по её ID.
    """
    session = db.get_session()
    note = session.get(Note, note_id)  # Используем новый метод Session.get()
    session.close()
    if note:
        print(f"Заголовок: {note.title}\nСодержание: {note.content}")
    else:
        print(f"Заметка с ID {note_id} не найдена.")


def search_notes(keyword):
    """
    Ищет заметки, содержащие указанное ключевое слово.
    """
    session = db.get_session()
    notes = session.query(Note).filter(Note.content.contains(keyword)).all()
    session.close()
    if notes:
        for note in notes:
            print(f"ID: {note.id}, Заголовок: {note.title}")
    else:
        print(f"Заметки, содержащие '{keyword}', не найдены.")


def delete_note(note_id):
    """
    Удаляет заметку по её ID.
    """
    session = db.get_session()
    note = session.get(Note, note_id)  # Используем новый метод Session.get()
    if note:
        session.delete(note)
        session.commit()
        print(f"Заметка с ID {note_id} удалена.")
    else:
        print(f"Заметка с ID {note_id} не найдена.")
    session.close()


def list_notes():
    """
    Отображает список всех заметок.
    """
    session = db.get_session()
    notes = session.query(Note).all()
    session.close()
    if notes:
        for note in notes:
            print(f"ID: {note.id}, Заголовок: {note.title}")
    else:
        print("Заметок нет.")


def main():
    """
    Основная функция для управления заметками через командную строку.
    """
    parser = argparse.ArgumentParser(
        description='Менеджер заметок.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--add', nargs=2, metavar=('title',
                        'content'), help='Добавить новую заметку')
    parser.add_argument('--view', type=int,
                        metavar='note_id', help='Просмотр заметки по ID')
    parser.add_argument('--search', metavar='keyword',
                        help='Поиск заметок по ключевому слову')
    parser.add_argument('--delete', type=int,
                        metavar='note_id', help='Удалить заметку по ID')
    parser.add_argument('--list', action='store_true',
                        help='Просмотр списка всех заметок')

    args = parser.parse_args()

    if args.add:
        title, content = args.add
        add_note(title, content)
    elif args.view:
        view_note(args.view)
    elif args.search:
        search_notes(args.search)
    elif args.delete:
        delete_note(args.delete)
    elif args.list:
        list_notes()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
