/**
 * Created by BIT on 2017-02-22.
 */

var express = require('express');
var router = express.Router();

//request,response ?
router.get('/',function (req,res) {
    res.render('index',{title:'Express'});
});

module.exports = router;

