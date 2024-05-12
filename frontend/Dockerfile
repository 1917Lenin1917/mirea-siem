FROM node:latest

COPY . .
RUN npm install
RUN npm run build
RUN npm install -g serve
EXPOSE 5173
CMD ["serve", "-l", "5173", "-s", "dist"]