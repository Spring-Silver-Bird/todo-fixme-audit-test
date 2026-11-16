# TODO/FIXME audit sandbox

Тестовый репозиторий для проверки workflow аудита `TODO`/`FIXME` через OpenCode.

- Workflow: `.github/workflows/todo-fixme-audit.yml`
- Запуск: вручную (`workflow_dispatch`) или по расписанию (понедельник, 06:00 UTC)
- Результат: artifact `todo-fixme-report` + tracking issue `[todo-audit]`
- Отчёты в репозиторий не коммитятся

Файлы в `src/` и `docs/` синтетические: они нужны, чтобы проверить критерии находки,
включая ложные срабатывания (`StatusType.TODO`, строковые литералы) и исключение
сгенерированных файлов.
