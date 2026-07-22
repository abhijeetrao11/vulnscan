const express = require("express");
const router = express.Router();

const {
    scan
} = require("../controllers/scanController");

router.post(
    "/",
    scan
);

module.exports = router;

