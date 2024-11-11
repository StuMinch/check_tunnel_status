const express = require('express');
const app = express();
const port = 5000;

app.get('/', (req, res) => {
    const gifUrl = 'https://afterstorygaming.com/wp-content/uploads/2018/09/2cn2fp9xzgoqpgm80rntizsjse2zjl5yflqwh_wz7c0.png?w=750'; // Replace with your GIF URL
    res.send(`
        <html>
            <head>
                <title>Winnie</title>
            </head>
            <body>
                <h1>Look at me I am running on the local host with a custom host entry!</h1>
                <img src="${gifUrl}" alt="Spidey" />
            </body>
        </html>
    `);
});

app.listen(port, () => {
    console.log(`App is running on http://web-store.ps.com:${port}`);
});
