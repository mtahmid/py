const multer = require('multer');

var storage = multer.memoryStorage()
var upload = multer({
    storage: storage,
    filename: function (req, file, cb) {
        cb(null, file.originalname)
    }
});

module.exports = upload;
