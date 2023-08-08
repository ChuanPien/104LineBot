const http = require('http');
const fs = require('fs');
const path = require('path');

const port = 3000;
const jobFile = path.join(__dirname, '../Crawler/job.json');
const cityFile = path.join(__dirname, '../Crawler/city.json');

const server = http.createServer((req, res) => {
  // 设置 CORS 头部
  res.setHeader('Access-Control-Allow-Origin', '*');

  if (req.url === '/job') {
    fs.readFile(jobFile, 'utf8', (err, data) => {
      if (err) {
        res.writeHead(500);
        res.end('Error reading Job file');
      } else {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(data);
      }
    });
  } 
  else if  (req.url === '/city') {
    fs.readFile(cityFile, 'utf8', (err, data) => {
      if (err) {
        res.writeHead(500);
        res.end('Error reading City file');
      } else {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(data);
      }
    });
  }
  else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

server.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
