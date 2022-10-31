# Build off of the alpine image to keep this image as small as possible

FROM node:10.13.0-alpine

WORKDIR /usr/src/app

RUN npm install --global nodemon

# Copy package.json into the image and install before copying everything else
COPY package.json ./
RUN npm install

COPY . .

CMD ["./startup.sh"]
