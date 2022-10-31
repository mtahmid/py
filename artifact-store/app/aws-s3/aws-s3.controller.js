/**
 * This controller takes in seleniumlog, driverlog, and video files from Zalenium and sends it to S3.
 *
 */

module.exports = function(s3, asyncHandler) {
    const uploadArtifact = asyncHandler(async (req, res, next) => {
        const s3Client = s3.s3Client;
        const params = s3.uploadParams;

        if (process.env.AWS_S3_BUCKET) {
            if (req.files.seleniumlog && req.files.seleniumlog.length > 0) {
                const artifact = req.files.seleniumlog[0];
                const message = `artifact received but no action taken for ${artifact.originalname}`;
                return res.status(202).json({message});
            } else if (req.files.driverlog && req.files.driverlog.length > 0) {
                const artifact = req.files.driverlog[0];
                const message = `artifact received but no action taken for ${artifact.originalname}`;
                return res.status(202).json({message});
            } else if (req.files.video && req.files.video.length > 0) {
                const artifact = req.files.video[0];
                const meta = JSON.parse(req.body.metadata);

                params.Key = `${meta.testRun}/${meta.browser}-${meta.platform}/${meta.testCase}.mp4`;
                params.Body = artifact.buffer;

                return s3Client.upload(params).promise().then((data) => {
                    res.json({message: 'File uploaded successfully! -> keyname = ' + artifact.originalname});
                }).catch((err) => {
                    throw new Error("Error sending artifact to s3");
                });
            } else {
                throw new Error("Unknown file type");
            }
        }
        else {
            console.log("AWS_S3_BUCKET env var not set or False, skipping artifact upload.");
        }
    });

    return {
        uploadArtifact: uploadArtifact
    };
};
