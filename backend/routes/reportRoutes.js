const express = require("express");

const router = express.Router();

const {
    downloadHTML, 
    downloadPDF
}
=
require("../controllers/reportController");

router.get("/html",downloadHTML);
router.get("/pdf",downloadPDF);
module.exports = router;
