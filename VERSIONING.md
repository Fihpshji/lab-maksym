# Політика версіонування

## Семантичне версіонування (SemVer)

Формат версії: `MAJOR.MINOR.PATCH`.

| Частина | Коли змінюється | Приклад |
|---|---|---|
| MAJOR | несумісні (зламні) зміни API | 1.1.1 → 2.0.0 |
| MINOR | нова функціональність, сумісна зі старою | 1.0.0 → 1.1.0 |
| PATCH | виправлення помилок без зміни API | 1.1.0 → 1.1.1 |

Приклад історії версій: `1.0.0` → `1.1.0` (додано SQLite) → `1.1.1` (виправлено баг) → `2.0.0` (змінено формат відповіді API).

## Git-стратегія: спрощений GitFlow

Команда складається з 1–2 осіб, тому гілка `release/*` не використовується.

- `main` — стабільні релізні версії (кожен коміт має тег);
- `develop` — інтеграція фіч;
- `feature/*` — окрема гілка на кожну фічу (від `develop`);
- `hotfix/*` — термінові виправлення (від `main`, зливаються в `main` і `develop`).

## Формат комітів

`type(scope): опис`, де type: `feat`, `fix`, `docs`, `test`, `chore`.

Приклад: `feat(auth): add login endpoint`.

## Команди

```bash
git checkout -b feature/add-login develop
git add .
git commit -m "feat(auth): add login endpoint"
git push origin feature/add-login

# після код-рев'ю
git checkout develop
git merge --no-ff feature/add-login
git push origin develop

# реліз
git checkout main
git merge --no-ff develop
git tag -a v1.0.0 -m "Release 1.0.0"
git push origin main v1.0.0
```
