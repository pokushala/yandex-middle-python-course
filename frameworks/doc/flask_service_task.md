# Задание

Реализуйте сервис, который отдаёт JSON. В нём содержится User-Agent клиента, который сделал запрос.
Реализуйте метод `GET /client/info`.
В ответ сервис должен вернуть заголовок `Content-Type` со значением `application/json.
Тело ответа должно быть в формате JSON.`

```json
{
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15"
}
```

Важно, что бы сервер запустился на `8000` порту.

Для проверки работоспособности вашего решения используйте UserAgent-API.json.

# Запуск решения

Для запуска должен быть установлен docker.
В директории frameworks/user_agent ввести 

`docker build . -t user-agent`

`docker run -p 8000:8000 user-agent`