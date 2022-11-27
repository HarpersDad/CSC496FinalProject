var express = require("express");
var app = express();
var port = 3000;
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

var mongoose = require("mongoose");
const { response } = require("express");
mongoose.Promise = global.Promise;
mongoose.connect("mongodb+srv://root:mongoPass@cluster0.ddvbnxo.mongodb.net/?retryWrites=true&w=majority");

var nameSchema = new mongoose.Schema({
    name: String,
    str: String,
    con: String,
    dex: String,
    wis: String,
    int: String,
    cha: String,
    userName: String
});
var User = mongoose.model("User", nameSchema);

var rootPage = __dirname + "/";
var homePage = __dirname + "/pages/home.html";
var statPage = __dirname + "/pages/index.html";
var charPage = __dirname + "/pages/grab.html";

app.get("/", (req, res) => {
    res.sendFile(homePage);
});

app.get("/pages/grab.html", (req, res) => {
    res.sendFile(charPage);
});

app.get("/pages/index.html", (req, res) => {
    res.sendFile(statPage);
});

app.get("/pages/home.html", (req, res) => {
    res.sendFile(homePage);
});

app.post("/addname", (req, res) => {
    var myData = new User(req.body);
    myData.save()
        .then(item => {
            res.sendFile(homePage);
        })
        .catch(err => {
            res.status(400).send("Unable to save to database");
        })
});

app.listen(port, () => {
    console.log("Server listening on port " + port);
});