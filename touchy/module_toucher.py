import pathlib

from .file_toucher import FileToucher


class ModuleToucher:
    def __init__(self, module_path):
        self._module_path = pathlib.Path(module_path)
        self._files_in_module = self.generate_file_list(self._module_path)
        self._texts_in_module = []

    @property
    def module_name(self):
        return self._module_path.name

    @property
    def texts_in_module(self):
        return self._texts_in_module

    @staticmethod
    def generate_file_list(module_path):
        """Generate a list of files in a given path"""
        touch_path = pathlib.Path(module_path)
        return [file for file in touch_path.rglob("*.py") if file.is_file()]

    def touch(self):
        for filename in self._files_in_module:
            touching = FileToucher(filename)
            touching.touch()
            self._texts_in_module.append(touching.text)
