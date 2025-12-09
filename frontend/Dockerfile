# --- Build step ---
FROM node:22-alpine AS builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build


# --- Runtime step ---
FROM node:22-alpine

WORKDIR /app

COPY --from=builder /app/dist ./dist

# Installer un petit serveur statique (serve)
RUN npm install -g serve

EXPOSE 5173

CMD ["serve", "-s", "dist", "-l", "5173"]