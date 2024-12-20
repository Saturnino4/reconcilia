FROM node:20

# Create a non-root user
WORKDIR /app

COPY package.json .
COPY package-lock.json .


RUN npm i - g @vue/cli
RUN npm install -g yarn
RUN yarn install

COPY . .

CMD ["yarn", "serve" "--ignore-engines"]



