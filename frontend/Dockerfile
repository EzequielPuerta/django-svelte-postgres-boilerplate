FROM node:20-slim

WORKDIR /app

ARG API_URL
ENV API_URL=$API_URL
ARG API_TOKEN
ENV API_TOKEN=$API_TOKEN

COPY package.json pnpm-lock.yaml ./

RUN npm install -g pnpm
RUN pnpm install

COPY . .

EXPOSE 5173

CMD ["pnpm", "run", "dev"]
