const path = require("path");

const downloadHTML = (req,res) => {

    const filePath = path.join(__dirname,"../../report.html");
    res.download(filePath);

};


const downloadPDF = (req,res) => {

    const filePath = path.join(__dirname,"../../report.pdf");
    res.download(filePath);

};
module.exports = {downloadHTML,downloadPDF};