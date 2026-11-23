# Multi-stage: build frontend, then run backend serving both

FROM node:20-alpine AS frontend-build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

FROM python:3.11-slim
WORKDIR /app

# Backend deps
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Backend code
COPY backend/ ./backend/

# Built frontend
COPY --from=frontend-build /app/frontend/dist ./frontend/dist

# Workspace
RUN mkdir -p /app/workspace /app/backend/data

ENV PYTHONPATH=/app/backend
ENV WORKSPACE_DIR=/app/workspace
ENV DATA_DIR=/app/backend/data

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "backend"]
