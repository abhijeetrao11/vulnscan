async function startScan(){

    const target =
        document.getElementById("target").value;

    document.getElementById(
        "status"
    ).innerHTML =
        "Scanning...";

    const response =
        await fetch(
            "http://localhost:3000/scan",
            {
                method:"POST",

                headers:{
                    "Content-Type":
                        "application/json"
                },

                body:JSON.stringify({
                    target
                })
            }
        );

    const data =
        await response.json();

    if(data.success){

        document.getElementById(
            "status"
        ).innerHTML =
            "Scan Complete";

        document.getElementById(
            "reports"
        ).style.display =
            "block";
    }
}