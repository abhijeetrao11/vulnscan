const {
    runScanner
} = require("../services/scannerService");


const scan = async (req,res) => {

    try{
       const { target } = req.body;
       
       const result = await runScanner(target);

        res.json({
            success: true,
            output: result
        }); 
    }
    catch (err){
        res.status(500).json({
            success: false,
            error: err
        });
    }
    
};

module.exports = {
    scan
};
