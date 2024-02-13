# Design-patterns

## Изменения:
1. Переделан этот репозиторий
2. Добавлен новый тест в Tests/test-settinfs.py:
   ```
   def test_check_open_settings_with_custom_path(self):
    # Подготовка
    manager = settings_manager()

    # Действие
    result = manager.open("settings.json") #путь к файлу настроек

    # Проверка
    self.assertTrue(result)
    self.assertEqual(manager.data["name"], "Company")
    self.assertEqual(manager.data["inn"], "123456789012")
    self.assertEqual(manager.data["account"], "12345678901")
    self.assertEqual(manager.data["correspondent_account"], "98765432109")
    self.assertEqual(manager.data["bik"], "987654321")
    self.assertEqual(manager.data["ownership_type"], "ABCDE")
   ```
3. Добавлен value.strip() в Source/settings.py для всех определений переменных
