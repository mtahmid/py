const bodyParser = require('body-parser');
const express = require('express');

const Controller = require('./aws-s3.controller.js');
const Router = require('./aws-s3.router.js');

module.exports = (upload, s3, asyncHandler) => {
    /* Parse HTTP request bodies as JSON */
    const route = express.Router();
    route.use(bodyParser.json());

    const controller = new Controller(s3, asyncHandler);

    /* Instantiate the routers */
    const router = new Router(route, controller, upload);

    return router;
}
