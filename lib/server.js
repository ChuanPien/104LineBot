const http = require('http');
const fs = require('fs');
const path = require('path');

const port = 3000;
const jsonFilePath = path.join(__dirname, '../Crawler/job.json');

const server = http.createServer((req, res) => {
  // 设置 CORS 头部
  res.setHeader('Access-Control-Allow-Origin', '*'); // 允许所有域名访问，也可以设置为你的前端页面的域名

  if (req.url === '/data') {
    fs.readFile(jsonFilePath, 'utf8', (err, data) => {
      if (err) {
        res.writeHead(500);
        res.end('Error reading JSON file');
      } else {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(data);
      }
    });
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

server.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
