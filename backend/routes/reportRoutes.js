const express = require("express");

const router = express.Router();

const {
    htmlReport,
    pdfReport
} = require("../controllers/reportController");

router.get("/html", htmlReport);

router.get("/pdf", pdfReport);

module.exports = router;