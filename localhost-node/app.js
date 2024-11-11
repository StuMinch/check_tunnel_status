const express = require('express');
const app = express();
const port = 9080;

app.get('/', (req, res) => {
    res.send('Look at me I am running locally with a custom host entry!');
});

app.listen(port, () => {
    console.log(`App is running on http://magicalkingdom.local:${port}`);
});
