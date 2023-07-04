from django.core.files.storage import FileSystemStorage


class FileSystemOverwriteStorage(FileSystemStorage):
    """
    Кастомное хранилище
    Уже существующие файлы заменяются вместо добавления новых
    """
    def get_available_name(self, name, max_length=None):

        if self.exists(name):
            self.delete(name)
        return super().get_available_name(name, max_length)
