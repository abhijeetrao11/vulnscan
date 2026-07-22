const { exec } = require("child_process");
const runScanner = (target) => {
    return new Promise((resolve, reject) => {
        const command = `python3 /home/alfino/project_vuln_scanner/main.py ${target}`;
        exec(
            command,
            (error,stdout,stderr)=> {
                if(error){
                    reject(error.message);
                    return;
                }
                if(stderr){
                    reject(stderr);
                    return ;
                }
                resolve(JSON.parse(stdout));
            }
        );
    });
};

module.exports = {
    runScanner
};