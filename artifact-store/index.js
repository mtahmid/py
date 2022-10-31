const express = require('express');

const upload = require('./config/multer.config.js');
const s3 = require('./config/s3.config.js');
const asyncHandler = require('./utils/async-handler.js');
const app = express();

/**
 * Import the API endpoints. Each component is an instance of an ExpressJS router.
 * Here the application (general utility) component, and the ToDos component are loaded.
 */
const awsS3Component = require('./app/aws-s3')(upload, s3, asyncHandler);

/**
 * Bind all of the API endpoints to the express application.
 * Bind the application component with no mountpoint, so the application component executes for each HTTP request.
 * Bind the todos component with the /todos, so the todos component executes for each HTTP request that goes to /todos.
 */
app.use('/', awsS3Component);

/**
 * Error for catching 404 errors
 */
app.use((req, res) => {
    res.status(404).send('404');
})

/**
 * This is the error handling middleware, all errors that are passed to middleware are processed here.
 */
app.use(function(err, req, res, next) {
    console.error(err.stack); // Hidden when NODE_ENV is in production

    if (!err.statusCode) {
        err.statusCode = 500;
    }
    res.status(err.statusCode).send(err.message);
});

app.listen(9000, () => {
    console.log('listening on port 9000')
});
