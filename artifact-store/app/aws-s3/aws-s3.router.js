/**
 * This file is responsible for creating all the route and calling upon the
 * respective controller
 *
 * @param route is the express router
 * @param controller the controller for the API
 */

module.exports = function (route, controller, upload) {
    const uploadFields = upload.fields([
        { name: 'video', maxCount: 1 },
        { name: 'driverlog', maxCount: 1 },
        { name: 'seleniumlog', maxCount: 1 }
    ]);

    route.post('/', uploadFields, controller.uploadArtifact);

    return route;
};
