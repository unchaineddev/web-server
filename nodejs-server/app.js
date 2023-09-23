const http = require('http') // library to start server
const fs = require('fs') // file handling
const port = 8081


const server = http.createServer(function(req, res){
    res.writeHead(200, { 'Content-Type': 'text/html'})
    fs.readFile('index.html', function(error, data) {
        if(error){
            res.writeHead(404)
            res.write("Error: 404 Not Found!")
        }
        else{
            res.write(data)
        }
        res.end()
    })
})


server.listen(port, function(error){
    if (error){
        console.log("There was an error:", error)
    }
    else{
        console.log('Server is listening on port: ' + port)
    }
})