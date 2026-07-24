const path = require("path");

const htmlReport = (req, res) => {

    res.sendFile(
        path.join(
            "/home/alfino/project_vuln_scanner/report.html"
        )
    );
};

const pdfReport = (req, res) => {

    res.download(
        "/home/alfino/project_vuln_scanner/report.pdf"
    );
};

module.exports = {
    htmlReport,
    pdfReport
};