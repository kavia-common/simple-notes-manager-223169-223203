# simple-notes-manager-223169-223203

Simple Notes Manager backend (Django + DRF)

Health
- GET /health -> {"status":"ok"}
- GET /api/health/ -> {"status":"ok"}

Notes CRUD (JSON)
- GET /api/notes/ : list notes
- POST /api/notes/ : create note
  body: {"title":"My note","content":"Body"}
- GET /api/notes/{id}/ : retrieve note
- PUT /api/notes/{id}/ : replace note
- PATCH /api/notes/{id}/ : partial update
- DELETE /api/notes/{id}/ : delete note

Example curl
- Health
  curl -s https://localhost:3001/health || true
  curl -s https://localhost:3001/api/health/ || true

- Create
  curl -s -X POST https://localhost:3001/api/notes/ \
    -H "Content-Type: application/json" \
    -d '{"title":"First","content":"Hello"}'

- List
  curl -s https://localhost:3001/api/notes/

- Get by id
  curl -s https://localhost:3001/api/notes/1/

- Update
  curl -s -X PUT https://localhost:3001/api/notes/1/ \
    -H "Content-Type: application/json" \
    -d '{"title":"Updated","content":"Changed"}'

- Patch
  curl -s -X PATCH https://localhost:3001/api/notes/1/ \
    -H "Content-Type: application/json" \
    -d '{"content":"Patched"}'

- Delete
  curl -s -X DELETE https://localhost:3001/api/notes/1/

Notes
- Uses SQLite by default, no extra env required.
- CORS is permissive for development.
- Swagger docs: /docs