const express = require("express");
const cors = require("cors");
const morgan = require("morgan");




const scanRoutes = require("./routes/scanRoutes");
const reportRoutes = require("./routes/reportRoutes");

const app = express();


app.use(cors());
app.use(express.json());
app.use(morgan("dev"));

app.use("/scan", scanRoutes);
app.use("/report", reportRoutes);

app.get("/", (req, res) => {
    res.json({
        message: "Backend Running"
    });
});

const PORT = 3000;

app.listen(PORT, () => {
    console.log(`Server running on ${PORT}`);
});