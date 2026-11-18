# Security configuration

The document-query endpoint `POST /preguntar` requires an API key. Set a long random secret as the `ATENEA_API_KEY` environment variable in your hosting provider's secret/environment settings. Never commit the value to GitHub.

Send it in the `X-API-Key` request header. Without this environment variable, the endpoint deliberately returns HTTP 503; with an incorrect key, it returns HTTP 401. The public health endpoint `GET /` remains available.

Example request (replace placeholders locally, never commit actual keys):

```bash
curl -X POST https://YOUR-HOST/preguntar -H 'Content-Type: application/json' -H 'X-API-Key: YOUR_KEY' -d '{"pregunta":"Consulta de ejemplo"}'
```

Important: the default Swagger UI may expose a manually entered header to whoever has access to that browser session. Do not share keys in screenshots or logs. This API-key mechanism is appropriate for trusted server-to-server clients; for public browser apps, use a backend proxy or user authentication rather than embedding a shared secret in frontend code.

Before merging this branch, configure the environment variable and update clients that call `/preguntar`. Also review indexed documents for confidential or personal information. Do not use real corporate documents without permission.
