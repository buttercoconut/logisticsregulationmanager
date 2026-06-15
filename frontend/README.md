# Logistics Regulation Manager Frontend

This is a minimal Vue 3 SPA that consumes the Logistics Regulation Manager API.

## Setup

```bash
cd /home/yutw/project/md_templates/results/logisticsregulationmanager/frontend
npm install
npm run dev
```

The app will be available at `http://localhost:5173`.

## Features

- List regulations with search
- View regulation details
- Simple routing

## Notes

- The API base URL is hard‑coded to `http://localhost:8000/api`. Adjust `src/services/api.js` if your backend runs elsewhere.
- This is a starting point; you can extend it with authentication, pagination, etc.
