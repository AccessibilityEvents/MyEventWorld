# dockerfile für frontend -> excalidraw
FROM node:20-alpine3.17
WORKDIR /serve
COPY frontend-neu/ /serve/
RUN ls -R /serve/
RUN npm install && npm run build
EXPOSE 3000
CMD ["node", "build/index.js"]