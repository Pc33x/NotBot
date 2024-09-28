class Language():
    def __init__(self, language):
        self.language = language

    def get_data(self):
        match(self.language):
            case 'Русский 🇷🇺':
                return {'text_info': 'Ваш язык -',
                        'text_add_note': 'Напишите заметку в чат, либо нажмите на нее чтобы удалить.',
                        'delete_info_callback': 'Заметка удалена.',
                        'delete_info': 'Успешно удалено.',
                        'text_long_err': 'Текст слишком длинный!',
                        'add_info': 'Заметка добавлена!',
                        'actions': 'kb.actions_ru'}
            case 'Deutsch 🇩🇪':
                return {'text_info': 'Ihre Sprache ist',
                        'text_add_note': 'Schreiben Sie eine Notiz in den Chat, oder klicken Sie darauf, um ihn zu löschen.',
                        'delete_info_callback': 'Notiz wurde gelöscht.',
                        'delete_info': 'Erfolgreich entfernt.',
                        'text_long_err': 'Text ist zu lang!',
                        'add_info': 'Notiz wurde hinzugefügt!',
                        'actions': 'kb.actions_de'}

            case 'English 🇬🇧':
                return {'text_info': 'Your language is',
                        'text_add_note': 'Write a note in the chat, or click on it to delete it.',
                        'delete_info_callback': 'Note was deleted.',
                        'delete_info': 'Successfully removed.',
                        'text_long_err': 'Text is too long!',
                        'add_info': 'Note was added.',
                        'actions': 'kb.actions_en'}