'''
Создать класс LogAnalyzer.

На вход передавать список логов
Методы:
1. count_by_level() — количество сообщений каждого уровня.
2. get_errors() — получить все ERROR.
3. get_most_common_error() — найти наиболее частую ошибку.
4. get_summary() — вернуть общую статистику.

Вопросы:
- Как организовать хранение логов?
- Как не загружать большой файл целиком в память?
- Как разделить ответственность между классами LogAnalyzer и LogReader?
- Нужен ли отдельный класс для логирования?
'''

logs = [
    "INFO: Test started",
    "ERROR: Connection timeout",
    "INFO: Test passed",
    "ERROR: Database unavailable",
    "WARNING: Slow response",
    "ERROR: Connection timeout",
]

analyzer = LogAnalyzer(logs)