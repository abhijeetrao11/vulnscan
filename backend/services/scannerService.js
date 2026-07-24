const { exec } = require("child_process");

const runScanner = (target) => {

    return new Promise((resolve, reject) => {

        const command =
            `python3 /home/alfino/project_vuln_scanner/main.py "${target}" --html --pdf`;

        console.log(command);

        exec(command, (error, stdout, stderr) => {

            if (error) {
                reject(error.message);
                return;
            }
            console.log("STDOUT:");
            console.log(stdout);

            console.log("STDERR:");
            console.log(stderr);

            resolve();
            
        });
    });
};

module.exports = {
    runScanner
};