'use strict';

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/node/svc/', (req, res) => {
  res.send('Hello world from node application\n');
});

app.get('/', (req, res) =>{
  res.status(200).send('Welcome to NodeJS world.')
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);