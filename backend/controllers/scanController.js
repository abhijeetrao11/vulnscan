const {
    runScanner
} = require("../services/scannerService");

const scan = async (req, res) => {

    try {

        const { target } = req.body;

        await runScanner(target);

        res.json({
            success: true,
            message: "Scan Complete"
        });

    }
    catch (err) {

        console.log(err);

        res.status(500).json({
            success: false,
            error: err
        });
    }
};

module.exports = {
    scan
};