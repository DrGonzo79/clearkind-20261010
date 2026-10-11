# ClearKind

A runnable prototype for calmly triaging household items during an estate clear-out. The static Next.js demo and tested FastAPI engine share the same explicit fictional fixtures.

## What works

- Filter a fictional estate queue by room.
- Mark the family signal, set the deadline, and generate a transparent route.
- Complete the route-specific safe-action checklist.
- Validate invalid timelines and surface empty/loading states.

No image recognition, appraisal, live marketplace data, or irreversible disposal automation is claimed. The Python API is source-only and is not publicly hosted.

## Run

```bash
npm ci
npm run dev
uv sync --project api --locked --dev
uv run --project api uvicorn main:app --app-dir api
```

## Verify

```bash
npm run typecheck
npm run test:e2e
npm run build
npm run audit:prod
uv run --project api pytest api/tests
```

Source: [Ideabrowser public idea page](https://www.ideabrowser.com/hub/ideas/help-families-decide-what-to-sell-donate-or-remove-from-an-estate-76e72927)
